# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, RegexValidator
from django.contrib.auth.models import User
from django.db.models import Sum

from hashids import Hashids
import datetime
import time
import uuid

from quirofanos_cmsb.helpers.custom_validators import ExpresionRegular, MensajeError, CodigoError
from quirofanos_cmsb.helpers import utils

# Tipos de Privilegios
PRIVILEGIO = (
    ('0', u'JEFE_PQ'),
    ('1', u'COORDINADOR_PQ'),
    ('2', u'EMERGENCIA_PQ'),
    ('3', u'ASISTENTE_PQ'),
    ('4', u'MEDICO'),
    ('5', u'OBSERVADOR_PRESUPUESTO'),
    ('6', u'OBSERVADOR'),
)

# Estados de una Cuenta
ESTADO_CUENTA = (
    ('P', u'Pendiente'),
    ('A', u'Aprobada'),
    ('R', u'Rechazada'),
)

# Estados de una Reservacion
ESTADO_RESERVACION = (
    ('P', u'Pendiente'),
    ('A', u'Aprobada'),
    ('R', u'Rechazada'),
)

# Generos
GENERO = (
    ('F', u'Femenino'),
    ('M', u'Masculino'),
)

# Tipos de Solicitud de Quirofano
TIPO_SOLICITUD_QUIROFANO = (
    ('0', u'Emergencia'),
    ('1', u'Electiva'),
)

# Estados de una Intervencion Quirurgica
ESTADO_INTERVENCION_QUIRURGICA = (
    ('0', u'En Espera'),
    ('1', u'En Curso'),
    ('2', u'En Recuperación'),
    ('3', u'En Habitación'),
)

# Tipos de Anestesia
TIPO_ANESTESIA = (
    ('G', u'General'),
    ('L', u'Local'),
)

# Tipos de Riesgo
TIPO_RIESGO = (
    ('B', u'Bueno'),
    ('R', u'Regular'),
    ('M', u'Malo'),
)

# Nombres de Areas
NOMBRE_AREA = (
    ('QG', u'Quirófano General'),
    ('A', u'Ambulatorio'),
    ('SP', u'Sala de Parto'),
    ('SEE', u'Sala de Estudios Endoscópicos'),
    ('SH', u'Sala de Hemodinamia'),
    ('AS', u'Anestesia en Servicio')
)

# Roles de medicos dentro de una Intervencion Quirurgica
ROL_PARTICIPACION = (
    ('0', u'Anestesiólogo'),
    ('1', u'Primer Ayudante'),
    ('2', u'Segundo Ayudante'),
    ('3', u'Tercer Ayudante'),
)

# Areas de ingreso asociadas al numero de expediente de un paciente
AREA_INGRESO = (
    ('AA', u'Admisión por Ambulatorio'),
    ('AE', u'Admisión por Emergencia'),
    ('AH', u'Admisión por Hospitalización'),
    ('AG', u'Admisión por Hemodinámica'),
    ('AL', u'Admisión por Laboratorio'),
    ('AX', u'Registro de Red Modificado'),
    )

class Cuenta (models.Model):
    ''' Clase que representa una Cuenta de Usuario '''
    usuario = models.OneToOneField(User)
    estado = models.CharField(max_length=1, choices=ESTADO_CUENTA)
    privilegio = models.CharField(max_length=1, choices=PRIVILEGIO)
    clave_inicial = models.CharField(max_length=10, validators=[MinLengthValidator(5)], blank=True, null=True)

    def save(self):
        ''' Sobreescribe el save() '''
        self.full_clean()
        super(Cuenta, self).save()

    def __unicode__(self):
        ''' Representacion unicode '''
        return self.usuario.username + ', ' + self.get_estado_display() + ', ' + self.get_privilegio_display()

class Medico (models.Model):
    ''' Clase que representa un Medico '''
    cuenta = models.OneToOneField(Cuenta, blank=True, null=True)
    nombre = models.CharField(max_length=50, validators=[
                              RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.NOMBRE_GENERAL_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])
    apellido = models.CharField(max_length=50, validators=[
                                RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.NOMBRE_GENERAL_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])
    cedula = models.CharField(max_length=12, unique=True, validators=[
                              RegexValidator(ExpresionRegular.CEDULA_BD, MensajeError.CEDULA_BD_INVALIDA, CodigoError.CEDULA_BD_INVALIDA)])
    genero = models.CharField(max_length=1, choices=GENERO)
    telefono = models.CharField(max_length=12, validators=[
                                RegexValidator(ExpresionRegular.TELEFONO_BD, MensajeError.TELEFONO_BD_INVALIDO, CodigoError.TELEFONO_BD_INVALIDO)], blank=True, null=True)
    email = models.EmailField(max_length=75, blank=True, null=True)
    especializacion = models.CharField(max_length=50, validators=[RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.NOMBRE_GENERAL_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])

    def clean(self):
        ''' Sobreescribe el clean(), colocando nombre, apellido capitalizados y el email todo en minuscula '''
        self.nombre = self.nombre.title()
        self.apellido = self.apellido.title()
        if self.email:
            self.email = self.email.lower()
        super(Medico, self).clean()

    def save(self):
        ''' Sobreescribe el save() '''
        self.full_clean()
        super(Medico, self).save()

    def __unicode__(self):
        ''' Representacion unicode '''
        return self.nombre + ' ' + self.apellido

class Departamento (models.Model):
    ''' Clase que representa un Departamento '''
    cuenta = models.OneToOneField(Cuenta, blank=True, null=True)
    nombre = models.CharField(max_length=50, unique=True, validators=[
                              RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.NOMBRE_GENERAL_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])
    telefono = models.CharField(max_length=12, validators=[
                                RegexValidator(ExpresionRegular.TELEFONO_BD, MensajeError.TELEFONO_BD_INVALIDO, CodigoError.TELEFONO_BD_INVALIDO)], blank=True, null=True)
    email = models.EmailField(max_length=75, blank=True, null=True)

    def clean(self):
        ''' Sobreescribe el clean(), colocando el nombre capitalizado y el email todo en minuscula '''
        self.nombre = self.nombre.title()
        if self.email:
            self.email = self.email.lower()
        super(Departamento, self).clean()

    def save(self):
        ''' Sobreescribe el save() '''
        self.full_clean()
        super(Departamento, self).save()

    def __unicode__(self):
        ''' Representacion unicode '''
        return self.nombre


class Quirofano(models.Model):
    ''' Clase que representa un Quirofano '''
    numero = models.IntegerField(validators=[MinValueValidator(0)])
    area = models.CharField(max_length=3, choices=NOMBRE_AREA)

    def save(self):
        ''' Sobreescribe el save() '''
        self.full_clean()
        super(Quirofano, self).save()

    def obtener_numero_intervenciones(self, ano, mes, dia):
        ''' Calcula el numero de intervenciones que estan pautadas para el quirofano para una fecha

        Parametros:
        ano -> Ano de la fecha a consultar
        mes -> Mes de la fecha a consultar
        dia -> Dia de la fecha a consultar '''
        try:
            return self.intervencionquirurgica_set.filter(fecha_intervencion__year=ano, fecha_intervencion__month=mes, fecha_intervencion__day=dia, reservacion__estado='A').count()
        except AttributeError:
            return 0;

    def esta_disponible(self, ano, mes, dia):
        ''' Devuelve un valor booleano que determina si el quirofano esta disponible o no para una fecha

        Parametros:
        ano -> Ano de la fecha a consultar
        mes -> Mes de la fecha a consultar
        dia -> Dia de la fecha a consultar '''
        try:
            return not self.intervencionquirugica_set.filter(fecha_intervencion__year=ano, fecha_intervencion__month=mes, fecha_intervencion__day=dia, reservacion__estado='A').aggregate(Sum('duracion')) > 12.00
        except AttributeError:
            return True

    def obtener_intervenciones_por_hora(self, ano, mes, dia):
        ''' Devuelve un diccionario en donde se tiene para cada media hora del dia una intervencion quirurgica que cubre ese horario

        Parametros:
        ano -> Ano de la fecha a consultar
        mes -> Mes de la fecha a consultar
        dia -> Dia de la fecha a consultar '''
        try:
            intervenciones = self.intervencionquirurgica_set.filter(fecha_intervencion__year=ano, fecha_intervencion__month=mes, fecha_intervencion__day=dia, reservacion__estado='A').order_by('hora_inicio')
            datos = {}
            for intervencion in intervenciones:
                for media_hora in intervencion.iterador_medias_horas():
                    datos[media_hora] = intervencion
            return datos
        except AttributeError:
            return None

    def __unicode__(self):
        ''' Representacion unicode '''
        return str(self.numero) + ', ' + self.get_area_display()


class MaterialQuirurgico(models.Model):
    ''' Clase que representa un Material Quirurgico '''
    nombre = models.CharField(max_length=50, validators=[
                              RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.NOMBRE_GENERAL_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])

    def clean(self):
        ''' Sobreescribe el clean(), colocando el nombre capitalizado '''
        self.nombre = self.nombre.title()
        super(MaterialQuirurgico, self).clean()

    def save(self):
        ''' Sobreescribe el save() '''
        self.full_clean()
        super(MaterialQuirurgico, self).save()

    def __unicode__(self):
        ''' Representacion unicode '''
        return self.nombre


class ServicioOperatorio(models.Model):
    ''' Clase que representa un Servicio Operatorio '''
    nombre = models.CharField(max_length=50, validators=[
                              RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.NOMBRE_GENERAL_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])

    def clean(self):
        ''' Sobreescribe el clean(), colocando el nombre capitalizado '''
        self.nombre = self.nombre.title()
        super(ServicioOperatorio, self).clean()

    def save(self):
        ''' Sobreescribe el save() '''
        self.full_clean()
        super(ServicioOperatorio, self).save()

    def __unicode__(self):
        ''' Representacion unicode '''
        return self.nombre


class EquipoEspecial(models.Model):
    ''' Clase que representa un Equipo Especial '''
    nombre = models.CharField(max_length=50, validators=[
                              RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.NOMBRE_GENERAL_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])

    def clean(self):
        ''' Sobreescribe el clean(), colocando el nombre capitalizado '''
        self.nombre = self.nombre.title()
        super(EquipoEspecial, self).clean()

    def save(self):
        ''' Sobreescribe el save() '''
        self.full_clean()
        super(EquipoEspecial, self).save()

    def __unicode__(self):
        ''' Representacion unicode '''
        return self.nombre


class SistemaCorporal(models.Model):
    ''' Clase que representa un Sistema Corporal segun el estandar ICD-10-PCS '''
    codigo_icd_10_pcs = models.CharField(
        max_length=2, unique=True, validators=[MinLengthValidator(2)])
    nombre = models.CharField(max_length=50, unique=True, validators=[
                              RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.NOMBRE_GENERAL_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])

    def clean(self):
        ''' Sobreescribe el clean(), colocando el codigo en mayuscula y el nombre capitalizado '''
        self.codigo_icd_10_pcs = self.codigo_icd_10_pcs.upper()
        self.nombre = self.nombre.title()
        super(SistemaCorporal, self).clean()

    def save(self):
        ''' Sobreescribe el save() '''
        self.full_clean()
        super(SistemaCorporal, self).save()

    def __unicode__(self):
        ''' Representacion unicode '''
        return self.nombre + ' [' + self.codigo_icd_10_pcs + ']'


class TipoProcedimientoQuirurgico(models.Model):
    ''' Clase que representa un Tipo Procedimiento Quirurgico segun el estandar ICD-10-PCS '''
    codigo_icd_10_pcs = models.CharField(max_length=1, unique=True)
    nombre = models.CharField(max_length=50, unique=True, validators=[
                              RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.NOMBRE_GENERAL_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])

    def clean(self):
        ''' Sobreescribe el clean(), colocando el codigo en mayuscula y el nombre capitalizado '''
        self.codigo_icd_10_pcs = self.codigo_icd_10_pcs.upper()
        self.nombre = self.nombre.title()
        super(TipoProcedimientoQuirurgico, self).clean()

    def save(self):
        ''' Sobreescribe el save() '''
        self.full_clean()
        super(TipoProcedimientoQuirurgico, self).save()

    def __unicode__(self):
        ''' Representacion unicode '''
        return self.nombre + ' [' + self.codigo_icd_10_pcs + ']'


class OrganoCorporal(models.Model):
    ''' Clase que representa un Organo Corporal segun el estandar ICD-10-PCS '''
    codigo_icd_10_pcs = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50, unique=True, validators=[
                              RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.NOMBRE_GENERAL_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])
    sistema_corporal = models.ForeignKey(SistemaCorporal)
    tipos_procedimientos_permitidos = models.ManyToManyField(TipoProcedimientoQuirurgico)

    def clean(self):
        ''' Sobreescribe el clean(), colocando el codigo en mayuscula y el nombre capitalizado '''
        self.codigo_icd_10_pcs = self.codigo_icd_10_pcs.upper()
        self.nombre = self.nombre.title()
        super(OrganoCorporal, self).clean()

    def save(self):
        ''' Sobreescribe el save() '''
        self.full_clean()
        super(OrganoCorporal, self).save()

    def __unicode__(self):
        ''' Representacion unicode '''
        return self.nombre

class CompaniaAseguradora(models.Model):
    nombre = models.CharField(max_length=50, validators=[RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.NOMBRE_GENERAL_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])

    def clean(self):
        ''' Sobreescribe el clean(), colocando el nombre capitalizado '''
        self.nombre = self.nombre.title()
        super(OrganoCorporal, self).clean()

    def save(self):
        ''' Sobreescribe el save() '''
        self.full_clean()
        super(CompaniaAseguradora, self).save()

    def __unicode__(self):
        ''' Representacion unicode '''
        return self.nombre

class Paciente(models.Model):
    ''' Clase que representa un Paciente '''
    nombre = models.CharField(max_length=50, validators=[
                              RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.NOMBRE_GENERAL_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])
    apellido = models.CharField(max_length=50, validators=[
                                RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.NOMBRE_GENERAL_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])
    cedula = models.CharField(max_length=12, unique=True, validators=[
                              RegexValidator(ExpresionRegular.CEDULA_BD, MensajeError.CEDULA_BD_INVALIDA, CodigoError.CEDULA_BD_INVALIDA)])
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    telefono = models.CharField(max_length=12, validators=[
                                RegexValidator(ExpresionRegular.TELEFONO_BD, MensajeError.TELEFONO_BD_INVALIDO, CodigoError.TELEFONO_BD_INVALIDO)])
    genero = models.CharField(max_length=1, choices=GENERO)
    compania_aseguradora = models.ForeignKey(CompaniaAseguradora, blank=True, null=True)
    area_ingreso = models.CharField(max_length=2, choices=AREA_INGRESO, blank=True, null=True)
    numero_expediente = models.CharField(
        max_length=6, blank=True, null=True, validators=[RegexValidator(ExpresionRegular.NUMERO_EXPEDIENTE, MensajeError.NUMERO_EXPEDIENTE_INVALIDO, CodigoError.NUMERO_EXPEDIENTE_INVALIDO)])
    numero_habitacion = models.CharField(
        max_length=3, blank=True, null=True, validators=[RegexValidator(ExpresionRegular.NUMERO_HABITACION, MensajeError.NUMERO_HABITACION_INVALIDO, CodigoError.NUMERO_HABITACION_INVALIDO)])
    diagnostico_ingreso = models.TextField()
    servicios_operatorios_requeridos = models.ManyToManyField(
        ServicioOperatorio, blank=True, null=True)

    def clean(self):
        ''' Sobreescribe el clean(), colocando nombre y apellido capitalizados '''
        self.nombre = self.nombre.title()
        self.apellido = self.apellido.title()

        if self.area_ingreso and not self.numero_expediente:
            raise ValidationError(MensajeError.AREA_INGRESO_SIN_NUMERO_EXPEDIENTE, code=CodigoError.AREA_INGRESO_SIN_NUMERO_EXPEDIENTE)

        if self.numero_expediente and not self.area_ingreso:
            raise ValidationError(MensajeError.NUMERO_EXPEDIENTE_SIN_AREA_INGRESO, code=CodigoError.NUMERO_EXPEDIENTE_SIN_AREA_INGRESO)

        super(Paciente, self).clean()

    def save(self):
        ''' Sobreescribe el save() '''
        self.full_clean()
        super(Paciente, self).save()

    def __unicode__(self):
        ''' Representacion unicode '''
        return self.nombre + ' ' + self.apellido


class IntervencionQuirurgica(models.Model):
    ''' Clase que representa una Intervencion Quirurgica '''
    fecha_intervencion = models.DateField(auto_now=False, auto_now_add=False)
    hora_inicio = models.TimeField(auto_now=False, auto_now_add=False)
    hora_fin = models.TimeField(auto_now=False, auto_now_add=False)
    duracion = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    estado = models.CharField(
        max_length=1, choices=ESTADO_INTERVENCION_QUIRURGICA)
    preferencia_anestesica = models.CharField(
        max_length=1, choices=TIPO_ANESTESIA)
    observaciones = models.TextField(blank=True, null=True)
    riesgo = models.CharField(max_length=1, choices=TIPO_RIESGO)
    razon_riesgo = models.TextField(blank=True, null=True)
    paciente = models.OneToOneField(Paciente)
    materiales_quirurgicos_requeridos = models.ManyToManyField(
        MaterialQuirurgico, blank=True, null=True)
    equipos_especiales_requeridos = models.ManyToManyField(
        EquipoEspecial, blank=True, null=True)
    quirofano = models.ForeignKey(Quirofano)

    def clean(self):
        ''' Sobreescribe el clean(), validando los valores del riesgo y la razon del riesgo, ademas de calcular la duracion de la Intervencion Quirurgica '''
        if self.riesgo == 'M' and self.razon_riesgo is None:
            raise ValidationError(
                MensajeError.RIESGO_MALO_SIN_RAZON_BD, code=CodigoError.RIESGO_MALO_SIN_RAZON_BD)
        elif self.riesgo != 'M' and self.razon_riesgo is not None:
            raise ValidationError(
                MensajeError.RIESGO_NO_MALO_CON_RAZON_BD, code=CodigoError.RIESGO_NO_MALO_CON_RAZON_BD)

        if self.hora_fin <= self.hora_inicio:
            raise ValidationError(
                MensajeError.HORA_FIN_MENOR_HORA_INICIO, code=CodigoError.HORA_FIN_MENOR_HORA_INICIO)

        hora_inicio_seg = datetime.timedelta(
            hours=self.hora_inicio.hour, minutes=self.hora_inicio.minute).total_seconds()
        hora_fin_seg = datetime.timedelta(
            hours=self.hora_fin.hour, minutes=self.hora_fin.minute).total_seconds()
        diferencia_horas = float(hora_fin_seg) - float(hora_inicio_seg)
        self.duracion = round(diferencia_horas / 3600, 2)

        if self.duracion < 1.00:
            raise ValidationError(
                MensajeError.DURACION_MENOR_QUE_UNA_HORA, code=CodigoError.DURACION_MENOR_QUE_UNA_HORA)

        super(IntervencionQuirurgica, self).clean()

    def save(self):
        ''' Sobreescribe el save() '''
        self.full_clean()
        super(IntervencionQuirurgica, self).save()

    def obtener_monto_honorarios_total(self):
        ''' Devuelve el monto total de honorarios de la Intervencion Quirurgica '''
        monto_honorarios_total = 0
        for procedimiento in self.procedimientoquirurgico_set.all():
            monto_honorarios_total = monto_honorarios_total + procedimiento.obtener_monto_honorarios_total()
        return monto_honorarios_total

    def obtener_hora_inicio_horas(self):
        ''' Devuelve la hora de inicio como un float '''
        return round(datetime.timedelta(hours=self.hora_inicio.hour, minutes=self.hora_inicio.minute).total_seconds() / 3600, 2)

    def obtener_hora_fin_horas(self):
        ''' Devuelve la hora de fin como un float '''
        return round(datetime.timedelta(hours=self.hora_fin.hour, minutes=self.hora_fin.minute).total_seconds() / 3600, 2)

    def iterador_medias_horas(self):
        ''' Devuelve un iterador sobre las medias horas del dia que cubre la intervencion quirurgica '''
        hora_inicio_horas = self.obtener_hora_inicio_horas()
        hora_fin_horas = self.obtener_hora_fin_horas()
        return utils.rango_decimal(hora_inicio_horas, hora_fin_horas, 0.5)

    def __unicode__(self):
        ''' Representacion unicode '''
        return self.paciente.__unicode__() + ', ' + self.reservacion.medico.__unicode__() + ', ' + str(self.fecha_intervencion)

class ProcedimientoQuirurgico(models.Model):
    ''' Clase que representa un Procedimiento Quirurgico '''
    intervencion_quirurgica = models.ForeignKey(IntervencionQuirurgica, blank=True, null=True)
    tipo_procedimiento_quirurgico = models.ForeignKey(TipoProcedimientoQuirurgico)
    organo_corporal = models.ForeignKey(OrganoCorporal)
    monto_honorarios_cirujano_principal = models.DecimalField(max_digits=15, decimal_places=2)
    medicos_participantes = models.ManyToManyField(Medico, through='Participacion')

    def save(self):
        ''' Sobreescribe el save() '''
        self.full_clean()
        super(ProcedimientoQuirurgico, self).save()

    def obtener_monto_honorarios_anestesiologo(self):
        return round(0.4*self.monto_honorarios_cirujano_principal, 2)

    def obtener_monto_honorarios_primer_ayudante(self):
        return round(0.4*self.monto_honorarios_cirujano_principal, 2)

    def obtener_monto_honorarios_segundo_ayudante(self):
        return round(0.3*self.monto_honorarios_cirujano_principal, 2)

    def obtener_monto_honorarios_total(self):
        ''' Devuelve el monto total de honorarios del procedimiento quirurgico '''
        monto_honorarios_total = monto_honorarios_cirujano_principal
        for medico in self.medicos_participantes.all():
            participacion = Participacion.get(procedimiento_quirurgico=self, medico=medico)
            monto_honorarios_total = monto_honorarios_total + participacion.monto_honorarios
        return monto_honorarios_total

    def __unicode__(self):
        ''' Representacion unicode '''
        return self.intervencion_quirurgica.__unicode__() + ', ' + self.organo_corporal.sistema_corporal.__unicode__() + ', ' + self.tipo_procedimiento_quirurgico.__unicode__() + ', ' + self.organo_corporal.__unicode__()


class Participacion(models.Model):
    ''' Clase que representa la Participacion de un Medico en un Procedimiento Quirurgico '''
    procedimiento_quirurgico = models.ForeignKey(ProcedimientoQuirurgico)
    medico = models.ForeignKey(Medico)
    rol = models.CharField(max_length=1, choices=ROL_PARTICIPACION)
    monto_honorarios = models.DecimalField(max_digits=15, decimal_places=2)

    def save(self):
        ''' Sobreescribe el save() '''
        self.full_clean()
        super(Participacion, self).save()

    def __unicode__(self):
        ''' Representacion unicode '''
        return self.intervencion_quirurgica.__unicode__() + ', ' + self.medico.__unicode__() + ', ' + self.get_rol_display()


class Reservacion (models.Model):
    ''' Clase que representa una Reservacion de Intervencio Quirurgica '''
    fecha_reservacion = models.DateField(auto_now=True, auto_now_add=True)
    codigo = models.CharField(
        max_length=10, unique=True, validators=[MinLengthValidator(5)], default='00000')
    estado = models.CharField(max_length=1, choices=ESTADO_RESERVACION)
    tipo_solicitud = models.CharField(
        max_length=1, choices=TIPO_SOLICITUD_QUIROFANO)
    dias_hospitalizacion = models.IntegerField(
        validators=[MinValueValidator(0)], default=0)
    medico = models.ForeignKey(Medico)
    intervencion_quirurgica = models.OneToOneField(IntervencionQuirurgica)

    def save(self):
        ''' Sobreescribe el save(), asignando un codigo de reservacion unico '''
        self.full_clean()

        super(Reservacion, self).save()

        hashids = Hashids(min_length=5, salt=uuid.uuid1().hex)
        self.codigo = hashids.encrypt(self.id).upper()
        super(Reservacion, self).save()

    def __unicode__(self):
        ''' Representacion unicode '''
        return self.intervencion_quirurgica.__unicode__() + ', ' + self.get_tipo_solicitud_display() + ', ' + self.get_estado_display() + ', ' + str(self.fecha_reservacion)

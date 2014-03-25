# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.core.exceptions import ValidationError

# from hashids import Hashids
import datetime
import time
import uuid

# Tipos de Privilegios
PRIVILEGIO = (
	('0', u'JEFE_PQ'),
	('1', u'COORDINADOR_PQ'),
	('2', u'ASISTENTE_PQ'),
	('3', u'MEDICO'),
	('4', u'OBSERVADOR'),
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

# Parentezco de Pacientes y Medicos
PARENTEZCO = (
	('0', u'Padre'),
	('1', u'Madre'),
	('2', u'Hijo(a)'),
	('3', u'Hermano(a)'),
	('4', u'Abuelo(a)'),
	('5', u'Nieto(a)'),
	('6', u'Tío(a)'),
	('7', u'Primo(a)'),
	('8', u'Esposo(a)'),
	('9', u'Sobrino(a)'),
	)


class Cuenta (models.Model):
	''' Clase que representa una Cuenta de Usuario '''
	nombre_usuario = models.CharField(max_length=20, unique=True)
	contrasena = models.CharField(validators=[MinLengthValidator(64)], max_length=64)
	estado = models.CharField(max_length=1, choices=ESTADO_CUENTA)
	privilegio = models.CharField(max_length=1, choices=PRIVILEGIO)
	fecha_creacion = models.DateField(auto_now=True, auto_now_add=True)

	def save(self):
		''' Sobreescribe el save() '''
		self.full_clean()
		super(Cuenta, self).save()

class Especializacion(models.Model):
	''' Clase que representa una Especializacion Medica'''
	nombre = models.CharField(max_length=30)

class Medico (models.Model):
	''' Clase que representa un Medico '''
	cuenta = models.OneToOneField(Cuenta)
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	cedula = models.CharField(max_length=12, unique=True)
	genero = models.CharField(max_length=1, choices=GENERO)
	email = models.EmailField(max_length=254, unique=True)	
	telefono = models.CharField(validators=[MinLengthValidator(12)], max_length=12)
	especializaciones = models.ManyToManyField(Especializacion)
	
	def save(self):
		''' Sobreescribe el save() '''
		self.full_clean()
		super(Medico, self).save()

class MedicoTratante (models.Model):
	''' Clase que representa un Medico Tratante '''	
	medico = models.OneToOneField(Medico)

class Departamento (models.Model):
	''' Clase que representa un Departamento '''
	cuenta = models.OneToOneField(Cuenta)
	nombre = models.CharField(max_length=20, unique=True)
	email = models.EmailField(max_length=254, unique=True)	
	telefono = models.CharField(validators=[MinLengthValidator(12)], max_length=12)

	def save(self):
		''' Sobreescribe el save() '''
		self.full_clean()
		super(Departamento, self).save()	

class Quirofano(models.Model):
	''' Clase que representa un Quirofano '''
	numero = models.IntegerField(validators=[MinValueValidator(0)])
	area = models.CharField(max_length=3, choices=NOMBRE_AREA)

	def save(self):
		''' Sobreescribe el save() '''
		self.full_clean()
		super(Quirofano, self).save()

class MaterialQuirurgico(models.Model):
	''' Clase que representa un Material Quirurgico '''
	nombre = models.CharField(max_length=30)

class ServicioOperatorio(models.Model):
	''' Clase que representa un Servicio Operatorio '''
	nombre = models.CharField(max_length=30)

class EquipoEspecial(models.Model):
	''' Clase que representa un Equipo Especial '''
	nombre = models.CharField(max_length=30)

class TipoIntervencionQuirurgica(models.Model):
	''' Clase que representa un Tipo de Intervencion Quirurgica '''
	nombre = models.CharField(max_length=30)

class Paciente(models.Model):
	''' Clase que representa un Paciente '''
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	cedula = models.CharField(max_length=12, unique=True)
	fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
	telefono = models.CharField(validators=[MinLengthValidator(12)], max_length=12)
	genero = models.CharField(max_length=1,choices=GENERO)
	numero_expediente = models.CharField(max_length=5, unique=True, blank=True, null=True) # Ver formato 
	numero_habitacion = models.CharField(max_length=5, blank=True, null=True) # Ver formato
	numero_inscripcion_medico = models.CharField(max_length=5, unique=True, blank=True, null=True) # Ver formato 
	diagnostico_ingreso = models.TextField()
	servicios_operatorios_requeridos = models.ManyToManyField(ServicioOperatorio, blank=True, null=True)
	familiar_medico = models.ForeignKey(Medico, blank=True, null=True)
	parentezco_familiar_medico = models.CharField(max_length=1, choices=PARENTEZCO, blank=True, null=True)

	def save(self):
		''' Sobreescribe el save() '''
		self.full_clean()
		super(Paciente, self).save()

class IntervencionQuirurgica(models.Model):
	''' Clase que representa una Intervencion Quirurgica '''
	fecha_intervencion = models.DateField(auto_now=False, auto_now_add=False)
	hora_inicio = models.TimeField(auto_now=False, auto_now_add=False)
	hora_fin = models.TimeField(auto_now=False, auto_now_add=False)
	duracion = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
	estado = models.CharField(max_length=1, choices=ESTADO_INTERVENCION_QUIRURGICA)
	preferencia_anestesica = models.CharField(max_length=1, choices=TIPO_ANESTESIA)
	observaciones = models.TextField(blank=True, null=True)
	riesgo = models.CharField(max_length=1, choices=TIPO_RIESGO)
	razon_riesgo = models.TextField(blank=True, null=True)
	paciente = models.OneToOneField(Paciente)
	materiales_quirurgicos_requeridos = models.ManyToManyField(MaterialQuirurgico, blank=True, null=True)
	equipos_especiales_requeridos = models.ManyToManyField(EquipoEspecial, blank=True, null=True)
	tipo_intervencion = models.ForeignKey(TipoIntervencionQuirurgica)
	quirofano = models.ForeignKey(Quirofano)
	medicos_participantes = models.ManyToManyField(Medico, through='Participacion')

	def save(self):
		''' Sobreescribe el save(), validando los valores de self.riesgo y self.razon_riesgo, ademas de calcular la duracion de la Intervencion Quirurgica '''
		hora_inicio = time.strptime(self.hora_inicio, "%H:%M")
		hora_fin = time.strptime(self.hora_fin, "%H:%M")
		hora_inicio_seg = datetime.timedelta(hours = hora_inicio.tm_hour, minutes = hora_inicio.tm_min).total_seconds()
		hora_fin_seg = datetime.timedelta(hours = hora_fin.tm_hour, minutes = hora_fin.tm_min).total_seconds()
		diferencia_horas = float(hora_fin_seg) - float(hora_inicio_seg)
		self.duracion = diferencia_horas / 3600

		self.full_clean()

		if self.riesgo == 'M':
			if self.razon_riesgo == None:		
				raise ValidationError(u'La razón del riesgo no puede ser vacía si el riesgo es malo')
		else:
			if self.razon_riesgo != None:
				raise ValidationError(u'La razón del riesgo no debe existir si el riesgo no es malo')

		if self.hora_fin <= self.hora_inicio:
			raise ValidationError(u'La hora de fin debe ser mayor que la hora de inicio')
		
		super(IntervencionQuirurgica, self).save()

class Participacion(models.Model):
	''' Clase que representa la Participacion de un Medico en una
	Intervencion Quirurgica '''
	intervencion_quirurgica = models.ForeignKey(IntervencionQuirurgica)
	medico = models.ForeignKey(Medico)
	rol = models.CharField(max_length=1, choices=ROL_PARTICIPACION)

	def save(self):
		''' Sobreescribe el save() '''
		self.full_clean()
		super(Participacion, self).save()

class Reservacion (models.Model):
	''' Clase que representa una Reservacion de Intervencio Quirurgica '''
	fecha_reservacion = models.DateField(auto_now=True, auto_now_add=True)
	codigo = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(5)], default='00000')
	estado = models.CharField(max_length=1, choices=ESTADO_RESERVACION)
	tipo_solicitud = models.CharField(max_length=1, choices=TIPO_SOLICITUD_QUIROFANO)
	dias_hospitalizacion = models.IntegerField(validators=[MinValueValidator(0)])
	medico = models.ForeignKey(MedicoTratante)
	intervencion_quirurgica = models.OneToOneField(IntervencionQuirurgica)

	def save(self):
		''' Sobreescribe el save(), asignando un codigo de reservacion unico '''
		self.full_clean()

		super(Reservacion, self).save()

		hashids = Hashids(min_length=5, salt=uuid.uuid1().hex)
		self.codigo = hashids.encrypt(self.id)  
		super(Reservacion, self).save()	

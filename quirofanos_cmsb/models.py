from django.db import models
import datetime
import time

from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.core.exceptions import ValidationError


# Tipos de Privilegios
PRIVILEGIO = (
	('0','JEFE_PQ'),
	('1', 'COORDINADOR_PQ'),
	('2', 'ASISTENTE_PQ'),
	('3', 'MEDICO'),
	('4', 'OBSERVADOR'),
	)

# Estados de una Cuenta
ESTADO_CUENTA = (
	('P','Pendiente'),
	('A', 'Aprobada'),
	('R', 'Rechazada'),
	)

# Estados de una Reservacion
ESTADO_RESERVACION = (
	('P','Pendiente'),
	('A', 'Aprobada'),
	('R', 'Rechazada'),
	)

# Generos
GENERO = (
	('F', 'Femenino'),
	('M', 'Masculino'),
	)

# Tipos de Solicitud de Quirofano
TIPO_SOLICITUD_QUIROFANO = (
	('0', 'Emergencia'),
	('1', 'Electiva'),
	)

# Estados de una Intervencion Quirurgica
ESTADO_INTERVENCION_QUIRURGICA = (
	('0', 'En Espera'),
	('1', 'En Curso'),
	('2', 'En Recuperacion'),
	('3', 'En Habitacion'),
	)

# Tipos de Anestesia
TIPO_ANESTESIA = (
	('G', 'General'),
	('L', 'Local'),
	)

# Tipos de Riesgo
TIPO_RIESGO = (
	('B', 'Bueno'),
	('R', 'Regular'),
	('M', 'Malo'),
	)

# Nombres de Areas
NOMBRE_AREA = (
	('QG', 'Quirofano General'),
	('A', 'Ambulatorio'),
	('SP', 'Sala de Parto'),
	('SEE', 'Sala de Estudios Endoscopicos'),
	('SH', 'Sala de Hemodinamia'),
	('AS', 'Anestesia en Servicio')
	)

# Roles de medicos dentro de una Intervencion Quirurgica
ROL_PARTICIPACION = (
	('0', 'Anestesiologo'),
	('1', 'Primer Ayudante'),
	('2', 'Segundo Ayudante'),
	('3', 'Tercer Ayudante'),
	)

# Parentezco de Pacientes y Medicos
PARENTEZCO = (
	('0', 'Padre'),
	('1', 'Madre'),
	('2', 'Hijo(a)'),
	('3', 'Hermano(a)'),
	('4', 'Abuelo(a)'),
	('5', 'Nieto(a)'),
	('6', 'Tio(a)'),
	('7', 'Primo(a)'),
	('8', 'Esposo(a)'),
	('9', 'Sobrino(a)'),
	)

# Validaciones

def validate_razon_riesgo(value,riesgo):
    '''Validacion de razon de riesgo distinto de null cuando el
        riesgo es malo
            
        Parametros:
        value: Ya toma la razon de riesgo
        riesgo: Valor del attr riesgo
            
        Levanta un ValidationError si falla la validacion'''

    if riesgo == 'malo':
        if value == None:
            raise ValidationError(u'%s La razon no puede ser vacia si el riesgo es malo')


# Clases

class Cuenta (models.Model):
	''' Clase que representa una Cuenta de Usuario '''
	nombre_usuario = models.CharField(max_length=20, unique=True)
	contrasena = models.CharField(validators=[MinLengthValidator(64)], max_length=64 ) # Validar min_length
	estado = models.CharField(max_length=1, choices=ESTADO_CUENTA)
	privilegio = models.CharField(max_length=1, choices=PRIVILEGIO)
	fecha_creacion = models.DateField(auto_now=True, auto_now_add=True)

	def save(self):
		self.full_clean()
		super(Cuenta,self).save()


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
	telefono = models.CharField(validators = [MinLengthValidator(12)], max_length=12 )	# Validar min_length
	especializaciones = models.ManyToManyField(Especializacion)


class MedicoTratante (models.Model):
	''' Clase que representa un Medico Tratante '''	
	medico = models.OneToOneField(Medico)


class Departamento (models.Model):
	''' Clase que representa un Departamento '''
	cuenta = models.OneToOneField(Cuenta)
	nombre = models.CharField(max_length=20, unique=True)
	email = models.EmailField(max_length=254, unique=True)	
	telefono = models.CharField(validators = [MinLengthValidator(12)], max_length=12 )	# Validar min_length
	

class Quirofano(models.Model):
	''' Clase que representa un Quirofano '''
	nombre = models.IntegerField(validators = [MinValueValidator(0)] ) # Validacion mayor o igual que cero
	area = models.CharField(max_length=3, choices=NOMBRE_AREA)


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
	telefono = models.CharField(validators = [MinLengthValidator(12)], max_length=12 )	# Validar min_length
	genero = models.CharField(max_length=1,choices=GENERO)
	numero_expediente = models.IntegerField(max_length=5, blank=True, unique=True, null=True) # Ver formato 
	numero_habitacion = models.CharField(max_length=5, blank=True, null=True) # Ver formato
	numero_inscripcion_medico = models.CharField(max_length=10, blank=True, unique=True, null=True) # Ver formato
	diagnostico_ingreso = models.TextField()
	servicios_operatorios_requeridos = models.ManyToManyField(ServicioOperatorio, blank=True, null=True)
	familiar_medico = models.ForeignKey(Medico, blank=True, null=True)
	parentezco_familiar_medico = models.CharField(max_length=1, choices=PARENTEZCO, blank=True, null=True)


class IntervencionQuirurgica(models.Model):
	''' Clase que representa una Intervencion Quirurgica '''
	fecha_intervencion = models.DateField(auto_now=False, auto_now_add=False)
	hora_inicio = models.TimeField(auto_now=False, auto_now_add=False)
	hora_fin = models.TimeField(auto_now=False, auto_now_add=False) # Validacion mayor que hora_inicio
	duracion = models.DecimalField(max_digits=4, decimal_places=2)
	estado = models.CharField(max_length=1, choices=ESTADO_INTERVENCION_QUIRURGICA)
	preferencia_anestesica = models.CharField(max_length=1, choices=TIPO_ANESTESIA)
	observaciones = models.TextField(blank=True, null=True)
	riesgo = models.CharField(max_length=1, choices=TIPO_RIESGO)
	razon_riesgo = models.TextField(blank=True, null=True) #Validacion != null cuando riesgo es malo
	paciente = models.OneToOneField(Paciente)
	materiales_quirurgicos_requeridos = models.ManyToManyField(MaterialQuirurgico, blank=True, null=True)
	equipos_especiales_requeridos = models.ManyToManyField(EquipoEspecial, blank=True, null=True)
	tipo_intervencion = models.ForeignKey(TipoIntervencionQuirurgica)
	quirofano = models.ForeignKey(Quirofano)
	medicos_participantes = models.ManyToManyField(Medico, through='Participacion')


	'''def calcular_duracion(self):
		 Calcula la duracion de una Intervencion Quirurgica
		self.duracion = self.hora_fin - self.hora_inicio # Calcular'''
	def save(self):
		''' Calcula la duracion de una Intervencion Quirurgica '''
		hora_inicio = time.strptime(self.hora_inicio, "%H:%M")
		hora_fin = time.strptime(self.hora_fin, "%H:%M")
		hora_inicio_seg = datetime.timedelta(hours = hora_inicio.tm_hour, minutes = hora_inicio.tm_min).total_seconds()
		hora_fin_seg = datetime.timedelta(hours = hora_fin.tm_hour, minutes = hora_fin.tm_min).total_seconds()
		diferencia_horas = float(hora_fin_seg) - float(hora_inicio_seg)
		self.duracion = diferencia_horas / 3600

		super(IntervencionQuirurgica, self).save()

	

class Participacion(models.Model):
	''' Clase que representa la Participacion de un Medico en una
	Intervencion Quirurgica '''
	intervencion_quirurgica = models.ForeignKey(IntervencionQuirurgica)
	medico = models.ForeignKey(Medico)
	rol = models.CharField(max_length=1, choices=ROL_PARTICIPACION)


class Reservacion (models.Model):
	''' Clase que representa una Reservacion de Intervencio Quirurgica '''
	fecha_reservacion = models.DateField(auto_now=True, auto_now_add=True)
	codigo = models.CharField(max_length=5, unique=True) # Decidir generacion automatica  # Validar min_length
	estado = models.CharField(max_length=1, choices=ESTADO_RESERVACION)
	tipo_solicitud = models.CharField(max_length=1, choices=TIPO_SOLICITUD_QUIROFANO)
	dias_hospitalizacion = models.IntegerField(validators = [MinValueValidator(0)] ) # Validacion mayor o igual que cero
	medico = models.ForeignKey(MedicoTratante)
	intervencion_quirurgica = models.OneToOneField(IntervencionQuirurgica)

# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator, validate_slug
from django.contrib.auth.models import User

from quirofanos_cmsb.helpers.custom_validators import ExpresionRegular, MensajeError, CodigoError
from quirofanos_cmsb.models import Medico, Departamento
from quirofanos_cmsb.forms import BaseForm

# Nacionalidades
NACIONALIDAD = (
	('V-', u'Venezolano'),
	('E-', u'Extranjero'),
	)

class InicioSesionForm(BaseForm):
	''' Formulario de inicio de sesion '''
	nombre_usuario = forms.CharField(max_length=30)
	contrasena = forms.CharField(widget=forms.PasswordInput)

class BusquedaMedicoForm(BaseForm):
	''' Formulario de busqueda de medico por su numero de cedula '''
	nacionalidad_medico = forms.ChoiceField(widget=forms.HiddenInput, choices=NACIONALIDAD, initial='V-')
	cedula_medico = forms.CharField(max_length=12, validators=[RegexValidator(ExpresionRegular.CEDULA, MensajeError.CEDULA_INVALIDA, CodigoError.CEDULA_INVALIDA)])

	def clean(self):
		''' Sobreescribe el clean(), validando que la cedula realmente exista en la base de datos '''
		cleaned_data = super(BusquedaMedicoForm, self).clean()
		cedula_medico = cleaned_data.get('cedula_medico')
		nacionalidad_medico = cleaned_data.get('nacionalidad_medico')
		if cedula_medico and nacionalidad_medico:
			cedula_medico_bd = nacionalidad_medico + cedula_medico
			medico = Medico.objects.filter(cedula=cedula_medico_bd)
			if not medico:
				self._errors["cedula_medico"] = self.error_class([MensajeError.CEDULA_BD_NO_EXISTE])
				del cleaned_data["cedula_medico"]
			else:
				medico = medico[0]
				if medico.cuenta:
					if medico.cuenta.estado in ('A', 'P'):
						self._errors["cedula_medico"] = self.error_class([MensajeError.EXISTE_CUENTA])
						del cleaned_data["cedula_medico"]

		return cleaned_data

class BusquedaDepartamentoForm(BaseForm):
	''' Formulario de busqueda de Departamento por nombre '''
	c = Departamento.objects.all().count()
	d = Departamento.objects.exclude(cuenta=None).exclude(cuenta__estado='R').count()
	if c != d:
		nombre_departamento = forms.ModelChoiceField(queryset=Departamento.objects.exclude(cuenta__estado='A').exclude(cuenta__estado='P'))
	else:
		nombre_departamento = None

class RegistroMedicoForm(BaseForm):
	''' Formulario de solicitud registro de medico '''
	cedula_medico = forms.CharField(widget=forms.HiddenInput, required=False)
	nombre_usuario_medico = forms.CharField(max_length=30, validators=[validate_slug])

	def clean_nombre_usuario_medico(self):
		''' Sobreescribe el clean_nombre_usuario_medico(), validando que el nombre de usuario ingresado sea unico '''
		nombre_usuario_medico = self.cleaned_data['nombre_usuario_medico']
		usuario = User.objects.filter(username=nombre_usuario_medico)
		if usuario:
			raise forms.ValidationError(MensajeError.EXISTE_USUARIO, code=CodigoError.EXISTE_USUARIO)
		return nombre_usuario_medico

class RegistroDepartamentoForm(BaseForm):
	''' Formulario de solicitud de registro de departamento '''
	nombre_departamento = forms.CharField(widget=forms.HiddenInput, required=False)
	nombre_usuario_departamento = forms.CharField(max_length=30, validators=[validate_slug])

	def clean_nombre_usuario_departamento(self):
		''' Sobreescribe el clean_nombre_usuario_departamento(), validando que el nombre de usuario ingresado sea unico '''
		nombre_usuario_departamento = self.cleaned_data['nombre_usuario_departamento']
		usuario = User.objects.filter(username=nombre_usuario_departamento)
		if usuario:
			raise forms.ValidationError(MensajeError.EXISTE_USUARIO, code=CodigoError.EXISTE_USUARIO)
		return nombre_usuario_departamento

class CambiarContrasenaForm(BaseForm):
	''' Formulario de cambio de contrasena '''
	contrasena_actual = forms.CharField(widget=forms.PasswordInput)
	contrasena_nueva = forms.CharField(widget=forms.PasswordInput)
	contrasena_confirmacion = forms.CharField(widget=forms.PasswordInput)


	def clean(self):
		''' Sobreescribe el clean(), validando que las contrasenas ingresadas coincidan '''
		cleaned_data = super(CambiarContrasenaForm, self).clean()

		# Validar que las contrasenas ingresadas coincidan
		contrasena_nueva = cleaned_data.get("contrasena_nueva")
		contrasena_confirmacion = cleaned_data.get("contrasena_confirmacion")
		if contrasena_nueva and contrasena_confirmacion:
			if contrasena_nueva != contrasena_confirmacion:
				raise forms.ValidationError(MensajeError.CONTRASENAS_NO_COINCIDEN, code=CodigoError.CONTRASENAS_NO_COINCIDEN)

		return cleaned_data


class RecuperarContrasenaForm(BaseForm):
	''' Formulario de recuperar contrasena '''
	nombre_usuario = forms.CharField(max_length=30, validators=[validate_slug])

class ActualizarEmailForm(BaseForm):
	''' Formulario de actualizacion de email  '''
	correo_electronico = forms.EmailField(max_length=75)

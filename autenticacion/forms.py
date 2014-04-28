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

	def clean_cedula_medico(self):
		''' Sobreescribe el clean_cedula_medico(), validando que la cedula realmente exista en la base de datos '''
		cedula_medico = self.cleaned_data['cedula_medico']
		cedula_medico_bd = self.cleaned_data['nacionalidad_medico'] + cedula_medico
		medico = Medico.objects.filter(cedula=cedula_medico_bd)
		if not medico:
			raise forms.ValidationError(MensajeError.CEDULA_BD_NO_EXISTE, CodigoError.CEDULA_BD_NO_EXISTE)

		medico = medico[0]
		if medico.cuenta:
			raise forms.ValidationError(MensajeError.EXISTE_CUENTA, CodigoError.EXISTE_CUENTA)
		return cedula_medico

class BusquedaDepartamentoForm(BaseForm):
	''' Formulario de busqueda de Departamento por nombre '''
	nombre_departamento = forms.ModelChoiceField(queryset=Departamento.objects.filter(cuenta=None))

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
	correo_electronico = forms.EmailField(max_length=75)

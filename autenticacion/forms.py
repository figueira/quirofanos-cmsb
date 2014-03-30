# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator, validate_slug
from django.contrib.auth.models import User

from quirofanos_cmsb.helpers.custom_validators import ExpresionRegular, MensajeError, CodigoError
from quirofanos_cmsb.models import Especializacion, Medico

# Generos
GENERO = (
	('F', u'Femenino'),
	('M', u'Masculino'),
	)

# Nacionalidades
NACIONALIDAD = (
	('V-', u'Venezolano'),
	('E-', u'Extranjero'),
	)

class InicioSesionForm(forms.Form):
	''' Formulario de inicio de sesion '''
	nombre_usuario = forms.CharField(max_length=30)
	contrasena = forms.CharField(widget=forms.PasswordInput)

class RegistroDepartamentoForm(forms.Form):
	''' Formulario de registro de Departamento '''
	nombre_departamento = forms.CharField(max_length=20, validators=[RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.NOMBRE_GENERAL_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])
	codigo_telefono = forms.CharField(validators=[RegexValidator(ExpresionRegular.CODIGO_TELEFONO, MensajeError.CODIGO_TELEFONO_INVALIDO, CodigoError.CODIGO_TELEFONO_INVALIDO)])
	telefono_departamento = forms.CharField(validators=[RegexValidator(ExpresionRegular.NUMERO_TELEFONO, MensajeError.NUMERO_TELEFONO_INVALIDO, CodigoError.NUMERO_TELEFONO_INVALIDO)])
	email_departamento = forms.EmailField(max_length=75)
	nombre_usuario_departamento = forms.CharField(max_length=30, validators=[validate_slug])
	contrasena_departamento = forms.CharField(widget=forms.PasswordInput)
	contrasena_confirmacion = forms.CharField(widget=forms.PasswordInput)

	def clean_nombre_usuario_departamento(self):
		''' Sobreescribe el clean_nombre_usuario_departamento(), validando que el nombre de usuario ingresado sea unico '''
		nombre_usuario_departamento = self.cleaned_data['nombre_usuario_departamento']
		for usuario in User.objects.all():
			if usuario.username == nombre_usuario_departamento:
				raise forms.ValidationError(MensajeError.EXISTE_USUARIO, code=CodigoError.EXISTE_USUARIO)
		return nombre_usuario_departamento

	def clean(self):
		''' Sobreescribe el clean(), validando que las contrasenas ingresadas coincidan '''
		cleaned_data = super(RegistroDepartamentoForm, self).clean()
		contrasena_departamento = cleaned_data.get("contrasena_departamento")
		contrasena_confirmacion = cleaned_data.get("contrasena_confirmacion")
		if contrasena_departamento and contrasena_confirmacion:
			if contrasena_departamento != contrasena_confirmacion:
				raise forms.ValidationError(MensajeError.CONTRASENAS_NO_COINCIDEN, code=CodigoError.CONTRASENAS_NO_COINCIDEN)
		return cleaned_data

class RegistroMedicoForm(forms.Form):
	''' Formulario de registro de Medico '''
	nombre_medico = forms.CharField(max_length=20, validators=[RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.NOMBRE_GENERAL_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])
	apellido_medico = forms.CharField(max_length=20, validators=[RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.APELLIDO_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])
	nacionalidad_medico = forms.ChoiceField(widget=forms.HiddenInput, choices=NACIONALIDAD, initial='V-')
	cedula_medico = forms.CharField(max_length=12, validators=[RegexValidator(ExpresionRegular.CEDULA, MensajeError.CEDULA_INVALIDA, CodigoError.CEDULA_INVALIDA)])
	especialidad_medico = forms.ModelMultipleChoiceField(queryset=Especializacion.objects.all())
	genero_medico = forms.ChoiceField(widget=forms.RadioSelect, choices=GENERO)
	codigo_telefono = forms.CharField(validators=[RegexValidator(ExpresionRegular.CODIGO_TELEFONO, MensajeError.CODIGO_TELEFONO_INVALIDO, CodigoError.CODIGO_TELEFONO_INVALIDO)])
	telefono_medico = forms.CharField(validators=[RegexValidator(ExpresionRegular.NUMERO_TELEFONO, MensajeError.NUMERO_TELEFONO_INVALIDO, CodigoError.NUMERO_TELEFONO_INVALIDO)])
	email_medico = forms.EmailField(max_length=75)
	nombre_usuario_medico = forms.CharField(max_length=30, validators=[validate_slug])
	contrasena_medico = forms.CharField(widget=forms.PasswordInput)
	contrasena_confirmacion = forms.CharField(widget=forms.PasswordInput)

	def clean_nombre_usuario_medico(self):
		''' Sobreescribe el clean_nombre_usuario_medico(), validando que el nombre de usuario ingresado sea unico '''
		nombre_usuario_medico = self.cleaned_data['nombre_usuario_medico']
		for usuario in User.objects.all():
			if usuario.username == nombre_usuario_medico:
				raise forms.ValidationError(MensajeError.EXISTE_USUARIO, code=CodigoError.EXISTE_USUARIO)
		return nombre_usuario_medico

	def clean(self):
		''' Sobreescribe el clean(), validando que las contrasenas ingresadas coincidan '''
		cleaned_data = super(RegistroMedicoForm, self).clean()

		# Validar que las contrasenas ingresadas coincidan
		contrasena_medico = cleaned_data.get("contrasena_medico")
		contrasena_confirmacion = cleaned_data.get("contrasena_confirmacion")
		if contrasena_medico and contrasena_confirmacion:
			if contrasena_medico != contrasena_confirmacion:
				raise forms.ValidationError(MensajeError.CONTRASENAS_NO_COINCIDEN, code=CodigoError.CONTRASENAS_NO_COINCIDEN)
		return cleaned_data

class CambiarContrasenaForm(forms.Form):
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


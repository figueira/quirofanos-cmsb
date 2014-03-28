# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator, validate_slug

from quirofanos_cmsb.helpers.custom_validators import ExpresionRegular, MensajeError, CodigoError


class InicioSesionForm(forms.Form):

	''' Formulario de inicio de sesion '''
    nombre_usuario = forms.CharField(max_length=30, validators=[validate_slug])
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

	def clean(self):
		''' Sobreescribe el clean(), validando que las contrasenas ingresadas coincidan '''
		cleaned_data = super(ContactForm, self).clean()
        contrasena_departamento = cleaned_data.get("contrasena_departamento")
        contrasena_confirmacion = cleaned_data.get("contrasena_confirmacion")
        if contrasena_departamento and contrasena_confirmacion:
        	if contrasena_departamento != contrasena_confirmacion:
        		raise forms.ValidationError(MensajeError.CONTRASENAS_NO_COINCIDEN, code=CodigoError.CONTRASENAS_NO_COINCIDEN)

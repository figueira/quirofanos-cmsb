# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator, validate_slug

from quirofanos_cmsb.helpers.custom_validators import ExpresionRegular, MensajeError, CodigoError


from quirofanos_cmsb.models import Especializacion

# Generos
GENERO = (
	('F', u'Femenino'),
	('M', u'Masculino'),
	)

class InicioSesionForm(forms.Form):

	''' Formulario de inicio de sesion '''
    nombre_usuario = forms.CharField(max_length=30, validators=[validate_slug])
    contrasena = forms.CharField(widget=forms.PasswordInput)

class RegistroDepartamentoForm(forms.Form):
	
	''' Formulario de registro de Departamento '''
	nombre_departamento = forms.CharField(max_length=20)
	codigo_telefono = forms.CharField(max_length=4, min_length=4, validators=[RegexValidator(ExpresionRegular.CODIGO_TELEFONO, MensajeError.CODIGO_TELEFONO_INVALIDO, CodigoError.CODIGO_TELEFONO_INVALIDO)])
	telefono_departamento = forms.CharField(max_length=7, min_length=7, validators=[RegexValidator(ExpresionRegular.NUMERO_TELEFONO, MensajeError.NUMERO_TELEFONO_INVALIDO, CodigoError.NUMERO_TELEFONO_INVALIDO)])
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
        		raise forms.ValidationError(u'Las contraseñas ingresadas no coinciden.')


class RegistroMedicoForm(forms.Form):
	nombre_medico = forms.CharField(max_length=20)
	apellido_medico = forms.CharField(max_length=20)
	cedula_medico = forms.CharField(max_length=12)
	especialidad_medico = forms.ModelMultipleChoiceField(queryset=Especializacion.objects.all())
	genero_medico = forms.ChoiceField(widget=forms.RadioSelect, choices=GENERO)
	codigo_telefono = forms.CharField(max_length=4, min_length=4)    
	telefono_medico = forms.CharField(max_length=7, min_length=7)
	email_medico = forms.EmailField(max_length=75)
	nombre_usuario_medico = forms.CharField(max_length=30)
	contrasena_medico = forms.CharField(widget=forms.PasswordInput)
	contrasena_confirmacion = forms.CharField(widget=forms.PasswordInput)
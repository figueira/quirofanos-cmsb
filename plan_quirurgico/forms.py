# -*- coding: utf-8 -*-
from django import forms

from quirofanos_cmsb.helpers.custom_validators import MensajeError, CodigoError

from quirofanos_cmsb.forms import BaseForm

class DuracionIntervencionQuirurgicaForm(BaseForm):
    ''' Formulario de ingreso de la duracion de una intervencion quirurgica para buscar horarios disponibles '''
    horas = forms.IntegerField(min_value=1, max_value=12, initial=1)
    minutos = forms.IntegerField(min_value=0, max_value=59, initial=0)

class CambiarContrasenaForm(BaseForm):
    ''' Formulario de actualizacion de contrasena '''
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

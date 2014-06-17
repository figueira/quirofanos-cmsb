# -*- coding: utf-8 -*-
from django import forms

from quirofanos_cmsb.forms import BaseForm

class MensajeForm(BaseForm):
	''' Formulario para hacer el 'render' en ver detalle 
		de mis mensajes '''
	titulo = forms.CharField(max_length=60)
	texto = forms.CharField(widget=forms.Textarea)
	fecha_mensaje = forms.DateTimeField(required=False)
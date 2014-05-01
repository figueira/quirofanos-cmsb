# -*- coding: utf-8 -*-
from django import forms

from quirofanos_cmsb.forms import BaseForm

class DuracionIntervencionQuirurgicaForm(BaseForm):
    ''' Formulario de ingreso de la duracion de una intervencion quirurgica para buscar horarios disponibles '''
    horas = forms.IntegerField(min_value=1, max_value=12, initial=1)
    minutos = forms.IntegerField(min_value=0, max_value=59, initial=0)

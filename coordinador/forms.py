# -*- coding: utf-8 -*-
from django import forms

from quirofanos_cmsb.forms import BaseForm


class GestionarSolicitudQuirofanoForm(BaseForm):
    ''' Formulario para la gestion de una solicitud de quirofano'''
    id_reservacion = forms.CharField(widget=forms.HiddenInput)

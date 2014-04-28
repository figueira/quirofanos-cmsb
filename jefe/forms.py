# -*- coding: utf-8 -*-
from django import forms

from quirofanos_cmsb.forms import BaseForm


class GestionarSolicitudUsuarioForm(BaseForm):
    ''' Formulario para la gestion de una solicitud de usuario'''
    id_cuenta = forms.CharField(widget=forms.HiddenInput)

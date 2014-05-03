# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator

from quirofanos_cmsb.forms import BaseForm
from quirofanos_cmsb.helpers.custom_validators import ExpresionRegular, MensajeError, CodigoError
from quirofanos_cmsb.models import GENERO, CompaniaAseguradora, AREA_INGRESO, ServicioOperatorio, TIPO_ANESTESIA, TIPO_RIESGO, MaterialQuirurgico, EquipoEspecial, Medico

class SolicitudQuirofanoForm(BaseForm):
    ''' Formulario de solicitud de quirofano '''
    # Paciente
    nombre_paciente = forms.CharField(max_length=50, validators=[
                              RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.NOMBRE_GENERAL_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])
    apellido_paciente = forms.CharField(max_length=50, validators=[
                              RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.NOMBRE_GENERAL_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])
    cedula_paciente = forms.CharField(max_length=12, validators=[
                              RegexValidator(ExpresionRegular.CEDULA_BD, MensajeError.CEDULA_BD_INVALIDA, CodigoError.CEDULA_BD_INVALIDA)])
    fecha_nacimiento_paciente = forms.DateField(input_formats=["%d/%m/%Y"])
    codigo_telefono_paciente = forms.CharField(validators=[RegexValidator(ExpresionRegular.CODIGO_TELEFONO, MensajeError.CODIGO_TELEFONO_INVALIDO, CodigoError.CODIGO_TELEFONO_INVALIDO)])
    numero_telefono_paciente = forms.CharField(validators=[RegexValidator(ExpresionRegular.NUMERO_TELEFONO, MensajeError.NUMERO_TELEFONO_INVALIDO, CodigoError.NUMERO_TELEFONO_INVALIDO)])
    genero_paciente = forms.ChoiceField(choices=GENERO, widget=forms.RadioSelect)
    compania_aseguradora_paciente = forms.ModelChoiceField(queryset=CompaniaAseguradora.objects.all(), required=False)
    area_ingreso_paciente = forms.ChoiceField(choices=AREA_INGRESO, required=False)
    numero_expediente_paciente = forms.CharField(validators=[RegexValidator(ExpresionRegular.NUMERO_EXPEDIENTE, MensajeError.NUMERO_EXPEDIENTE_INVALIDO, CodigoError.NUMERO_EXPEDIENTE_INVALIDO)], required=False)
    numero_habitacion_paciente = forms.CharField(validators=[RegexValidator(ExpresionRegular.NUMERO_HABITACION, MensajeError.NUMERO_HABITACION_INVALIDO, CodigoError.NUMERO_HABITACION_INVALIDO)], required=False)
    diagnostico_ingreso_paciente = forms.CharField(widget=forms.Textarea)
    servicios_operatorios_paciente = forms.ModelChoiceField(queryset=ServicioOperatorio.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    # Intervencion Quirurgica
    preferencia_anestesica = forms.ChoiceField(choices=TIPO_ANESTESIA, widget=forms.RadioSelect)
    observaciones = forms.CharField(widget=forms.Textarea, required=False)
    riesgo = forms.ChoiceField(choices=TIPO_RIESGO, widget=forms.RadioSelect)
    razon_riesgo = forms.CharField(widget=forms.Textarea, required=False)
    materiales_quirurgicos_requeridos = forms.ModelChoiceField(queryset=MaterialQuirurgico.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    equipos_especiales_requeridos = forms.ModelChoiceField(queryset=EquipoEspecial.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    dias_hospitalizacion = forms.IntegerField(min_value=0)

class ProcedimientoQuirurgicoForm(BaseForm):
    ''' Formulario para agregar un procedimiento quirurgico a una solicitud de quirofano '''
    id_organo_corporal = forms.IntegerField(min_value=1, required=False)
    id_tipo_procedimiento_quirurgico = forms.IntegerField(min_value=1, required=False)
    monto_honorarios_cirujano_principal = forms.DecimalField(max_digits=15, decimal_places=2)
    anestesiologo = forms.ModelChoiceField(queryset=Medico.objects.all())
    primer_ayudante = forms.ModelChoiceField(queryset=Medico.objects.all())
    segundo_ayudante = forms.ModelChoiceField(queryset=Medico.objects.all())
    tercer_ayudante = forms.ModelChoiceField(queryset=Medico.objects.all())
    monto_honorarios_tercer_ayudante = forms.DecimalField(max_digits=15, decimal_places=2, required=False)







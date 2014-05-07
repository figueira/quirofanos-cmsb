# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator
from django.forms import extras

from quirofanos_cmsb.forms import BaseForm
from quirofanos_cmsb.helpers.custom_validators import ExpresionRegular, MensajeError, CodigoError
from quirofanos_cmsb.models import GENERO, CompaniaAseguradora, AREA_INGRESO, ServicioOperatorio, TIPO_ANESTESIA, TIPO_RIESGO, MaterialQuirurgico, EquipoEspecial, Medico
from autenticacion.forms import NACIONALIDAD

TIPO_PAGO = (
    ("P", "Particular"),
    ("S", "Seguro"),
    )

class SolicitudQuirofanoForm(BaseForm):
    ''' Formulario de solicitud de quirofano '''
    # Paciente
    nombre_paciente = forms.CharField(max_length=50, validators=[
                              RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.NOMBRE_GENERAL_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])
    apellido_paciente = forms.CharField(max_length=50, validators=[
                              RegexValidator(ExpresionRegular.NOMBRE_GENERAL, MensajeError.NOMBRE_GENERAL_INVALIDO, CodigoError.NOMBRE_GENERAL_INVALIDO)])
    nacionalidad_paciente = forms.ChoiceField(widget=forms.HiddenInput, choices=NACIONALIDAD, initial='V-')
    cedula_paciente = forms.CharField(max_length=12, validators=[
                              RegexValidator(ExpresionRegular.CEDULA, MensajeError.CEDULA_INVALIDA, CodigoError.CEDULA_INVALIDA)])
    fecha_nacimiento_paciente = forms.DateField(input_formats=['%d/%m/%Y', '%m/%d/%Y', '%Y-%m-%d'])
    codigo_telefono_paciente = forms.CharField(validators=[RegexValidator(ExpresionRegular.CODIGO_TELEFONO, MensajeError.CODIGO_TELEFONO_INVALIDO, CodigoError.CODIGO_TELEFONO_INVALIDO)])
    numero_telefono_paciente = forms.CharField(validators=[RegexValidator(ExpresionRegular.NUMERO_TELEFONO, MensajeError.NUMERO_TELEFONO_INVALIDO, CodigoError.NUMERO_TELEFONO_INVALIDO)])
    genero_paciente = forms.ChoiceField(choices=GENERO, widget=forms.RadioSelect)
    tipo_pago_paciente = forms.ChoiceField(choices=TIPO_PAGO, widget=forms.RadioSelect)
    compania_aseguradora_paciente = forms.ModelChoiceField(queryset=CompaniaAseguradora.objects.all(), required=False)
    paciente_con_expediente = forms.BooleanField(required=False)
    area_ingreso_paciente = forms.ChoiceField(choices=AREA_INGRESO, required=False)
    numero_expediente_paciente = forms.CharField(validators=[RegexValidator(ExpresionRegular.NUMERO_EXPEDIENTE, MensajeError.NUMERO_EXPEDIENTE_INVALIDO, CodigoError.NUMERO_EXPEDIENTE_INVALIDO)], required=False)
    paciente_hospitalizado = forms.BooleanField(required=False)
    numero_habitacion_paciente = forms.CharField(validators=[RegexValidator(ExpresionRegular.NUMERO_HABITACION, MensajeError.NUMERO_HABITACION_INVALIDO, CodigoError.NUMERO_HABITACION_INVALIDO)], required=False)
    diagnostico_ingreso_paciente = forms.CharField(widget=forms.Textarea)
    servicios_operatorios_paciente = forms.ModelMultipleChoiceField(queryset=ServicioOperatorio.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    # Intervencion Quirurgica
    preferencia_anestesica = forms.ChoiceField(choices=TIPO_ANESTESIA, widget=forms.RadioSelect)
    observaciones = forms.CharField(widget=forms.Textarea, required=False)
    riesgo = forms.ChoiceField(choices=TIPO_RIESGO, widget=forms.RadioSelect)
    razon_riesgo = forms.CharField(widget=forms.Textarea, required=False)
    materiales_quirurgicos_requeridos = forms.ModelMultipleChoiceField(queryset=MaterialQuirurgico.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    equipos_especiales_requeridos = forms.ModelMultipleChoiceField(queryset=EquipoEspecial.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    dias_hospitalizacion = forms.IntegerField(min_value=0)

    def clean(self):
        ''' Sobreescribe el clean(), asegurandose de que si este campo es True se debe haber indicado numero de expediente. Ademas, asegurandose de que si este campo es True se debe haber indicado el numero de habitacion. Ademas, asegurandose de que si el riesgo es malo entonces debe haberse indicado la razon del riesgo. '''
        cleaned_data = super(SolicitudQuirofanoForm, self).clean()
        paciente_con_expediente = cleaned_data.get("paciente_con_expediente")
        numero_expediente_paciente = cleaned_data.get("numero_expediente_paciente")
        if paciente_con_expediente and numero_expediente_paciente == "":
            self._errors["numero_expediente_paciente"] = self.error_class([MensajeError.PACIENTE_CON_EXPEDIENTE_SIN_ESPECIFICACION])
            del cleaned_data["numero_expediente_paciente"]

        paciente_hospitalizado = cleaned_data.get("paciente_hospitalizado")
        numero_habitacion_paciente = cleaned_data.get("numero_habitacion_paciente")
        if paciente_hospitalizado and numero_habitacion_paciente == "":
            self._errors["numero_habitacion_paciente"] = self.error_class([MensajeError.PACIENTE_HOSPITALIZADO_SIN_HABITACION])
            del cleaned_data["numero_habitacion_paciente"]

        riesgo = cleaned_data.get("riesgo")
        razon_riesgo = cleaned_data.get("razon_riesgo")
        if riesgo and riesgo == "M" and razon_riesgo == "":
            self._errors["razon_riesgo"] = self.error_class([MensajeError.RIESGO_MALO_SIN_RAZON])
            del cleaned_data["razon_riesgo"]

        return cleaned_data

class ProcedimientoQuirurgicoForm(BaseForm):
    ''' Formulario para agregar un procedimiento quirurgico a una solicitud de quirofano '''
    id_organo_corporal = forms.IntegerField(min_value=1, widget=forms.HiddenInput, required=False)
    id_tipo_procedimiento_quirurgico = forms.IntegerField(min_value=1, widget=forms.HiddenInput, required=False)
    monto_honorarios_cirujano_principal = forms.DecimalField(min_value=0.00, max_digits=15, decimal_places=2)
    anestesiologo = forms.ModelChoiceField(queryset=Medico.objects.all())
    primer_ayudante = forms.ModelChoiceField(queryset=Medico.objects.all())
    segundo_ayudante = forms.ModelChoiceField(queryset=Medico.objects.all())
    tercer_ayudante = forms.ModelChoiceField(queryset=Medico.objects.all())
    monto_honorarios_tercer_ayudante = forms.DecimalField(min_value=0.00, max_digits=15, decimal_places=2, required=False)

class EliminarProcedimientoQuirurgicoForm(BaseForm):
    ''' Formulario para eliminar un procedimiento quirurgico durante el proceso de solicitud de quirofano '''
    id_procedimiento_quirurgico = forms.IntegerField(min_value=1, widget=forms.HiddenInput, required=False)







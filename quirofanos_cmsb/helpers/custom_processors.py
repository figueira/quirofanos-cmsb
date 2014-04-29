# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _

from quirofanos_cmsb.helpers.template_text import TextoMostrable

def constantes_texto(request):
    datos = {}
    datos['NO_POSEE'] = TextoMostrable.NO_POSEE
    datos['ULTIMA_SEMANA'] = TextoMostrable.ULTIMA_SEMANA
    datos['ULTIMO_MES'] = TextoMostrable.ULTIMO_MES
    datos['ULTIMOS_TRES_MESES'] = TextoMostrable.ULTIMOS_TRES_MESES
    datos['PENDIENTES'] = TextoMostrable.PENDIENTES
    datos['APROBADAS'] = TextoMostrable.APROBADAS
    datos['RECHAZADAS'] = TextoMostrable.RECHAZADAS
    datos['VOLVER'] = TextoMostrable.VOLVER
    datos['BUSCAR'] = TextoMostrable.BUSCAR
    datos['ENVIAR'] = TextoMostrable.ENVIAR
    datos['ACEPTAR'] = TextoMostrable.ACEPTAR
    datos['CANCELAR'] = TextoMostrable.CANCELAR
    datos['LABEL_NOMBRE'] = TextoMostrable.LABEL_NOMBRE
    datos['LABEL_APELLIDO'] = TextoMostrable.LABEL_APELLIDO
    datos['LABEL_CEDULA'] = TextoMostrable.LABEL_CEDULA
    datos['LABEL_GENERO'] = TextoMostrable.LABEL_GENERO
    datos['LABEL_TELEFONO'] = TextoMostrable.LABEL_TELEFONO
    datos['LABEL_EMAIL'] = TextoMostrable.LABEL_EMAIL
    datos['LABEL_NOMBRE_USUARIO'] = TextoMostrable.LABEL_NOMBRE_USUARIO
    datos['LABEL_ESPECIALIZACION'] = TextoMostrable.LABEL_ESPECIALIZACION
    datos['LABEL_ESPECIALIZACION_ABREVIADO'] = TextoMostrable.LABEL_ESPECIALIZACION_ABREVIADO
    datos['LABEL_DEPARTAMENTO'] = TextoMostrable.LABEL_DEPARTAMENTO
    datos['LABEL_DEPARTAMENTO_ABREVIADO'] = TextoMostrable.LABEL_DEPARTAMENTO_ABREVIADO
    datos['LABEL_FECHA_SOLICITUD'] = TextoMostrable.LABEL_FECHA_SOLICITUD
    datos['LABEL_TIPO_USUARIO'] = TextoMostrable.LABEL_TIPO_USUARIO
    datos['RECHAZAR_SOLICITUD'] = TextoMostrable.RECHAZAR_SOLICITUD
    datos['APROBAR_SOLICITUD'] = TextoMostrable.APROBAR_SOLICITUD
    datos['LABEL_INTERVENCION_PLURAL'] = TextoMostrable.LABEL_INTERVENCION_PLURAL
    datos['LABEL_INTERVENCION_ABREVIADO'] = TextoMostrable.LABEL_INTERVENCION_ABREVIADO
    datos['LABEL_QUIRURGICA_PLURAL'] = TextoMostrable.LABEL_QUIRURGICA_PLURAL
    datos['DISPONIBLE'] = TextoMostrable.DISPONIBLE
    datos['NO_DISPONIBLE'] = TextoMostrable.NO_DISPONIBLE
    datos['LABEL_PACIENTE'] = TextoMostrable.LABEL_PACIENTE
    datos['LABEL_INTERVENCION'] = TextoMostrable.LABEL_INTERVENCION
    datos['LABEL_QUIRURGICA'] = TextoMostrable.LABEL_QUIRURGICA
    datos['LABEL_MEDICO'] = TextoMostrable.LABEL_MEDICO
    datos['SOLICITAR_QUIROFANO'] = TextoMostrable.SOLICITAR_QUIROFANO
    datos['LABEL_HORAS'] = TextoMostrable.LABEL_HORAS
    datos['LABEL_MINUTOS'] = TextoMostrable.LABEL_MINUTOS
    datos['HORAS'] = TextoMostrable.HORAS
    datos['MINUTOS'] = TextoMostrable.MINUTOS
    datos['MENSAJE_SELECCIONAR_TURNO_INTERVENCION'] = TextoMostrable.MENSAJE_SELECCIONAR_TURNO_INTERVENCION
    datos['LABEL_DURACION_INTERVENCION'] = TextoMostrable.LABEL_DURACION_INTERVENCION
    return datos

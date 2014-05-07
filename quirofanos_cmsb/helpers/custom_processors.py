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
    datos['SELECCIONAR_TURNO'] = TextoMostrable.SELECCIONAR_TURNO
    datos['LABEL_AREA'] = TextoMostrable.LABEL_AREA
    datos['LABEL_QUIROFANO'] = TextoMostrable.LABEL_QUIROFANO
    datos['LABEL_FECHA'] = TextoMostrable.LABEL_FECHA
    datos['LABEL_HORA_INICIO'] = TextoMostrable.LABEL_HORA_INICIO
    datos['LABEL_HORA_FIN'] = TextoMostrable.LABEL_HORA_FIN
    datos['LABEL_ANESTESIA'] = TextoMostrable.LABEL_ANESTESIA
    datos['LABEL_OBSERVACIONES'] = TextoMostrable.LABEL_OBSERVACIONES
    datos['LABEL_NIVEL_RIESGO'] = TextoMostrable.LABEL_NIVEL_RIESGO
    datos['LABEL_EQUIPOS_ESPECIALES'] = TextoMostrable.LABEL_EQUIPOS_ESPECIALES
    datos['LABEL_MATERIAL_QUIRURGICO'] = TextoMostrable.LABEL_MATERIAL_QUIRURGICO
    datos['LABEL_FECHA_NACIMIENTO'] = TextoMostrable.LABEL_FECHA_NACIMIENTO
    datos['LABEL_DIAGNOSTICO'] = TextoMostrable.LABEL_DIAGNOSTICO
    datos['LABEL_FORMA_PAGO'] = TextoMostrable.LABEL_FORMA_PAGO
    datos['LABEL_ASEGURADORA'] = TextoMostrable.LABEL_ASEGURADORA
    datos['LABEL_HABITACION'] = TextoMostrable.LABEL_HABITACION
    datos['LABEL_PACIENTE_HOSPITALIZADO'] = TextoMostrable.LABEL_PACIENTE_HOSPITALIZADO
    datos['PACIENTE'] = TextoMostrable.PACIENTE
    datos['LABEL_CODIGO_TELEFONO'] = TextoMostrable.LABEL_CODIGO_TELEFONO
    datos['LABEL_NUMERO_TELEFONO'] = TextoMostrable.LABEL_NUMERO_TELEFONO
    datos['QUIROFANO'] = TextoMostrable.QUIROFANO
    datos['LABEL_RAZON_RIESGO'] = TextoMostrable.LABEL_RAZON_RIESGO
    datos['LABEL_ANESTESIOLOGO'] = TextoMostrable.LABEL_ANESTESIOLOGO
    datos['LABEL_ANESTESIOLOGO_ABREVIADO'] = TextoMostrable.LABEL_ANESTESIOLOGO_ABREVIADO
    datos['LABEL_BOLIVARES'] = TextoMostrable.LABEL_BOLIVARES
    datos['LABEL_PRIMER_AYUDANTE'] = TextoMostrable.LABEL_PRIMER_AYUDANTE
    datos['LABEL_SEGUNDO_AYUDANTE'] = TextoMostrable.LABEL_SEGUNDO_AYUDANTE
    datos['LABEL_TERCER_AYUDANTE'] = TextoMostrable.LABEL_TERCER_AYUDANTE
    datos['LABEL_CIRUJANO_PRINCIPAL'] = TextoMostrable.LABEL_CIRUJANO_PRINCIPAL
    datos['LABEL_HONORARIOS'] = TextoMostrable.LABEL_HONORARIOS
    datos['LABEL_SERVICIOS_OPERATORIOS'] = TextoMostrable.LABEL_SERVICIOS_OPERATORIOS
    datos['LABEL_PACIENTE_CON_EXPEDIENTE'] = TextoMostrable.LABEL_PACIENTE_CON_EXPEDIENTE
    datos['LABEL_AREA_INGRESO'] = TextoMostrable.LABEL_AREA_INGRESO
    datos['LABEL_NUMERO_EXPEDIENTE'] = TextoMostrable.LABEL_NUMERO_EXPEDIENTE
    datos['LABEL_DIAS_HOSPITALIZACION'] = TextoMostrable.LABEL_DIAS_HOSPITALIZACION
    return datos


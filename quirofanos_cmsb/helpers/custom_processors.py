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
    return datos

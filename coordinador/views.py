# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.db import transaction

import calendar
from datetime import time

from quirofanos_cmsb.helpers.user_tests import es_coordinador
from quirofanos_cmsb.helpers import utils
from quirofanos_cmsb.models import IntervencionQuirurgica, Participacion, Quirofano
from quirofanos_cmsb.helpers.flash_messages import MensajeTemporalError, MensajeTemporalAviso, MensajeTemporalExito

@require_GET
@login_required
@user_passes_test(es_coordinador)
def solicitudes_quirofano(request):
	''' Controlador correspondiente al listado de solicitudes de quirofano realizadas por medicos

	Parametros:
	request -> Solicitud HTTP '''

	return render_to_response('coordinador/solicitudes_quirofano.html', context_instance=RequestContext(request))

@require_POST
@login_required
@user_passes_test(es_coordinador)
def eliminar_intervencion_quirurgica(request, area, ano, mes ,dia, id_intervencion):
    ''' Controlador correspondiente a la eliminacion de una intervencion quirurgica

    Parametros:
    request -> Solicitud HTTP
    id_intervencion -> identificador de la intervencion quirurgica que sera eliminada '''

    try:
        intervencion_quirurgica = IntervencionQuirurgica.objects.get(pk=id_intervencion)
    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, MensajeTemporalError.ELIMINAR_INTERVENCION_QUIRURGICA_INVALIDA)
        return redirect('plan_dia', area, ano, mes, dia)

    with transaction.atomic():
        reservacion = intervencion_quirurgica.reservacion
        lista_procedimientos = intervencion_quirurgica.procedimientoquirurgico_set.all()
        for procedimiento in lista_procedimientos:
            Participacion.objects.filter(procedimiento_quirurgico=procedimiento).delete()
            procedimiento.delete()

            reservacion.delete()

            intervencion_quirurgica.delete()

    messages.add_message(request, messages.WARNING, MensajeTemporalAviso.INTERVENCION_QUIRURGICA_ELIMINADA)
    return redirect('plan_dia', area, ano, mes, dia)

@require_POST
@login_required
@user_passes_test(es_coordinador)
def cambiar_horario_intervencion_quirurgica(request, id_intervencion, area, ano, mes, dia, id_quirofano, hora_inicio, duracion_en_medias_horas):
    ''' Controlador correspondiente al cambio de horario de una intervencion quirurgica

    Parametros:
    request -> Solicitud HTTP
    id_intervencion -> Intervencion que sera cambiada de horario
    ano -> Ano de la fecha del cambio
    mes -> Mes de la fecha del cambio
    dia -> Dia de la fecha del cambio
    id_quirofano -> Id del quirofano a asignar
    hora_inicio -> Hora nueva de inicio de la intervencion quirurgica
    duracion_en_medias_horas -> Nueva duracion de la intervencion quirurgica en cantidad de medias horas que ocupa a partir de la hora de inicio '''
    ano = int(ano)
    mes = int(mes)
    dia = int(dia)
    id_quirofano = int(id_quirofano)
    hora_inicio = float(hora_inicio)
    duracion_en_medias_horas = int(duracion_en_medias_horas)

    try:
        intervencion_quirurgica = IntervencionQuirurgica.objects.get(pk=id_intervencion)
        quirofano = Quirofano.objects.get(pk=id_quirofano)
    except ObjectDoesNotExist:
        raise Http404

    medias_horas_no_disponibles = quirofano.obtener_intervenciones_por_hora(ano, mes, dia).keys()
    turnos_disponibles = []
    turnos_atravesados = []
    utils.obtener_turnos_disponibles(duracion_en_medias_horas, medias_horas_no_disponibles, turnos_disponibles, turnos_atravesados)

    if mes < 1 or mes > 12:
        raise Http404
    if ano < 1:
        raise Http404
    if dia < 1 or dia > calendar.monthrange(ano, mes)[1]:
        raise Http404
    if hora_inicio not in turnos_disponibles:
        raise Http404

    hora_fin = hora_inicio + duracion_en_medias_horas*0.5

    with transaction.atomic():
        hora_inicio_tupla = utils.obtener_hora(hora_inicio)
        hora_fin_tupla = utils.obtener_hora(hora_fin)
        intervencion_quirurgica.hora_inicio = time(hora_inicio_tupla[0], hora_inicio_tupla[1])
        intervencion_quirurgica.hora_fin = time(hora_fin_tupla[0], hora_fin_tupla[1])
        intervencion_quirurgica.quirofano = quirofano
        intervencion_quirurgica.save()

    messages.add_message(request, messages.SUCCESS, MensajeTemporalExito.INTERVENCION_QUIRURGICA_HORARIO_CAMBIADO)
    return redirect('plan_dia', area, ano, mes, dia)







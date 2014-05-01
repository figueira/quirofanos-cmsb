# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.http import Http404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist

import calendar

from quirofanos_cmsb.helpers.user_tests import es_medico
from quirofanos_cmsb.helpers import utils
from quirofanos_cmsb.models import Quirofano

@require_GET
@login_required
@user_passes_test(es_medico)
def solicitud_quirofano(request, ano, mes, dia, id_quirofano, hora_inicio, duracion_en_medias_horas):
	''' Controlador correspondiente a la pagina del formulario de una nueva solicitud de quirofano

	Parametros:
	request -> Solicitud HTTP
	ano -> Ano de la fecha a ser solicitada
	mes -> Mes de la fecha a ser solicitada
	dia -> Dia de la fecha a ser solicitada
	id_quirofano -> Id del quirofano a ser solicitado
	hora_inicio -> Hora de inicio de la intervencion quirurgica
	duracion_en_medias_horas -> Duracion de la intervencion quirurgica en cantidad de medias horas que ocupa a partir de la hora de inicio '''
	ano = int(ano)
	mes = int(mes)
	dia = int(dia)
	id_quirofano = int(id_quirofano)
	hora_inicio = float(hora_inicio)
	duracion_en_medias_horas = int(duracion_en_medias_horas)

	try:
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

	# Implementar logica de controlador

	return render_to_response('medico/solicitud_quirofano.html', context_instance=RequestContext(request))

@require_GET
@login_required
@user_passes_test(es_medico)
def mis_solicitudes(request):
	 ''' Controlador correspondiente a la pagina del listado de solicitudes realizadas por el medico

	 Parametros:
	 request -> Solicitud HTTP '''

	 return render_to_response('medico/mis_solicitudes.html', context_instance=RequestContext(request))

@require_GET
@login_required
@user_passes_test(es_medico)
def proximas_intervenciones_quirurgicas(request):
	 ''' Controlador correspondiente a la pagina del listado de las proximas intervenciones quirurgicas del medico

	 Parametros:
	 request -> Solicitud HTTP '''

	 return render_to_response('medico/proximas_intervenciones_quirurgicas.html', context_instance=RequestContext(request))

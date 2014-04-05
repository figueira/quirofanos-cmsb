# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST

import datetime
from calendar import Calendar

from quirofanos_cmsb.helpers import utils

@require_GET
@login_required
def calendario(request, ano=datetime.date.today().year, mes=datetime.date.today().month):
	''' Controlador correspondiente al calendario de disponibilidad de quirofanos por mes

	Parametros:
	request -> Solicitud HTTP
	ano -> ano del calendario
	mes -> mes del calendario '''
	ano = int(ano)
	mes = int(mes)

	if mes < 1 or mes > 12:
		raise Http404
	if ano < 1:
		raise Http404

	calendario = Calendar()
	semanas = calendario.monthdays2calendar(ano, mes)
	datos  = {}
	datos['ano'] = ano
	datos['mes'] = mes
	datos['mes_nombre'] = utils.obtener_nombre_mes(mes)
	datos['semanas'] = semanas
	return render_to_response('plan_quirurgico/calendario.html', datos, context_instance=RequestContext(request))

def plan_dia(request):
	''' Controlador correspondiente al detalle del plan quirurgico por dia

	Parametros:
	request -> Solucitud HTTP '''

	return render_to_response('plan_quirurgico/plan_dia.html')

def plan_dia_obs(request):
	''' Controlador correspondiente al detalle del plan quirurgico por dia

	Parametros:
	request -> Solucitud HTTP '''

	return render_to_response('plan_quirurgico/plan_dia_obs.html')

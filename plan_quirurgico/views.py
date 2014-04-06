# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST

from datetime import date
from calendar import Calendar

from quirofanos_cmsb.helpers import utils
from quirofanos_cmsb.models import Quirofano

@require_GET
@login_required
def calendario(request, area_actual='QG', ano=date.today().year, mes=date.today().month):
	''' Controlador correspondiente al calendario de disponibilidad de quirofanos por mes

	Parametros:
	request -> Solicitud HTTP
	area -> area de quirofanos a ser consultada
	ano -> ano del calendario
	mes -> mes del calendario '''
	ano = int(ano)
	mes = int(mes)
	quirofanos_area_distinta = Quirofano.objects.distinct('area')
	areas = []
	areas_valores = []
	for quirofano in quirofanos_area_distinta:
		area = {}
		area['valor'] = quirofano.area
		area['nombre'] = quirofano.get_area_display()
		areas.append(area)
		areas_valores.append(area['valor'])
	quirofanos_area = Quirofano.objects.filter(area=area)

	if mes < 1 or mes > 12:
		raise Http404
	if ano < 1:
		raise Http404
	if area_actual not in areas_valores:
		raise Http404

	calendario = Calendar()
	semanas_tuplas = calendario.monthdays2calendar(ano, mes)
	semanas_diccionarios = []
	for semana in semanas_tuplas:
		semana_diccionario = []
		for dia in semana:
			dia_diccionario = {}
			dia_diccionario['dia_mes'] = dia[0]
			dia_diccionario['dia_semana'] = dia[1]
			nro_intervenciones = 0
			disponibilidad = True
			for quirofano in quirofanos_area:
				nro_intervenciones = nro_intervenciones + quirofano.obtener_nro_intervenciones(ano=ano, mes=mes, dia=dia[0])
				disponibilidad = quirofano.esta_disponible(ano=ano, mes=mes, dia=dia[0])
			dia_diccionario['nro_intervenciones'] = nro_intervenciones
			dia_diccionario['disponibilidad'] = disponibilidad
			semana_diccionario.append(dia_diccionario)
		semanas_diccionarios.append(semana_diccionario)

	datos  = {}
	datos['ano'] = ano
	datos['mes'] = mes
	datos['mes_nombre'] = utils.obtener_nombre_mes(mes)
	datos['area_actual'] = area_actual
	datos['areas'] = areas
	datos['semanas'] = semanas_diccionarios
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

# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST

from datetime import date
import calendar

from quirofanos_cmsb.helpers import utils
from quirofanos_cmsb.models import Quirofano
from quirofanos_cmsb.helpers.template_text import TextoMostrable

@require_GET
@login_required
def calendario(request, area_actual='QG', ano=date.today().year, mes=date.today().month):
	''' Controlador correspondiente al calendario de disponibilidad de quirofanos por mes

	Parametros:
	request -> Solicitud HTTP
	area -> Area de quirofanos a ser consultada
	ano -> Ano del calendario
	mes -> Mes del calendario '''
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

	if mes < 1 or mes > 12:
		raise Http404
	if ano < 1:
		raise Http404
	if area_actual not in areas_valores:
		raise Http404

	quirofanos_area_actual = Quirofano.objects.filter(area=area_actual)
	calendario = calendar.Calendar()
	semanas_tuplas = calendario.monthdays2calendar(ano, mes)
	semanas_diccionarios = []
	for semana in semanas_tuplas:
		semana_diccionario = []
		for dia in semana:
			dia_diccionario = {}
			dia_diccionario['dia_mes'] = dia[0]
			dia_diccionario['dia_semana'] = dia[1]
			numero_intervenciones = 0
			disponibilidad = True
			for quirofano in quirofanos_area_actual:
				numero_intervenciones = numero_intervenciones + quirofano.obtener_numero_intervenciones(ano=ano, mes=mes, dia=dia[0])
				disponibilidad = quirofano.esta_disponible(ano=ano, mes=mes, dia=dia[0])
			dia_diccionario['numero_intervenciones'] = numero_intervenciones
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

def plan_dia(request, area, ano, mes, dia):
	''' Controlador correspondiente al detalle del plan quirurgico por dia

	Parametros:
	request -> Solucitud HTTP
	area -> Area de quirofanos a consultar
	ano -> Ano a consultar
	mes -> Mes a consultar
	dia -> Dia a consultar '''
	ano = int(ano)
	mes = int(mes)
	dia = int(dia)
	areas_valores = Quirofano.objects.distinct('area').values_list('area', flat=True)
	if mes < 1 or mes > 12:
		raise Http404
	if ano < 1:
		raise Http404
	if area not in areas_valores:
		raise Http404
	if dia < 1 or dia > calendar.monthrange(ano, mes)[1]:
		raise Http404

	quirofanos_area = Quirofano.objects.filter(area=area)
	quirofanos_area_intervenciones = []
	for quirofano in quirofanos_area:
		quirofano_diccionario = {}
		if quirofano.numero == 0:
			quirofano_diccionario['nombre'] = TextoMostrable.SALA_RECUPERACION
		else:
			quirofano_diccionario['nombre'] = TextoMostrable.QUIROFANO + ' ' + str(quirofano.numero)
		quirofano_diccionario['intervenciones'] = quirofano.obtener_intervenciones_por_hora(ano, mes, dia)
		quirofanos_area_intervenciones.append(quirofano_diccionario)

	datos = {}
	datos['area_nombre'] = quirofanos_area[0].get_area_display()
	datos['ano'] = ano
	datos['mes'] = mes
	datos['dia'] = dia
	datos['quirofanos'] = quirofanos_area_intervenciones
	datos['medias_horas'] = [x for x in utils.rango_decimal(7, 19.5, 0.5)]
	datos['medias_horas_legibles'] = [utils.obtener_representacion_media_hora(x) for x in datos['medias_horas']]
	return render_to_response('plan_quirurgico/plan_dia.html', datos, context_instance=RequestContext(request))

def plan_dia_obs(request):
	''' Controlador correspondiente al detalle del plan quirurgico por dia

	Parametros:
	request -> Solucitud HTTP '''

	return render_to_response('plan_quirurgico/plan_dia_obs.html')

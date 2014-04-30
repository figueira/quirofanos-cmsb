# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.shortcuts import redirect

from datetime import date, timedelta
import calendar
import math

from quirofanos_cmsb.helpers import utils
from quirofanos_cmsb.models import Quirofano
from quirofanos_cmsb.helpers.template_text import TextoMostrable
from plan_quirurgico.forms import DuracionIntervencionQuirurgicaForm

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
	if not mes - 1 < 1:
		datos['mes_anterior'] = mes - 1
	else:
		datos['ano_anterior'] = ano - 1
		datos['mes_anterior'] = 12
	if not mes + 1 > 12:
		datos['mes_proximo'] = mes + 1
	else:
		datos['ano_proximo'] = ano + 1
		datos['mes_proximo'] = 1
	datos['mes_nombre'] = utils.obtener_nombre_mes(mes)
	datos['area_actual'] = area_actual
	datos['areas'] = areas
	datos['semanas'] = semanas_diccionarios
	return render_to_response('plan_quirurgico/calendario.html', datos, context_instance=RequestContext(request))

@require_http_methods(["GET", "POST"])
@login_required
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

	seleccionar_turno = False
	horas_intervencion = 0
	minutos_intervencion = 0
	cantidad_medias_horas_intervencion = 0
	formulario_duracion_intervencion_quirurgica = DuracionIntervencionQuirurgicaForm()
	if request.POST:
		formulario_duracion_intervencion_quirurgica = DuracionIntervencionQuirurgicaForm(request.POST)
		if formulario_duracion_intervencion_quirurgica.is_valid():
			seleccionar_turno = True
			horas_intervencion = formulario_duracion_intervencion_quirurgica.cleaned_data['horas']
			minutos_intervencion = formulario_duracion_intervencion_quirurgica.cleaned_data['minutos']
			duracion_horas = round(timedelta(hours=horas_intervencion, minutes=minutos_intervencion).total_seconds() / 3600, 2)
			cantidad_medias_horas_intervencion = int(math.ceil(duracion_horas / 0.5))

	quirofanos_area = Quirofano.objects.filter(area=area)
	quirofanos_area_intervenciones = []
	medias_horas = [x for x in utils.rango_decimal(7, 19.5, 0.5)]
	for quirofano in quirofanos_area:
		quirofano_diccionario = {}
		if quirofano.numero == 0:
			quirofano_diccionario['nombre'] = TextoMostrable.SALA_RECUPERACION
		else:
			quirofano_diccionario['nombre'] = TextoMostrable.QUIROFANO + ' ' + str(quirofano.numero)
		quirofano_diccionario['intervenciones'] = quirofano.obtener_intervenciones_por_hora(ano, mes, dia)
		if seleccionar_turno:
			medias_horas_disponibles = list(set(medias_horas).difference(set(quirofano_diccionario['intervenciones'].keys())))
			medias_horas_disponibles.sort()
			medias_horas_disponibles_para_duracion = []
			medias_horas_disponibles_atravesadas = []
			indices_por_saltar = 0
			for i in range(0, len(medias_horas_disponibles)):
				disponible = True
				if indices_por_saltar > 0:
					indices_por_saltar = indices_por_saltar - 1
					continue
				for j in range(1, cantidad_medias_horas_intervencion):
					if (i + j >= len(medias_horas_disponibles)) or not (medias_horas_disponibles[i+j] == medias_horas_disponibles[i] + j*0.5):
						disponible = False
						break
				if disponible:
					medias_horas_disponibles_para_duracion.append(medias_horas_disponibles[i])
					indices_por_saltar = cantidad_medias_horas_intervencion - 1
				else:
					medias_horas_disponibles_atravesadas.append(medias_horas_disponibles[i])
			quirofano_diccionario['turnos_disponibles'] = medias_horas_disponibles_para_duracion
			quirofano_diccionario['medias_horas_disponibles_atravesadas'] = medias_horas_disponibles_atravesadas
		quirofanos_area_intervenciones.append(quirofano_diccionario)

	datos = {}
	datos['area_nombre'] = quirofanos_area[0].get_area_display()
	datos['ano'] = ano
	datos['mes'] = mes
	datos['dia'] = dia
	datos['area_actual'] = area
	datos['quirofanos'] = quirofanos_area_intervenciones
	datos['medias_horas'] = medias_horas
	datos['medias_horas_legibles'] = [utils.obtener_representacion_media_hora(x) for x in medias_horas]
	datos['formulario_duracion_intervencion_quirurgica'] = formulario_duracion_intervencion_quirurgica
	datos['seleccionar_turno'] = seleccionar_turno
	datos['horas_intervencion'] = horas_intervencion
	datos['minutos_intervencion'] = minutos_intervencion
	datos['cantidad_medias_horas_intervencion'] = cantidad_medias_horas_intervencion
	return render_to_response('plan_quirurgico/plan_dia.html', datos, context_instance=RequestContext(request))

@require_GET
@login_required
def plan_dia_obs(request):
	''' Controlador correspondiente al detalle del plan quirurgico por dia

	Parametros:
	request -> Solucitud HTTP '''

	return render_to_response('plan_quirurgico/plan_dia_obs.html')


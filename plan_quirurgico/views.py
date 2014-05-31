# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import Http404, HttpResponse
from django.template import RequestContext, Context
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from datetime import date, timedelta
import calendar
import math
import cStringIO as StringIO
import ho.pisa as pisa
from django.template.loader import get_template
from cgi import escape

from quirofanos_cmsb.helpers import utils
from quirofanos_cmsb.models import Quirofano, IntervencionQuirurgica, Reservacion, Participacion, Medico
from quirofanos_cmsb.helpers.template_text import TextoMostrable
from plan_quirurgico.forms import DuracionIntervencionQuirurgicaForm
from autenticacion.forms import CambiarContrasenaForm, ActualizarEmailForm
from medico.forms import SolicitudQuirofanoForm
from quirofanos_cmsb.helpers.flash_messages import MensajeTemporalError, MensajeTemporalExito
from quirofanos_cmsb.helpers.utils import obtener_tipo_usuario, obtener_total_horas, obtener_representacion_media_hora

@require_http_methods(["GET", "POST"])
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

	tipo_usuario = obtener_tipo_usuario(request.user.cuenta)
	posee_email = False

	if tipo_usuario == 'medico':
		if request.user.cuenta.medico.email:
			posee_email = True
	elif tipo_usuario == 'departamento':
		if request.user.cuenta.departamento.email:
			posee_email = True
	else:
		posee_email = True

   	if not posee_email:
		if request.method == 'GET':
			formulario_actualizacion_email = ActualizarEmailForm()
		elif request.method == 'POST':
			formulario_actualizacion_email = ActualizarEmailForm(request.POST)
			if formulario_actualizacion_email.is_valid():
				correo_electronico = formulario_actualizacion_email.cleaned_data['correo_electronico']
				with transaction.atomic():
					if tipo_usuario == 'medico':
						request.user.cuenta.medico.email = correo_electronico
						request.user.cuenta.medico.save()
					elif tipo_usuario == 'departamento':
						request.user.cuenta.departamento.email = correo_electronico
						request.user.cuenta.departamento.save()
					posee_email = True

				messages.add_message(request, messages.SUCCESS,MensajeTemporalExito.ACTUALIZACION_EMAIL_EXITOSO)
		datos["formulario_actualizacion_email"] = formulario_actualizacion_email

	datos['posee_email'] = posee_email

	datos['es_primer_ingreso'] = True
	if request.user.check_password(request.user.cuenta.clave_inicial):
		if request.method == 'GET':
			formulario_cambio_contrasena = CambiarContrasenaForm()
		elif request.method == 'POST':
			formulario_cambio_contrasena = CambiarContrasenaForm(request.POST)
			if formulario_cambio_contrasena.is_valid():
				contrasena_actual = formulario_cambio_contrasena.cleaned_data['contrasena_actual']
				contrasena_nueva = formulario_cambio_contrasena.cleaned_data['contrasena_nueva']
				if request.user.check_password(contrasena_actual):
					with transaction.atomic():
						request.user.set_password(contrasena_nueva)
						request.user.save()
						if posee_email:
							messages.add_message(request, messages.SUCCESS,MensajeTemporalExito.CAMBIO_CONTRASENA_EXITOSO)
						else:
							messages.add_message(request, messages.SUCCESS,MensajeTemporalExito.CAMBIO_CONTRASENA_EXITOSO, extra_tags='modal')
						datos['es_primer_ingreso'] = False
						return redirect('calendario')
				else:
					messages.add_message(request, messages.ERROR,
						MensajeTemporalError.CAMBIO_CONTRASENA_FALLIDO,extra_tags='modal')
					return redirect('calendario')
		datos["formulario_cambio_contrasena"] = formulario_cambio_contrasena
	else:
		datos['es_primer_ingreso'] = False

	return render_to_response('plan_quirurgico/calendario.html', datos, context_instance=RequestContext(request))

@require_http_methods(["GET", "POST"])
@login_required
def plan_dia(request, area, ano, mes, dia):
	''' Controlador correspondiente al detalle del plan quirurgico por dia para usuarios medicos

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
	if request.user.cuenta.privilegio != '4':
		return redirect('plan_dia_obs', area, ano, mes, dia)

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
	medias_horas = utils.obtener_medias_horas()
	for quirofano in quirofanos_area:
		quirofano_diccionario = {}
		if quirofano.numero == 0:
			quirofano_diccionario['nombre'] = TextoMostrable.SALA_RECUPERACION
		else:
			quirofano_diccionario['nombre'] = TextoMostrable.QUIROFANO + ' ' + str(quirofano.numero)
		quirofano_diccionario['clave_primaria'] = quirofano.id
		quirofano_diccionario['intervenciones'] = quirofano.obtener_intervenciones_por_hora(ano, mes, dia)
		if seleccionar_turno:
			medias_horas_disponibles_para_duracion = []
			medias_horas_disponibles_atravesadas = []
			utils.obtener_turnos_disponibles(cantidad_medias_horas_intervencion, quirofano_diccionario['intervenciones'].keys(), medias_horas_disponibles_para_duracion, medias_horas_disponibles_atravesadas)
			quirofano_diccionario['turnos_disponibles'] = medias_horas_disponibles_para_duracion
			quirofano_diccionario['medias_horas_disponibles_atravesadas'] = medias_horas_disponibles_atravesadas
		quirofanos_area_intervenciones.append(quirofano_diccionario)

	if quirofanos_area_intervenciones[0]['nombre'] == TextoMostrable.SALA_RECUPERACION:
		quirofanos_area_sr = quirofanos_area_intervenciones.pop(0)
		quirofanos_area_intervenciones.append(quirofanos_area_sr)

	reservaciones_aprobadas = Reservacion.objects.filter(estado ='A', intervencion_quirurgica__fecha_intervencion__year=ano, intervencion_quirurgica__fecha_intervencion__month=mes, intervencion_quirurgica__fecha_intervencion__day=dia, intervencion_quirurgica__quirofano__area=area)

	reservaciones_aprobadas_diccionarios = []
	for reservacion in reservaciones_aprobadas:
		reservacion_diccionario = {}
		reservacion_diccionario["objeto"] = reservacion
		if reservacion.intervencion_quirurgica.quirofano.numero == 0:
			quirofano_legible = TextoMostrable.SALA_RECUPERACION
		else:
			quirofano_legible = TextoMostrable.QUIROFANO + ' ' + str(reservacion.intervencion_quirurgica.quirofano.numero)

		reservacion_diccionario["quirofano_legible"] = quirofano_legible
		reservacion_diccionario["area_legible"] = reservacion.intervencion_quirurgica.quirofano.get_area_display()
		reservacion_diccionario["hora_inicio_legible"] = utils.obtener_representacion_media_hora(utils.obtener_total_horas(reservacion.intervencion_quirurgica.hora_inicio))
		reservacion_diccionario["hora_fin_legible"] = utils.obtener_representacion_media_hora(utils.obtener_total_horas(reservacion.intervencion_quirurgica.hora_fin))
		datos_formulario = {}
		datos_formulario["nombre_paciente"] = reservacion.intervencion_quirurgica.paciente.nombre
		datos_formulario["apellido_paciente"] = reservacion.intervencion_quirurgica.paciente.apellido
		datos_formulario["nacionalidad_paciente"] = reservacion.intervencion_quirurgica.paciente.cedula[:2]
		datos_formulario["cedula_paciente"] = reservacion.intervencion_quirurgica.paciente.cedula[2:]
		datos_formulario["fecha_nacimiento_paciente"] = reservacion.intervencion_quirurgica.paciente.fecha_nacimiento
		datos_formulario["codigo_telefono_paciente"] = reservacion.intervencion_quirurgica.paciente.telefono[:4]
		datos_formulario["numero_telefono_paciente"] = reservacion.intervencion_quirurgica.paciente.telefono[5:]
		datos_formulario["genero_paciente"] = reservacion.intervencion_quirurgica.paciente.genero
		if reservacion.intervencion_quirurgica.paciente.compania_aseguradora:
			datos_formulario["tipo_pago_paciente"] = "S"
			datos_formulario["compania_aseguradora_paciente"] = reservacion.intervencion_quirurgica.paciente.compania_aseguradora
		else:
			datos_formulario["tipo_pago_paciente"] = "P"

		if reservacion.intervencion_quirurgica.paciente.numero_expediente:
			datos_formulario["paciente_con_expediente"] = True
			datos_formulario["area_ingreso_paciente"] = reservacion.intervencion_quirurgica.paciente.area_ingreso
			datos_formulario["numero_expediente_paciente"] = reservacion.intervencion_quirurgica.paciente.numero_expediente
		else:
			datos_formulario["paciente_con_expediente"] = False

		if reservacion.intervencion_quirurgica.paciente.numero_habitacion:
			datos_formulario["paciente_hospitalizado"] = True
			datos_formulario["numero_habitacion_paciente"] = reservacion.intervencion_quirurgica.paciente.numero_habitacion
		else:
			datos_formulario["paciente_hospitalizado"] = False

		datos_formulario["diagnostico_ingreso_paciente"] = reservacion.intervencion_quirurgica.paciente.diagnostico_ingreso
		datos_formulario["servicios_operatorios_paciente"] = reservacion.intervencion_quirurgica.paciente.servicios_operatorios_requeridos.all()
		datos_formulario["preferencia_anestesica"] = reservacion.intervencion_quirurgica.preferencia_anestesica
		if reservacion.intervencion_quirurgica.observaciones:
			datos_formulario["observaciones"] = reservacion.intervencion_quirurgica.observaciones

		datos_formulario["riesgo"] = reservacion.intervencion_quirurgica.riesgo
		if reservacion.intervencion_quirurgica.riesgo == "M":
			datos_formulario["razon_riesgo"] = reservacion.intervencion_quirurgica.razon_riesgo

		datos_formulario["materiales_quirurgicos_requeridos"] = reservacion.intervencion_quirurgica.materiales_quirurgicos_requeridos.all()
		datos_formulario["equipos_especiales_requeridos"] = reservacion.intervencion_quirurgica.equipos_especiales_requeridos.all()
		datos_formulario["dias_hospitalizacion"] = reservacion.dias_hospitalizacion

		reservacion_diccionario["formulario"] = SolicitudQuirofanoForm(datos_formulario)
		reservaciones_aprobadas_diccionarios.append(reservacion_diccionario)

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
	datos["reservaciones"] = reservaciones_aprobadas_diccionarios

	return render_to_response('plan_quirurgico/plan_dia.html', datos, context_instance=RequestContext(request))

@require_GET
@login_required
def plan_dia_obs(request, area, ano, mes, dia):
	''' Controlador correspondiente al detalle del plan quirurgico por dia para usuarios observadores

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
	quirofanos_area = Quirofano.objects.filter(area=area)
	if mes < 1 or mes > 12:
		raise Http404
	if ano < 1:
		raise Http404
	if area not in areas_valores:
		raise Http404
	if dia < 1 or dia > calendar.monthrange(ano, mes)[1]:
		raise Http404

	intervenciones = []
	lista_intervenciones_area = IntervencionQuirurgica.objects.filter(fecha_intervencion__year=ano, fecha_intervencion__month=mes, fecha_intervencion__day=dia, reservacion__estado='A', quirofano__area=area).order_by('quirofano','hora_fin','hora_inicio')

	for intervencion in lista_intervenciones_area:
		intervencion_diccionario = {}
		intervencion_diccionario['objeto'] = intervencion
		procedimientos = intervencion.procedimientoquirurgico_set.all()
		intervencion_diccionario['procedimientos'] = procedimientos
		intervencion_diccionario['hora_inicio'] = obtener_representacion_media_hora(obtener_total_horas(intervencion.hora_inicio))
		intervencion_diccionario['hora_fin'] = obtener_representacion_media_hora(obtener_total_horas(intervencion.hora_fin))
		anestesiologo_id = Participacion.objects.get(procedimiento_quirurgico_id=procedimientos.first().id, rol=0).medico_id
		intervencion_diccionario['anestesiologo'] = Medico.objects.get(id=anestesiologo_id)
		intervenciones.append(intervencion_diccionario)

	datos = {}
	datos['area_nombre'] = quirofanos_area[0].get_area_display()
	datos['ano'] = ano
	datos['mes'] = mes
	datos['dia'] = dia
	datos['area_actual'] = area
	datos['quirofanos_area'] = quirofanos_area
	datos['intervenciones'] = intervenciones

	return render_to_response('plan_quirurgico/plan_dia_obs.html', datos, context_instance=RequestContext(request))

@require_GET
@login_required
def plan_dia_pdf(request, area, ano, mes, dia):
	''' Controlador correspondiente a la generacion del plan quirurgico en PDF

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
	quirofanos_area = Quirofano.objects.filter(area=area)

	intervenciones = []
	lista_intervenciones_area = IntervencionQuirurgica.objects.filter(fecha_intervencion__year=ano, fecha_intervencion__month=mes, fecha_intervencion__day=dia, reservacion__estado='A', quirofano__area=area).order_by('quirofano','hora_fin','hora_inicio')

	for intervencion in lista_intervenciones_area:
		intervencion_diccionario = {}
		intervencion_diccionario['objeto'] = intervencion
		procedimientos = intervencion.procedimientoquirurgico_set.all()
		intervencion_diccionario['procedimientos'] = procedimientos
		intervencion_diccionario['hora_inicio'] = obtener_representacion_media_hora(obtener_total_horas(intervencion.hora_inicio))
		intervencion_diccionario['hora_fin'] = obtener_representacion_media_hora(obtener_total_horas(intervencion.hora_fin))
		anestesiologo_id = Participacion.objects.get(procedimiento_quirurgico_id=procedimientos.first().id, rol=0).medico_id
		intervencion_diccionario['anestesiologo'] = Medico.objects.get(id=anestesiologo_id)
		intervenciones.append(intervencion_diccionario)

	return render_to_pdf('plan_dia_pdf.html',
		{
		'area_nombre': quirofanos_area[0].get_area_display(),
		'ano' : ano,
		'mes': mes,
		'dia' : dia,
		'quirofanos_area': quirofanos_area,
		'intervenciones': intervenciones,
		'img_path': '/static/img/logo_centro_medico.png',
		'pagesize':'A4',
		})


def render_to_pdf(template_src, context_dict):
	template = get_template(template_src)
	context = Context(context_dict)
	html  = template.render(context)
	result = StringIO.StringIO()

	pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		response = HttpResponse(result.getvalue(), mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=plan_quirurgico.pdf'
        return response
	return HttpResponse('ERROR<pre>%s</pre>' % escape(html))

# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.http import Http404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.forms.forms import NON_FIELD_ERRORS
from django.db import transaction
from django.contrib import messages

import calendar
import json
from datetime import date
from datetime import time

from quirofanos_cmsb.helpers.user_tests import es_medico
from quirofanos_cmsb.helpers import utils
from quirofanos_cmsb.helpers.template_text import TextoMostrable
from quirofanos_cmsb.helpers.flash_messages import MensajeTemporalError, MensajeTemporalExito
from quirofanos_cmsb.models import Quirofano, SistemaCorporal, OrganoCorporal, TipoProcedimientoQuirurgico, Participacion, ProcedimientoQuirurgico, Reservacion, IntervencionQuirurgica, Paciente
from medico.forms import SolicitudQuirofanoForm, ProcedimientoQuirurgicoForm, EliminarProcedimientoQuirurgicoForm

@require_http_methods(["GET", "POST"])
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

	if quirofano.numero == 0:
		quirofano_legible = TextoMostrable.SALA_RECUPERACION
	else:
		quirofano_legible = TextoMostrable.QUIROFANO + ' ' + str(quirofano.numero)

	area_legible = quirofano.get_area_display()
	fecha_intervencion_legible = str(dia) + "/" + str(mes) + "/" + str(ano)
	hora_inicio_legible = utils.obtener_representacion_media_hora(hora_inicio)
	hora_fin = hora_inicio + duracion_en_medias_horas*0.5
	hora_fin_legible = utils.obtener_representacion_media_hora(hora_fin)

	formulario_solicitud_quirofano = SolicitudQuirofanoForm(prefix="solicitud_quirofano")
	formulario_procedimiento_quirurgico = ProcedimientoQuirurgicoForm(prefix="procedimiento_quirurgico")
	formulario_eliminar_procedimiento_quirurgico = EliminarProcedimientoQuirurgicoForm(prefix="eliminar_procedimiento_quirurgico")
	agregando_procedimiento = False
	procedimiento_agregado = False
	procedimiento_eliminado = False
	procedimientos_quirurgicos = ProcedimientoQuirurgico.objects.filter(intervencion_quirurgica=None)
	errores_primera_pagina = True
	id_sistema_corporal_actual = None

	if request.method == 'POST':
		formulario_solicitud_quirofano = SolicitudQuirofanoForm(prefix="solicitud_quirofano", data=request.POST)
		formulario_procedimiento_quirurgico = ProcedimientoQuirurgicoForm(prefix="procedimiento_quirurgico", data=request.POST)
		formulario_eliminar_procedimiento_quirurgico = EliminarProcedimientoQuirurgicoForm(prefix="eliminar_procedimiento_quirurgico", data=request.POST)
		if request.POST["accion"] == "procedimiento_quirurgico":
			agregando_procedimiento = True
			try:
				formulario_procedimiento_quirurgico_valido = formulario_procedimiento_quirurgico.is_valid()
				id_organo_corporal = formulario_procedimiento_quirurgico.cleaned_data["id_organo_corporal"]
				id_tipo_procedimiento_quirurgico = formulario_procedimiento_quirurgico.cleaned_data["id_tipo_procedimiento_quirurgico"]
				organo_corporal = OrganoCorporal.objects.get(pk=id_organo_corporal)
				tipo_procedimiento_quirurgico = TipoProcedimientoQuirurgico.objects.get(pk=id_tipo_procedimiento_quirurgico)
				if tipo_procedimiento_quirurgico not in organo_corporal.tipos_procedimientos_permitidos.all():
					raise ObjectDoesNotExist

				id_sistema_corporal_actual = organo_corporal.sistema_corporal_id

				if formulario_procedimiento_quirurgico_valido:
					monto_honorarios_cirujano_principal = formulario_procedimiento_quirurgico.cleaned_data["monto_honorarios_cirujano_principal"]
					anestesiologo = formulario_procedimiento_quirurgico.cleaned_data["anestesiologo"]
					primer_ayudante = formulario_procedimiento_quirurgico.cleaned_data["primer_ayudante"]
					segundo_ayudante = formulario_procedimiento_quirurgico.cleaned_data["segundo_ayudante"]
					tercer_ayudante = formulario_procedimiento_quirurgico.cleaned_data["tercer_ayudante"]
					monto_honorarios_tercer_ayudante = formulario_procedimiento_quirurgico.cleaned_data["monto_honorarios_tercer_ayudante"]
					with transaction.atomic():
						procedimiento_quirurgico = ProcedimientoQuirurgico()
						procedimiento_quirurgico.organo_corporal = organo_corporal
						procedimiento_quirurgico.tipo_procedimiento_quirurgico = tipo_procedimiento_quirurgico
						procedimiento_quirurgico.monto_honorarios_cirujano_principal = monto_honorarios_cirujano_principal
						procedimiento_quirurgico.save()
						Participacion.objects.create(procedimiento_quirurgico=procedimiento_quirurgico, medico=anestesiologo, rol='0', monto_honorarios=procedimiento_quirurgico.obtener_monto_honorarios_anestesiologo())
						Participacion.objects.create(procedimiento_quirurgico=procedimiento_quirurgico, medico=primer_ayudante, rol='1', monto_honorarios=procedimiento_quirurgico.obtener_monto_honorarios_primer_ayudante())
						Participacion.objects.create(procedimiento_quirurgico=procedimiento_quirurgico, medico=segundo_ayudante, rol='2', monto_honorarios=procedimiento_quirurgico.obtener_monto_honorarios_segundo_ayudante())
						if not monto_honorarios_tercer_ayudante:
							monto_honorarios_tercer_ayudante = 0.00

						Participacion.objects.create(procedimiento_quirurgico=procedimiento_quirurgico, medico=tercer_ayudante, rol='3', monto_honorarios=monto_honorarios_tercer_ayudante)
					agregando_procedimiento = False
					procedimiento_agregado = True

			except ObjectDoesNotExist:
				lista_errores = formulario_procedimiento_quirurgico.error_class([MensajeTemporalError.TIPO_PROCEDIMIENTO_QUIRURGICO_INVALIDO])
				formulario_procedimiento_quirurgico._errors[NON_FIELD_ERRORS] = lista_errores

		elif request.POST["accion"] == "eliminar_procedimiento_quirurgico":
			try:
				formulario_eliminar_procedimiento_quirurgico_valido = formulario_eliminar_procedimiento_quirurgico.is_valid()
				id_procedimiento_quirurgico = formulario_eliminar_procedimiento_quirurgico.cleaned_data["id_procedimiento_quirurgico"]
				procedimiento_quirurgico = ProcedimientoQuirurgico.objects.get(pk=id_procedimiento_quirurgico)
				if formulario_eliminar_procedimiento_quirurgico_valido:
					with transaction.atomic():
						Participacion.objects.filter(procedimiento_quirurgico=procedimiento_quirurgico).delete()
						procedimiento_quirurgico.delete()
					procedimiento_eliminado = True

			except ObjectDoesNotExist:
				lista_errores = formulario_eliminar_procedimiento_quirurgico.error_class([MensajeTemporalError.ELIMINAR_PROCEDIMIENTO_QUIRURGICO_INVALIDO])
				formulario_eliminar_procedimiento_quirurgico._errors[NON_FIELD_ERRORS] = lista_errores

		elif request.POST["accion"] == "solicitud_quirofano":
			formulario_solicitud_quirofano_valido = formulario_solicitud_quirofano.is_valid()
			if procedimientos_quirurgicos.count() > 0:
				if formulario_solicitud_quirofano_valido:
					with transaction.atomic():
						cedula_paciente = formulario_solicitud_quirofano.cleaned_data["nacionalidad_paciente"] + formulario_solicitud_quirofano.cleaned_data["cedula_paciente"]
						paciente = Paciente()
						if not Paciente.objects.filter(cedula=cedula_paciente):
							paciente.nombre = formulario_solicitud_quirofano.cleaned_data["nombre_paciente"]
							paciente.apellido = formulario_solicitud_quirofano.cleaned_data["apellido_paciente"]
							paciente.cedula = cedula_paciente
							paciente.fecha_nacimiento = formulario_solicitud_quirofano.cleaned_data["fecha_nacimiento_paciente"]
							paciente.genero = formulario_solicitud_quirofano.cleaned_data["genero_paciente"]
						else:
							paciente = Paciente.objects.get(cedula=cedula_paciente)

						paciente.telefono = formulario_solicitud_quirofano.cleaned_data["codigo_telefono_paciente"] + "-" + formulario_solicitud_quirofano.cleaned_data["numero_telefono_paciente"]
						paciente.diagnostico_ingreso = formulario_solicitud_quirofano.cleaned_data["diagnostico_ingreso_paciente"]
						if formulario_solicitud_quirofano.cleaned_data["paciente_con_expediente"]:
							paciente.area_ingreso = formulario_solicitud_quirofano.cleaned_data["area_ingreso_paciente"]
							paciente.numero_expediente =  formulario_solicitud_quirofano.cleaned_data["numero_expediente_paciente"]

						if formulario_solicitud_quirofano.cleaned_data["paciente_hospitalizado"]:
							paciente.numero_habitacion = formulario_solicitud_quirofano.cleaned_data["numero_habitacion_paciente"]

						if formulario_solicitud_quirofano.cleaned_data["tipo_pago_paciente"] == "S":
							paciente.compania_aseguradora = formulario_solicitud_quirofano.cleaned_data["compania_aseguradora_paciente"]

						paciente.save()

						servicios_operatorios_paciente = formulario_solicitud_quirofano.cleaned_data.get("servicios_operatorios_paciente")
						if servicios_operatorios_paciente is not []:
							paciente.servicios_operatorios_requeridos = servicios_operatorios_paciente
						paciente.save()

						intervencion_quirurgica = IntervencionQuirurgica()
						intervencion_quirurgica.paciente = paciente
						intervencion_quirurgica.estado = "0"
						intervencion_quirurgica.fecha_intervencion = date(ano, mes, dia)
						hora_inicio_tupla = utils.obtener_hora(hora_inicio)
						hora_fin_tupla = utils.obtener_hora(hora_fin)
						intervencion_quirurgica.hora_inicio = time(hora_inicio_tupla[0], hora_inicio_tupla[1])
						intervencion_quirurgica.hora_fin = time(hora_fin_tupla[0], hora_fin_tupla[1])
						intervencion_quirurgica.observaciones = formulario_solicitud_quirofano.cleaned_data["observaciones"]
						intervencion_quirurgica.preferencia_anestesica = formulario_solicitud_quirofano.cleaned_data["preferencia_anestesica"]
						intervencion_quirurgica.quirofano = quirofano
						intervencion_quirurgica.riesgo = formulario_solicitud_quirofano.cleaned_data["riesgo"]
						if intervencion_quirurgica.riesgo == "M":
							intervencion_quirurgica.razon_riesgo = formulario_solicitud_quirofano.cleaned_data["razon_riesgo"]

						intervencion_quirurgica.save()

						materiales_quirurgicos_requeridos = formulario_solicitud_quirofano.cleaned_data.get("materiales_quirurgicos_requeridos")
						if materiales_quirurgicos_requeridos is not []:
							intervencion_quirurgica.materiales_quirurgicos_requeridos = materiales_quirurgicos_requeridos

						equipos_especiales_requeridos = formulario_solicitud_quirofano.cleaned_data.get("equipos_especiales_requeridos")
						if equipos_especiales_requeridos is not []:
							intervencion_quirurgica.equipos_especiales_requeridos = equipos_especiales_requeridos

						intervencion_quirurgica.save()

						reservacion = Reservacion()
						reservacion.intervencion_quirurgica = intervencion_quirurgica
						reservacion.dias_hospitalizacion = formulario_solicitud_quirofano.cleaned_data["dias_hospitalizacion"]
						reservacion.estado = "P"
						reservacion.tipo_solicitud = "1"
						reservacion.medico = request.user.cuenta.medico
						reservacion.save()

						for procedimiento_quirurgico in procedimientos_quirurgicos:
							procedimiento_quirurgico.intervencion_quirurgica = intervencion_quirurgica
							procedimiento_quirurgico.save()

					messages.add_message(request, messages.SUCCESS, MensajeTemporalExito.SOLICITUD_QUIROFANO_ENVIADA)
					return redirect('mis_solicitudes')

			else:
				errores_primera_pagina = formulario_solicitud_quirofano["nombre_paciente"].errors or formulario_solicitud_quirofano["apellido_paciente"].errors or formulario_solicitud_quirofano["cedula_paciente"].errors or formulario_solicitud_quirofano["genero_paciente"].errors or formulario_solicitud_quirofano["fecha_nacimiento_paciente"].errors or formulario_solicitud_quirofano["codigo_telefono_paciente"].errors or formulario_solicitud_quirofano["numero_telefono_paciente"].errors or formulario_solicitud_quirofano["diagnostico_ingreso_paciente"].errors or formulario_solicitud_quirofano["servicios_operatorios_paciente"].errors or formulario_solicitud_quirofano["paciente_hospitalizado"].errors or formulario_solicitud_quirofano["numero_habitacion_paciente"].errors or formulario_solicitud_quirofano["paciente_con_expediente"].errors or formulario_solicitud_quirofano["area_ingreso_paciente"].errors or formulario_solicitud_quirofano["numero_expediente_paciente"].errors or formulario_solicitud_quirofano["tipo_pago_paciente"].errors or formulario_solicitud_quirofano["compania_aseguradora_paciente"].errors

				lista_errores = formulario_solicitud_quirofano.error_class([MensajeTemporalError.NO_SE_AGREGO_PROCEDIMIENTO_QUIRURGICO])
				formulario_solicitud_quirofano._errors[NON_FIELD_ERRORS] = lista_errores

	sistemas_corporales = SistemaCorporal.objects.all()
	sistemas_corporales_diccionarios = []
	for sistema_corporal in sistemas_corporales:
		sistema_corporal_diccionario = {}
		sistema_corporal_diccionario["id"] = sistema_corporal.id
		sistema_corporal_diccionario["codigo_icd_10_pcs"] = sistema_corporal.codigo_icd_10_pcs
		sistema_corporal_diccionario["nombre"] = sistema_corporal.nombre

		organos_corporales_asociados = sistema_corporal.organocorporal_set.all()
		organos_corporales_asociados_diccionarios = []
		for organo_corporal_asociado in organos_corporales_asociados:
			organo_corporal_asociado_diccionario = {}
			organo_corporal_asociado_diccionario["id"] = organo_corporal_asociado.id
			organo_corporal_asociado_diccionario["codigo_icd_10_pcs"] = organo_corporal_asociado.codigo_icd_10_pcs
			organo_corporal_asociado_diccionario["nombre"] = organo_corporal_asociado.nombre

			tipos_procedimientos_permitidos = organo_corporal_asociado.tipos_procedimientos_permitidos.all()
			tipos_procedimientos_permitidos_diccionarios = []
			for tipo_procedimiento_permitido in tipos_procedimientos_permitidos:
				tipo_procedimiento_permitido_diccionario = {}
				tipo_procedimiento_permitido_diccionario["id"] = tipo_procedimiento_permitido.id
				tipo_procedimiento_permitido_diccionario["codigo_icd_10_pcs"] = tipo_procedimiento_permitido.codigo_icd_10_pcs
				tipo_procedimiento_permitido_diccionario["nombre"] = tipo_procedimiento_permitido.nombre
				tipos_procedimientos_permitidos_diccionarios.append(tipo_procedimiento_permitido_diccionario)

			organo_corporal_asociado_diccionario["tipos_procedimientos_permitidos"] = tipos_procedimientos_permitidos_diccionarios
			organos_corporales_asociados_diccionarios.append(organo_corporal_asociado_diccionario)

		sistema_corporal_diccionario["organos_corporales"] = organos_corporales_asociados_diccionarios
		sistemas_corporales_diccionarios.append(sistema_corporal_diccionario)

	datos = {}
	datos["dia"] = dia
	datos["mes"] = mes
	datos["ano"] = ano
	datos["hora_inicio"] = hora_inicio
	datos["id_quirofano"] = id_quirofano
	datos["duracion_en_medias_horas"] = duracion_en_medias_horas
	datos["formulario_solicitud_quirofano"] = formulario_solicitud_quirofano
	datos["formulario_procedimiento_quirurgico"] = formulario_procedimiento_quirurgico
	datos["formulario_eliminar_procedimiento_quirurgico"] = formulario_eliminar_procedimiento_quirurgico
	datos["agregando_procedimiento"] = agregando_procedimiento
	datos["procedimiento_agregado"] = procedimiento_agregado
	datos["procedimiento_eliminado"] = procedimiento_eliminado
	datos["accion"] = "solicitud_quirofano"
	datos["quirofano_legible"] = quirofano_legible
	datos["area_legible"] = area_legible
	datos["hora_inicio_legible"] = hora_inicio_legible
	datos["hora_fin_legible"] = hora_fin_legible
	datos["fecha_intervencion_legible"] = fecha_intervencion_legible
	datos["json_sistemas_corporales"] = json.dumps(sistemas_corporales_diccionarios, sort_keys=True, indent=4, separators=(',', ': '))
	datos["procedimientos_quirurgicos"] = procedimientos_quirurgicos
	datos["nombre_cirujano_principal"] = request.user.cuenta.medico.nombre
	datos["apellido_cirujano_principal"] = request.user.cuenta.medico.apellido
	datos["errores_primera_pagina"] = errores_primera_pagina
	datos["id_sistema_corporal_actual"] = id_sistema_corporal_actual

	return render_to_response('medico/solicitud_quirofano.html', datos,  context_instance=RequestContext(request))

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

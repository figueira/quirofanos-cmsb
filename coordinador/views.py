# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.template import RequestContext
from django.contrib import messages
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

import calendar
from datetime import date, timedelta

from quirofanos_cmsb.helpers.flash_messages import MensajeTemporalError, MensajeTemporalExito, MensajeTemporalAviso, construir_mensaje
from quirofanos_cmsb.helpers import utils
from quirofanos_cmsb.helpers.template_text import TextoMostrable
from quirofanos_cmsb.helpers.user_tests import es_coordinador
from quirofanos_cmsb.models import Reservacion, IntervencionQuirurgica, Participacion, Quirofano
from coordinador.forms import GestionarSolicitudQuirofanoForm

@require_GET
@login_required
@user_passes_test(es_coordinador)
def solicitudes_quirofanos(request, estado="pendientes", periodo=1):
    ''' Controlador correspondiente al listado de solicitudes de quirofano realizadas por medicos

    Parametros:
    request -> Solicitud HTTP
    estado -> Estado de las solicitudes a consultar
    periodo -> Periodo a consultar '''
    periodo = int(periodo)
    if periodo < 1 or periodo > 3:
        raise Http404
    if estado not in ("pendientes", "aprobadas", "rechazadas"):
        raise Http404

    datos = {}
    fecha_valor = date.today() - timedelta(days=8)
    datos['tipo_busqueda'] = TextoMostrable.ULTIMA_SEMANA
    if (periodo == 2):
        fecha_valor = date.today() - timedelta(days=31)
        datos['tipo_busqueda'] = TextoMostrable.ULTIMO_MES
    elif (periodo == 3):
        fecha_valor = date.today() - timedelta(days=93)
        datos['tipo_busqueda'] = TextoMostrable.ULTIMOS_TRES_MESES

    lista_solicitudes_quirofano_pendientes = Reservacion.objects.filter(estado='P', fecha_reservacion__gte=fecha_valor).order_by('-fecha_reservacion')
    lista_solicitudes_quirofano_aprobadas = Reservacion.objects.filter(estado='A', fecha_reservacion__gte=fecha_valor).order_by('-fecha_reservacion')
    lista_solicitudes_quirofano_rechazadas = Reservacion.objects.filter(estado='R', fecha_reservacion__gte=fecha_valor).order_by('-fecha_reservacion')
    numero_solicitudes_pendientes = Reservacion.objects.filter(estado='P').count()

    paginator_pendientes = Paginator(lista_solicitudes_quirofano_pendientes, 10)
    page = request.GET.get('page')
    try:
        lista_solicitudes_quirofano_pendientes = paginator_pendientes.page(page)
    except PageNotAnInteger:
        lista_solicitudes_quirofano_pendientes = paginator_pendientes.page(1)
    except EmptyPage:
        lista_solicitudes_quirofano_pendientes = paginator_pendientes.page(paginator_pendientes.num_pages)

    paginator_aprobadas = Paginator(lista_solicitudes_quirofano_aprobadas, 10)
    page = request.GET.get('page')
    try:
        lista_solicitudes_quirofano_aprobadas = paginator_aprobadas.page(page)
    except PageNotAnInteger:
        lista_solicitudes_quirofano_aprobadas = paginator_aprobadas.page(1)
    except EmptyPage:
        lista_solicitudes_quirofano_aprobadas = paginator_aprobadas.page(paginator_aprobadas.num_pages)

    paginator_rechazadas = Paginator(lista_solicitudes_quirofano_rechazadas, 10)
    page = request.GET.get('page')
    try:
        lista_solicitudes_quirofano_rechazadas = paginator_rechazadas.page(page)
    except PageNotAnInteger:
        lista_solicitudes_quirofano_rechazadas = paginator_rechazadas.page(1)
    except EmptyPage:
        lista_solicitudes_quirofano_rechazadas = paginator_rechazadas.page(paginator_rechazadas.num_pages)

    datos['lista_solicitudes_quirofano_pendientes'] = lista_solicitudes_quirofano_pendientes
    datos['lista_solicitudes_quirofano_aprobadas'] = lista_solicitudes_quirofano_aprobadas
    datos['lista_solicitudes_quirofano_rechazadas'] = lista_solicitudes_quirofano_rechazadas
    datos['numero_solicitudes_pendientes'] = numero_solicitudes_pendientes
    datos['estado_solicitud'] = estado
    datos['formulario_solicitud_quirofano'] = GestionarSolicitudQuirofanoForm()

    return render_to_response('coordinador/solicitudes_quirofanos.html', datos, context_instance=RequestContext(request))

@require_POST
@login_required
@user_passes_test(es_coordinador)
def aceptar_solicitud_quirofano(request):
    ''' Controlador correspondiente a la aprobacion de solicitudes de quirofanos

    Parametros:
    request -> Solicitud HTTP '''
    formulario_solicitud_quirofano = GestionarSolicitudQuirofanoForm(request.POST)
    if formulario_solicitud_quirofano.is_valid():
        id_reservacion = int(formulario_solicitud_quirofano.cleaned_data['id_reservacion'])
        try:
            reservacion_quirofano = Reservacion.objects.get(id=id_reservacion)
        except ObjectDoesNotExist:
            #messages.add_message(request, messages.ERROR, MensajeTemporalError. APROBACION_USUARIO_FALLIDA)

        with transaction.atomic():
            reservacion_quirofano.estado = 'A'
            reservacion_quirofano.save()

        ''' Enviar Email al usuario '''
        tipo_usuario = ''
        try:
            if cuenta_usuario.medico:
                tipo_usuario = 'medico'
        except ObjectDoesNotExist:
            tipo_usuario = 'departamento'
        if tipo_usuario == 'medico':
            if cuenta_usuario.medico.email:
                enviar_email(asunto='Su cuenta ha sido aprobada.', contenido_texto='La cuenta solicitada ha sido aprobada. Su usuario es: ' + cuenta_usuario.usuario.username + ' y su clave de acceso es: ' + cuenta_usuario.clave_inicial + ' .', contenido_html='', recipiente='mjramos91@gmail.com')
        elif tipo_usuario == 'departamento':
            if cuenta_usuario.departamento.email:
                enviar_email(asunto='Su cuenta ha sido aprobada.', contenido_texto='La cuenta solicitada ha sido aprobada. Su usuario es: ' + cuenta_usuario.usuario.username + ' y su clave de acceso es: ' + cuenta_usuario.clave_inicial + ' .', contenido_html='', recipiente='mjramos91@gmail.com')

        messages.add_message(request, messages.SUCCESS, construir_mensaje(MensajeTemporalExito.SOLICITUD_USUARIO_APROBADA, "La clave de acceso del usuario es: " + cuenta_usuario.clave_inicial))
    else:
        messages.add_message(request, messages.ERROR, MensajeTemporalError. APROBACION_USUARIO_FALLIDA)

    return redirect('solicitudes_quirofanos')

@require_POST
@login_required
@user_passes_test(es_coordinador)
def rechazar_solicitud_usuario(request):
    ''' Controlador correspondiente al rechazo de solicitudes de quirofanos

    Parametros:
    request -> Solicitud HTTP '''
    formulario_solicitud_quirofano = GestionarSolicitudQuirofanoForm(request.POST)
    if formulario_solicitud_quirofano.is_valid():
        id_reservacion = int(formulario_solicitud_quirofano.cleaned_data['id_reservacion'])
        try:
            reservacion_quirofano = Reservacion.objects.get(id=id_reservacion)
        except ObjectDoesNotExist:
            #messages.add_message(request, messages.ERROR, MensajeTemporalError. RECHAZO_USUARIO_FALLIDO)

        reservacion_quirofano.estado = 'R'
        reservacion_quirofano.save()

        messages.add_message(request, messages.SUCCESS, MensajeTemporalExito.SOLICITUD_USUARIO_RECHAZADA)
    else:
        messages.add_message(request, messages.ERROR, MensajeTemporalError. RECHAZO_USUARIO_FALLIDO)

    return redirect('solicitudes_quirofanos')

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

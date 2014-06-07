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

from datetime import date, timedelta

from quirofanos_cmsb.helpers.flash_messages import MensajeTemporalError, MensajeTemporalExito, construir_mensaje
from quirofanos_cmsb.helpers.template_text import TextoMostrable
from quirofanos_cmsb.helpers.user_tests import es_coordinador
from quirofanos_cmsb.models import Reservacion

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

    return render_to_response('coordinador/solicitudes_quirofanos.html', datos, context_instance=RequestContext(request))

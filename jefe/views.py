# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.template import RequestContext
from django.contrib import messages
from django.shortcuts import redirect
from django.http import Http404
from datetime import date, timedelta

from quirofanos_cmsb.models import Cuenta
from quirofanos_cmsb.helpers.flash_messages import MensajeTemporalError, MensajeTemporalExito

@require_http_methods(["GET"])
def solicitudes_usuarios(request, estado="pendientes", periodo=1):
    ''' Controlador correspondiente al listado de solicitudes de usuarios

    Parametros:
    request -> Solicitud HTTP '''
    periodo = int(periodo)
    if periodo < 1 or periodo > 3:
        raise Http404

    datos = {}
    fecha_valor = date.today() - timedelta(days=8)
    datos['tipo_busqueda'] = u'Última Semana'
    if (periodo == 2):
        fecha_valor = date.today() - timedelta(days=31)
        datos['tipo_busqueda'] = u'Último Mes'
    elif (periodo == 3):
        fecha_valor = date.today() - timedelta(days=93)
        datos['tipo_busqueda'] = u'Últimos 3 Meses'

    lista_solicitudes_usuario_pendientes = Cuenta.objects.filter(estado='P', usuario__date_joined__gte=fecha_valor).order_by('-usuario__date_joined').exclude(privilegio='0').exclude(privilegio='1')
    lista_solicitudes_usuario_aprobadas = Cuenta.objects.filter(estado='A', usuario__date_joined__gte=fecha_valor).order_by('-usuario__date_joined').exclude(privilegio='0').exclude(privilegio='1')
    lista_solicitudes_usuario_rechazadas = Cuenta.objects.filter(estado='R', usuario__date_joined__gte=fecha_valor).order_by('-usuario__date_joined').exclude(privilegio='0').exclude(privilegio='1')
    numero_solicitudes_pendientes = Cuenta.objects.filter(estado='P').count()

    paginator_pendientes = Paginator(lista_solicitudes_usuario_pendientes, 2)
    page = request.GET.get('page')
    try:
        lista_solicitudes_usuario_pendientes = paginator_pendientes.page(page)
    except PageNotAnInteger:
        lista_solicitudes_usuario_pendientes = paginator_pendientes.page(1)
    except EmptyPage:
        lista_solicitudes_usuario_pendientes = paginator_pendientes.page(paginator_pendientes.num_pages)

    paginator_aprobadas = Paginator(lista_solicitudes_usuario_aprobadas, 2)
    page = request.GET.get('page')
    try:
        lista_solicitudes_usuario_aprobadas = paginator_aprobadas.page(page)
    except PageNotAnInteger:
        lista_solicitudes_usuario_aprobadas = paginator_aprobadas.page(1)
    except EmptyPage:
        lista_solicitudes_usuario_aprobadas = paginator_aprobadas.page(paginator_aprobadas.num_pages)

    paginator_rechazadas = Paginator(lista_solicitudes_usuario_rechazadas, 2)
    page = request.GET.get('page')
    try:
        lista_solicitudes_usuario_rechazadas = paginator_rechazadas.page(page)
    except PageNotAnInteger:
        lista_solicitudes_usuario_rechazadas = paginator_rechazadas.page(1)
    except EmptyPage:
        lista_solicitudes_usuario_rechazadas = paginator_rechazadas.page(paginator_rechazadas.num_pages)

    datos['lista_solicitudes_usuario_pendientes'] = lista_solicitudes_usuario_pendientes
    datos['lista_solicitudes_usuario_aprobadas'] = lista_solicitudes_usuario_aprobadas
    datos['lista_solicitudes_usuario_rechazadas'] = lista_solicitudes_usuario_rechazadas
    datos['numero_solicitudes_pendientes'] = numero_solicitudes_pendientes
    datos['estado_solicitud'] = estado

    return render_to_response('jefe/solicitudes_usuarios.html', datos, context_instance=RequestContext(request))

@require_http_methods(["GET"])
def aceptar_solicitud_usuario(request, id_cuenta):
    ''' Controlador correspondiente a la aprobacion de solicitudes de usuarios

    Parametros:
    request -> Solicitud HTTP '''
    cuenta_usuario = Cuenta.objects.get(id=id_cuenta)
    cuenta_usuario.estado = 'A'
    cuenta_usuario.save()

    messages.add_message(request, messages.SUCCESS, MensajeTemporalExito.SOLICITUD_USUARIO_APROBADA)
    return redirect('solicitudes_usuarios')

@require_http_methods(["GET"])
def rechazar_solicitud_usuario(request, id_cuenta):
    ''' Controlador correspondiente al rechazo de solicitudes de usuarios

    Parametros:
    request -> Solicitud HTTP '''
    cuenta_usuario = Cuenta.objects.get(id=id_cuenta)
    cuenta_usuario.estado = 'R'
    cuenta_usuario.save()

    messages.add_message(request, messages.SUCCESS, MensajeTemporalExito.SOLICITUD_USUARIO_RECHAZADA)
    return redirect('solicitudes_usuarios')

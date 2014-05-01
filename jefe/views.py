# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.template import RequestContext
from django.contrib import messages
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from datetime import date, timedelta
from hashids import Hashids
import uuid

from quirofanos_cmsb.models import Cuenta
from quirofanos_cmsb.helpers.flash_messages import MensajeTemporalError, MensajeTemporalExito, construir_mensaje
from quirofanos_cmsb.helpers.template_text import TextoMostrable
from quirofanos_cmsb.helpers.email import enviar_email
from quirofanos_cmsb.helpers.user_tests import es_jefe
from jefe.forms import GestionarSolicitudUsuarioForm

@require_GET
@login_required
@user_passes_test(es_jefe)
def solicitudes_usuarios(request, estado="pendientes", periodo=1):
    ''' Controlador correspondiente al listado de solicitudes de usuarios

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
    datos['formulario_solicitud_usuario'] = GestionarSolicitudUsuarioForm()

    return render_to_response('jefe/solicitudes_usuarios.html', datos, context_instance=RequestContext(request))

@require_POST
@login_required
@user_passes_test(es_jefe)
def aceptar_solicitud_usuario(request):
    ''' Controlador correspondiente a la aprobacion de solicitudes de usuarios

    Parametros:
    request -> Solicitud HTTP '''
    formulario_solicitud_usuario = GestionarSolicitudUsuarioForm(request.POST)
    if formulario_solicitud_usuario.is_valid():
        id_cuenta = int(formulario_solicitud_usuario.cleaned_data['id_cuenta'])
        try:
            cuenta_usuario = Cuenta.objects.get(id=id_cuenta)
        except ObjectDoesNotExist:
            messages.add_message(request, messages.ERROR, MensajeTemporalError. APROBACION_USUARIO_FALLIDA)

        cuenta_usuario.estado = 'A'
        hashids = Hashids(min_length=5, salt=uuid.uuid1().hex)
        password = hashids.encrypt(cuenta_usuario.id).upper()
        cuenta_usuario.clave_inicial = password
        usuario = cuenta_usuario.usuario
        usuario.is_active = True
        usuario.set_password(password)
        usuario.save()
        cuenta_usuario.save()

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

    return redirect('solicitudes_usuarios')

@require_POST
@login_required
@user_passes_test(es_jefe)
def rechazar_solicitud_usuario(request):
    ''' Controlador correspondiente al rechazo de solicitudes de usuarios

    Parametros:
    request -> Solicitud HTTP '''
    formulario_solicitud_usuario = GestionarSolicitudUsuarioForm(request.POST)
    if formulario_solicitud_usuario.is_valid():
        id_cuenta = int(formulario_solicitud_usuario.cleaned_data['id_cuenta'])
        try:
            cuenta_usuario = Cuenta.objects.get(id=id_cuenta)
        except ObjectDoesNotExist:
            messages.add_message(request, messages.ERROR, MensajeTemporalError. RECHAZO_USUARIO_FALLIDO)

        cuenta_usuario.estado = 'R'
        cuenta_usuario.save()

        messages.add_message(request, messages.SUCCESS, MensajeTemporalExito.SOLICITUD_USUARIO_RECHAZADA)
    else:
        messages.add_message(request, messages.ERROR, MensajeTemporalError. RECHAZO_USUARIO_FALLIDO)

    return redirect('solicitudes_usuarios')

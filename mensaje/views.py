from django.shortcuts import render_to_response, redirect
from datetime import date, time, timedelta, datetime
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template import RequestContext
from quirofanos_cmsb.helpers.template_text import TextoMostrable
from django.contrib.auth.models import User

from quirofanos_cmsb.models import Cuenta, Mensaje
from mensaje.forms import MensajeForm

@require_GET
@login_required
def mis_mensajes(request, pk):
	''' Controlador para listar los mensajes asociados a una cuenta

		Parametros:
		request -> Solicitud Http
		pk -> clave primaria de la cuenta asociada '''

	cuenta = Cuenta.objects.get(id=pk)
	nombre_usuario_login = request.session["nombre_usuario"]
	usuario = User.objects.get(username=nombre_usuario_login)

	if cuenta.usuario.username != usuario.username:
		raise Http404

	mensajes_pendientes = Mensaje.objects.filter(cuenta=cuenta,estado='NL')
	mensajes_leidos = Mensaje.objects.filter(cuenta=cuenta,estado='L')

	mensajes_pendientes_diccionario = []
	for mensaje in mensajes_pendientes:
		mensaje_diccionario = {}
		mensaje_diccionario['objeto'] = mensaje
		mensaje_diccionario['titulo_legible'] = mensaje.get_titulo_display()
		datos_formulario = {}
		datos_formulario['titulo'] = mensaje.get_titulo_display()
		datos_formulario['texto'] = mensaje.texto
		datos_formulario['feha_mensaje'] = mensaje.fecha_mensaje
		mensaje_diccionario['formulario'] = MensajeForm(datos_formulario)
		mensajes_pendientes_diccionario.append(mensaje_diccionario)

	mensajes_leidos_diccionario = []
	for mensaje in mensajes_leidos:
		mensaje_diccionario = {}
		mensaje_diccionario['objeto'] = mensaje
		mensaje_diccionario['titulo_legible'] = mensaje.get_titulo_display()
		datos_formulario = {}
		datos_formulario['titulo'] = mensaje.get_titulo_display()
		datos_formulario['texto'] = mensaje.texto
		datos_formulario['feha_mensaje'] = mensaje.fecha_mensaje
		mensaje_diccionario['formulario'] = MensajeForm(datos_formulario)
		mensajes_leidos_diccionario.append(mensaje_diccionario)

	paginator_pendientes = Paginator(mensajes_pendientes_diccionario, 2)
	page = request.GET.get('page')
	try:
	    mensajes_pendientes_diccionario = paginator_pendientes.page(page)
	except PageNotAnInteger:
	    mensajes_pendientes_diccionario = paginator_pendientes.page(1)
	except EmptyPage:
	    mensajes_pendientes_diccionario = paginator_pendientes.page(paginator_pendientes.num_pages)

	paginator_aprobadas = Paginator(mensajes_leidos_diccionario, 2)
	page = request.GET.get('page')
	try:
	    mensajes_leidos_diccionario = paginator_aprobadas.page(page)
	except PageNotAnInteger:
	    mensajes_leidos_diccionario = paginator_aprobadas.page(1)
	except EmptyPage:
	    mensajes_leidos_diccionario = paginator_aprobadas.page(paginator_aprobadas.num_pages)


	datos = {}
	datos['mensajes_pendientes'] = mensajes_pendientes_diccionario	
	datos['mensajes_leidos'] = mensajes_leidos_diccionario
	datos['numero_mensajes_pendientes'] = mensajes_pendientes.count()
	datos['cuenta_id'] = cuenta.id

	# return redirect('calendario')
	return render_to_response('mensaje/mis_mensajes.html', datos, context_instance=RequestContext(request))

@require_POST
@login_required
def marcar_mensaje(request, pk):
	''' Controlador para marcar mensaje como leido

		Parametros:
		request -> Solicitud Http
		pk -> clave primaria de la cuenta asociada '''

	nombre_usuario_login = request.session["nombre_usuario"]
	usuario = User.objects.get(username=nombre_usuario_login)

	mensaje = Mensaje.objects.get(pk=pk)
	cuenta = mensaje.cuenta

	if cuenta.usuario.username != usuario.username:
		raise Http404

	mensaje.estado = 'L'
	mensaje.save()
	
	return redirect('mis_mensajes', pk=cuenta.id)
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.template import RequestContext
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from hashids import Hashids
import uuid

from quirofanos_cmsb.models import Cuenta, Departamento, Medico
from autenticacion.forms import InicioSesionForm, CambiarContrasenaForm, BusquedaMedicoForm, RegistroMedicoForm, RegistroDepartamentoForm, RecuperarContrasenaForm, BusquedaDepartamentoForm, ActualizarEmailForm
from quirofanos_cmsb.helpers.flash_messages import MensajeTemporalError, MensajeTemporalExito
from quirofanos_cmsb.helpers.email import enviar_email
from quirofanos_cmsb.helpers.utils import obtener_tipo_usuario

@require_GET
def inicio(request):
	''' Controlador correspondiente a la pagina de inicio de la aplicacion

	Parametros:
	request -> Solicitud HTTP '''
	if request.user.is_authenticated():
		return redirect('calendario')

	formulario_inicio_sesion = InicioSesionForm()
	formulario_busqueda_medico = BusquedaMedicoForm()
	formulario_busqueda_departamento = BusquedaDepartamentoForm()
	datos = {}
	datos['formulario_inicio_sesion'] = formulario_inicio_sesion
	datos['formulario_busqueda_medico'] = formulario_busqueda_medico
	datos['formulario_busqueda_departamento'] = formulario_busqueda_departamento
	return render_to_response('autenticacion/inicio.html', datos, context_instance=RequestContext(request))

@require_POST
def busqueda_medico(request):
	''' Controlodar correspondiente a la busqueda de medico por numero de cedula

	Parametros:
	request -> Solicitud HTTP '''
	formulario_busqueda_medico = BusquedaMedicoForm(request.POST)
	datos = {}
	if formulario_busqueda_medico.is_valid():
		cedula_medico = formulario_busqueda_medico.cleaned_data['cedula_medico']
		nacionalidad_medico = formulario_busqueda_medico.cleaned_data['nacionalidad_medico']
		cedula_medico_bd = nacionalidad_medico + cedula_medico
		formulario_registro_medico = RegistroMedicoForm(initial={'cedula_medico': cedula_medico_bd})
		medico = Medico.objects.get(cedula=cedula_medico_bd)
		datos['medico'] = medico
		datos['formulario_registro_medico'] = formulario_registro_medico

	formulario_inicio_sesion = InicioSesionForm()
	formulario_busqueda_departamento = BusquedaDepartamentoForm()
	datos['formulario_inicio_sesion'] = formulario_inicio_sesion
	datos['formulario_busqueda_departamento'] = formulario_busqueda_departamento
	datos['formulario_busqueda_medico'] = formulario_busqueda_medico
	return render_to_response('autenticacion/inicio.html', datos,context_instance=RequestContext(request))

@require_POST
def busqueda_departamento(request):
	''' Controlodar correspondiente a la busqueda de departamento por nombre

	Parametros:
	request -> Solicitud HTTP '''
	formulario_busqueda_departamento = BusquedaDepartamentoForm(request.POST)
	datos = {}
	if formulario_busqueda_departamento.is_valid():
		nombre_departamento = formulario_busqueda_departamento.cleaned_data['nombre_departamento']
		departamento = Departamento.objects.get(nombre=nombre_departamento)
		formulario_registro_departamento = RegistroDepartamentoForm(initial={'nombre_departamento': nombre_departamento})
		datos['departamento'] = departamento
		datos['formulario_registro_departamento'] = formulario_registro_departamento

	formulario_inicio_sesion = InicioSesionForm()
	formulario_busqueda_medico = BusquedaMedicoForm()
	datos['formulario_inicio_sesion'] = formulario_inicio_sesion
	datos['formulario_busqueda_departamento'] = formulario_busqueda_departamento
	datos['formulario_busqueda_medico'] = formulario_busqueda_medico
	return render_to_response('autenticacion/inicio.html', datos,context_instance=RequestContext(request))


@require_POST
def registro_medico(request):
	''' Controlador correspondiente al registro de un medico

	Parametros:
	request -> Solicitud HTTP '''
	formulario_registro_medico = RegistroMedicoForm(request.POST)
	formulario_valido = formulario_registro_medico.is_valid()
	cedula_medico = formulario_registro_medico.cleaned_data['cedula_medico']
	medico = Medico.objects.filter(cedula=cedula_medico)
	if not medico:
		messages.add_message(request, messages.ERROR, MensajeTemporalError.REGISTRO_MEDICO_CEDULA_MODIFICADA)
		return redirect('inicio')

	medico = medico[0]
	if medico.cuenta:
		messages.add_message(request, messages.ERROR, MensajeTemporalError.REGISTRO_MEDICO_CUENTA_EXISTE)
		return redirect('inicio')

	if formulario_valido:
		with transaction.atomic():
			nombre_usuario_medico = formulario_registro_medico.cleaned_data['nombre_usuario_medico']

			usuario = User.objects.create_user(username=nombre_usuario_medico, email=medico.email)
			usuario.is_active = False

			cuenta_medico = Cuenta()
			cuenta_medico.usuario = usuario
			cuenta_medico.estado = 'P'
			cuenta_medico.privilegio = '4'

			usuario.save()
			cuenta_medico.save()
			medico.cuenta = cuenta_medico
			medico.save()

			messages.add_message(request, messages.SUCCESS, MensajeTemporalExito.SOLICITUD_REGISTRO_EXITOSO)
			return redirect('inicio')

	formulario_inicio_sesion = InicioSesionForm()
	formulario_busqueda_medico = BusquedaMedicoForm()
	formulario_busqueda_departamento = BusquedaDepartamentoForm()
	datos = {}
	datos['formulario_registro_medico'] = formulario_registro_medico
	datos['formulario_inicio_sesion'] = formulario_inicio_sesion
	datos['formulario_busqueda_medico'] = formulario_busqueda_medico
	datos['formulario_busqueda_departamento'] = formulario_busqueda_departamento
	datos['medico'] = medico
	return render_to_response('autenticacion/inicio.html', datos,context_instance=RequestContext(request))

@require_POST
def registro_departamento(request):
	''' Controlador correspondiente al registro de un departamento

	Parametros:
	request -> Solicitud HTTP '''
	formulario_registro_departamento = RegistroDepartamentoForm(request.POST)
	formulario_valido = formulario_registro_departamento.is_valid()
	nombre_departamento = formulario_registro_departamento.cleaned_data['nombre_departamento']
	departamento = Departamento.objects.filter(nombre=nombre_departamento)
	if not departamento:
		messages.add_message(request, messages.ERROR, MensajeTemporalError.REGISTRO_DEPARTAMENTO_NOMBRE_MODIFICADO)
		return redirect('inicio')

	departamento = departamento[0]
	if departamento.cuenta:
		messages.add_message(request, messages.ERROR, MensajeTemporalError.REGISTRO_DEPARTAMENTO_CUENTA_EXISTE)
		return redirect('inicio')

	if formulario_valido:
		with transaction.atomic():
			nombre_usuario_departamento = formulario_registro_departamento.cleaned_data['nombre_usuario_departamento']

			usuario = User.objects.create_user(username=nombre_usuario_departamento, email=departamento.email)
			usuario.is_active = False

			cuenta_departamento = Cuenta()
			cuenta_departamento.usuario = usuario
			cuenta_departamento.estado = 'P'
			if nombre_departamento == u'Enfermeras Recuperación':
				cuenta_departamento.privilegio = '3'
			elif nombre_departamento == u'Admisión Emergencia':
				cuenta_departamento.privilegio = '2'
			elif nombre_departamento == u'Admisión Principal':
				cuenta_departamento.privilegio == '5'
			else:
				cuenta_departamento.privilegio = '6'
			usuario.save()
			cuenta_departamento.save()
			departamento.cuenta = cuenta_departamento
			departamento.save()

			messages.add_message(request, messages.SUCCESS, MensajeTemporalExito.SOLICITUD_REGISTRO_EXITOSO)
			return redirect('inicio')

	formulario_inicio_sesion = InicioSesionForm()
	formulario_busqueda_medico = BusquedaMedicoForm()
	formulario_busqueda_departamento = BusquedaDepartamentoForm()
	datos = {}
	datos['formulario_inicio_sesion'] = formulario_inicio_sesion
	datos['formulario_busqueda_medico'] = formulario_busqueda_medico
	datos['formulario_busqueda_departamento'] = formulario_busqueda_departamento
	datos['formulario_registro_departamento'] = formulario_registro_departamento
	datos['departamento'] = departamento
	return render_to_response('autenticacion/inicio.html', datos,context_instance=RequestContext(request))

@require_POST
def iniciar_sesion(request):
	''' Controlador correspondiente al inicio de sesion

	Parametros:
	request -> Solicitud HTTP '''
	formulario_inicio_sesion = InicioSesionForm(request.POST)
	if formulario_inicio_sesion.is_valid():
		nombre_usuario = formulario_inicio_sesion.cleaned_data['nombre_usuario']
		contrasena = formulario_inicio_sesion.cleaned_data['contrasena']
		user = authenticate(username=nombre_usuario, password=contrasena)
		if user:
			cuenta = None
			try:
				cuenta = user.cuenta
			except Cuenta.DoesNotExist:
				messages.add_message(request, messages.ERROR, MensajeTemporalError.AUTENTICACION_FALLIDA)
				return redirect('inicio')
			if user.is_active:
				login(request, user)
				request.session["nombre_usuario"] = user.username
				privilegio = cuenta.privilegio
				if privilegio == "0":
					request.session["privilegio"] = "JEFE_PQ"
					request.session["template_base"] = "jefe/contexto.html"
					request.session["nombre"] = u'Jefe Plan Quirúrgico'
				elif privilegio == "1":
					request.session["privilegio"] = "COORDINADOR_PQ"
					request.session["template_base"] = "coordinador/contexto.html"
					request.session["nombre"] = u'Coordinador Plan Quirúrgico'
				elif privilegio == "2":
					request.session["privilegio"] = "EMERGENCIA_PQ"
					request.session["template_base"] = "contexto.html"
					departamento = cuenta.departamento
					request.session["nombre"] = departamento.nombre
				elif privilegio == "3":
					request.session["privilegio"] = "ASISTENTE_PQ"
					request.session["template_base"] = "contexto.html"
					departamento = cuenta.departamento
					request.session["nombre"] = departamento.nombre
				elif privilegio == "4":
					request.session["privilegio"] = "MEDICO"
					request.session["template_base"] = "medico/contexto.html"
					medico = cuenta.medico
					nombre_medico = medico.nombre
					apellido_medico = medico.apellido
					request.session["nombre"] = nombre_medico + ' ' + apellido_medico
				elif privilegio == "5":
					request.session["privilegio"] = "OBSERVADOR_PRESUPUESTO"
					request.session["template_base"] = "contexto.html"
					departamento = cuenta.departamento
					request.session["nombre"] = departamento.nombre
				elif privilegio == "6":
					request.session["privilegio"] = "OBSERVADOR"
					request.session["template_base"] = "contexto.html"
					departamento = cuenta.departamento
					request.session["nombre"] = departamento.nombre

				return redirect('calendario')
			else:
				messages.add_message(request, messages.ERROR, MensajeTemporalError.AUTENTICACION_USUARIO_INACTIVO)
				return redirect('inicio')
		else:
			messages.add_message(request, messages.ERROR, MensajeTemporalError.AUTENTICACION_FALLIDA)
			return redirect('inicio')
	else:
		messages.add_message(request, messages.ERROR, MensajeTemporalError.AUTENTICACION_CAMPO_VACIO)
		return redirect('inicio')

@require_GET
@login_required
def cerrar_sesion(request):
	''' Controlador correspondiente al cierre de sesion

	Parametros:
	request -> Solicitud HTTP '''
	logout(request)
	return redirect('inicio')

@require_http_methods(["GET", "POST"])
@login_required
def cambiar_contrasena(request):
	''' Controlador correspondiente al cambio de contrasena

	Parametros:
	request -> Solicitud HTTP '''
	datos = {}
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
					messages.add_message(request, messages.SUCCESS, MensajeTemporalExito.CAMBIO_CONTRASENA_EXITOSO)
					return redirect('calendario')
			else:
				messages.add_message(request, messages.ERROR,
					MensajeTemporalError.CAMBIO_CONTRASENA_FALLIDO)
				return redirect('cambiar_contrasena')

	datos["formulario_cambio_contrasena"] = formulario_cambio_contrasena
	return render_to_response('autenticacion/cambiar_contrasena.html', datos, context_instance=RequestContext(request))

@require_http_methods(["GET","POST"])
def recuperar_contrasena(request):
	''' Controlador correspondiente a la recuperacion de contrasena

	Parametros:
	request -> Solicitud HTTP '''
	datos = {}
	if request.method == 'GET':
		formulario_recuperar_contrasena = RecuperarContrasenaForm()
	elif request.method == 'POST':
		formulario_recuperar_contrasena = RecuperarContrasenaForm(request.POST)
		if formulario_recuperar_contrasena.is_valid():
			nombre_usuario = formulario_recuperar_contrasena.cleaned_data['nombre_usuario']
			usuario = User.objects.filter(username=nombre_usuario, is_active=True).first()
			if usuario:
				''' Enviar Email al usuario '''
				tipo_usuario = obtener_tipo_usuario(usuario.cuenta)
				email_usuario = ''

				if tipo_usuario == 'medico':
					if usuario.cuenta.medico.email:
						email_usuario = usuario.cuenta.medico.email
					else:
						messages.add_message(request, messages.ERROR,MensajeTemporalError.RECUPERAR_CONTRASENA_SIN_EMAIL)
						return redirect('recuperar_contrasena')

				elif tipo_usuario == 'departamento':
					if usuario.cuenta.departamento.email:
						email_usuario = usuario.cuenta.departamento.email
					else:
						messages.add_message(request, messages.ERROR,MensajeTemporalError.RECUPERAR_CONTRASENA_SIN_EMAIL)
						return redirect('recuperar_contrasena')
				else:
					if usuario.email:
						email_usuario = usuario.email

				with transaction.atomic():
					hashids = Hashids(min_length=5, salt=uuid.uuid1().hex)
					password = hashids.encrypt(usuario.cuenta.id).upper()
					usuario.cuenta.clave_inicial = password
					usuario.set_password(password)
					usuario.save()
					usuario.cuenta.save()

				enviar_email(asunto='Recuperación de Clave de Acceso.', contenido_texto='Su clave de acceso ha sido recuperada. Su nombre de usuario es: ' + usuario.username + ' y su clave de acceso es: ' + usuario.cuenta.clave_inicial + ' .', contenido_html='', recipiente='mjramos91@gmail.com')

				messages.add_message(request, messages.SUCCESS, MensajeTemporalExito.RECUPERAR_CONTRASENA_EXITOSO)

				return redirect('inicio')
			else:
				messages.add_message(request, messages.ERROR,
					MensajeTemporalError.RECUPERAR_CONTRASENA_FALLIDO)
				return redirect('recuperar_contrasena')

	datos["formulario_recuperar_contrasena"] = formulario_recuperar_contrasena
	return render_to_response('autenticacion/recuperar_contrasena.html', datos, context_instance=RequestContext(request))

@require_http_methods(["GET", "POST"])
@login_required
def cambiar_correo_electronico(request):
	''' Controlador correspondiente al cambio de correo electronico

	Parametros:
	request -> Solicitud HTTP '''
	datos = {}
	tipo_usuario = obtener_tipo_usuario(request.user.cuenta)

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

				messages.add_message(request, messages.SUCCESS,MensajeTemporalExito.ACTUALIZACION_EMAIL_EXITOSO)

				return redirect('calendario')

	datos["formulario_actualizacion_email"] = formulario_actualizacion_email

	return render_to_response('autenticacion/cambiar_correo_electronico.html', datos, context_instance=RequestContext(request))

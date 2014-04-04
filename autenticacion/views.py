# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.template import RequestContext
from django.contrib import messages

from quirofanos_cmsb.models import Cuenta, Departamento, Medico, MedicoTratante
from autenticacion.forms import InicioSesionForm, CambiarContrasenaForm, RegistroMedicoForm, RegistroDepartamentoForm, RecuperarContrasenaForm
from quirofanos_cmsb.helpers.flash_messages import MensajeTemporalError, MensajeTemporalExito

@require_GET
def inicio(request):
	''' Controlador correspondiente a la pagina de inicio de la aplicacion

	Parametros:
	request -> Solicitud HTTP '''
	if request.user.is_authenticated():
		return redirect('calendario')

	formulario_inicio_sesion = InicioSesionForm()
	formulario_registro_departamento = RegistroDepartamentoForm()
	formulario_registro_medico = RegistroMedicoForm()
	datos = {}
	datos['formulario_inicio_sesion'] = formulario_inicio_sesion
	datos['formulario_registro_departamento'] = formulario_registro_departamento
	datos['formulario_registro_medico'] = formulario_registro_medico
	return render_to_response('autenticacion/inicio.html', datos, context_instance=RequestContext(request))


@require_POST
def registro_departamento(request):
	''' Controlador correspondiente al registro de un departamento

	Parametros:
	request -> Solicitud HTTP '''
	formulario_registro_departamento = RegistroDepartamentoForm(request.POST)
	if formulario_registro_departamento.is_valid():
		nombre_departamento = formulario_registro_departamento.cleaned_data['nombre_departamento']
		codigo_telefono = formulario_registro_departamento.cleaned_data['codigo_telefono']
		telefono_departamento = formulario_registro_departamento.cleaned_data['telefono_departamento']
		email_departamento = formulario_registro_departamento.cleaned_data['email_departamento']
		nombre_usuario_departamento = formulario_registro_departamento.cleaned_data['nombre_usuario_departamento']
		contrasena_departamento = formulario_registro_departamento.cleaned_data['contrasena_departamento']
		contrasena_confirmacion = formulario_registro_departamento.cleaned_data['contrasena_confirmacion']

		usuario = User.objects.create_user(nombre_usuario_departamento,email_departamento,contrasena_departamento)
		usuario.is_active = False
		usuario.save()

		cuenta_departamento = Cuenta()
		cuenta_departamento.usuario = usuario
		cuenta_departamento.estado = 'P'
		cuenta_departamento.privilegio = '4'
		cuenta_departamento.save()

		departamento = Departamento()
		departamento.cuenta = cuenta_departamento
		departamento.nombre = nombre_departamento
		departamento.telefono = codigo_telefono + '-' + telefono_departamento
		departamento.save()

		messages.add_message(request, messages.SUCCESS, MensajeTemporalExito.SOLICITUD_REGISTRO_EXITOSO)
		return redirect('inicio')

	formulario_inicio_sesion = InicioSesionForm()
	formulario_registro_medico = RegistroMedicoForm()
	datos = {}
	datos['formulario_registro_departamento'] = formulario_registro_departamento
	datos['formulario_inicio_sesion'] = formulario_inicio_sesion
	datos['formulario_registro_medico'] = formulario_registro_medico
	return render_to_response('autenticacion/inicio.html', datos,context_instance=RequestContext(request))

@require_POST
def registro_medico(request):
	''' Controlador correspondiente al registro de un medico

	Parametros:
	request -> Solicitud HTTP '''
	formulario_registro_medico = RegistroMedicoForm(request.POST)
	if formulario_registro_medico.is_valid():
		nombre_medico = formulario_registro_medico.cleaned_data['nombre_medico']
		apellido_medico = formulario_registro_medico.cleaned_data['apellido_medico']
		nacionalidad_medico = formulario_registro_medico.cleaned_data['nacionalidad_medico']
		cedula_medico = formulario_registro_medico.cleaned_data['cedula_medico']
		especialidad_medico = formulario_registro_medico.cleaned_data['especialidad_medico']
		genero_medico = formulario_registro_medico.cleaned_data['genero_medico']
		codigo_telefono = formulario_registro_medico.cleaned_data['codigo_telefono']
		telefono_medico = formulario_registro_medico.cleaned_data['telefono_medico']
		email_medico = formulario_registro_medico.cleaned_data['email_medico']
		nombre_usuario_medico = formulario_registro_medico.cleaned_data['nombre_usuario_medico']
		contrasena_medico = formulario_registro_medico.cleaned_data['contrasena_medico']
		contrasena_confirmacion = formulario_registro_medico.cleaned_data['contrasena_confirmacion']

		usuario = User.objects.create_user(nombre_usuario_medico,email_medico,contrasena_medico)
		usuario.is_active = False
		usuario.save()

		cuenta_medico = Cuenta()
		cuenta_medico.usuario = usuario
		cuenta_medico.estado = 'P'
		cuenta_medico.privilegio = '3'
		cuenta_medico.save()

		medico = Medico()
		medico.cuenta = cuenta_medico
		medico.nombre = nombre_medico
		medico.apellido = apellido_medico
		medico.cedula = nacionalidad_medico + cedula_medico
		medico.genero = genero_medico
		medico.telefono = codigo_telefono + '-' + telefono_medico
		medico.save()
		medico.especializaciones = especialidad_medico

		for especializacion in especialidad_medico:
			if especializacion.es_quirurgica:
				medico_tratante = MedicoTratante()
				medico_tratante.medico = medico
				medico_tratante.save()
				break

		messages.add_message(request, messages.SUCCESS, MensajeTemporalExito.SOLICITUD_REGISTRO_EXITOSO)
		return redirect('inicio')

	formulario_inicio_sesion = InicioSesionForm()
	formulario_registro_departamento = RegistroDepartamentoForm()
	datos = {}
	datos['formulario_registro_medico'] = formulario_registro_medico
	datos['formulario_inicio_sesion'] = formulario_inicio_sesion
	datos['formulario_registro_departamento'] = formulario_registro_departamento
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
			if user.is_active:
				login(request, user)
				request.session["nombre_usuario"] = request.user.username
				cuenta = request.user.cuenta
				privilegio = request.user.cuenta.privilegio
				if privilegio == "0":
					request.session["privilegio"] = "JEFE_PQ"
					request.session["template_base"] = "jefe/contexto.html"
					request.session["nombre"] = u'jefe Plan Quirúrgico'
				elif privilegio == "1":
					request.session["privilegio"] = "COORDINADOR_PQ"
					request.session["template_base"] = "coordinador/contexto.html"
					request.session["nombre"] = u'Coordinador Plan Quirúrgico'
				elif privilegio == "2":
					request.session["privilegio"] = "ASISTENTE_PQ"
					request.session["template_base"] = "contexto.html"
					request.session["nombre"] = u'Asistente Plan Quirúrgico'
				elif privilegio == "3":
					request.session["privilegio"] = "MEDICO"
					request.session["template_base"] = "medico/contexto.html"
					medico = Medico.objects.select_related().get(cuenta=cuenta)
					nombre_medico = medico.nombre
					apellido_medico = medico.apellido
					request.session["nombre"] = nombre_medico +' '+ apellido_medico
				elif privilegio == "4":
					request.session["privilegio"] = "OBSERVADOR"
					request.session["template_base"] = "contexto.html"
					departamento = Departamento.objects.select_related().get(cuenta=cuenta)
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
			correo_electronico = formulario_recuperar_contrasena.cleaned_data['correo_electronico']
			usuario = User.objects.filter(email=correo_electronico, is_active=True)
			if usuario:
				# Enviar email
				messages.add_message(request, messages.SUCCESS, MensajeTemporalExito.RECUPERAR_CONTRASENA_EXITOSO)
				return redirect('inicio')
			else:
				messages.add_message(request, messages.ERROR,
					MensajeTemporalError.RECUPERAR_CONTRASENA_FALLIDO)
				return redirect('recuperar_contrasena')
	datos["formulario_recuperar_contrasena"] = formulario_recuperar_contrasena
	return render_to_response('autenticacion/recuperar_contrasena.html', datos, context_instance=RequestContext(request))

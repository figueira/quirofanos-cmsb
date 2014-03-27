# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_http_methods
from django.template import RequestContext
from django.contrib import messages

from quirofanos_cmsb.models import Cuenta, Departamento
from autenticacion.forms import InicioSesionForm
from autenticacion.forms import RegistroDepartamentoForm

def inicio(request):
	''' Controlador correspondiente a la pagina de inicio de la aplicacion 

	Parametros:
	request -> Solicitud HTTP '''
	if request.user.is_authenticated():
		return redirect('calendario')

	formulario_inicio_sesion = InicioSesionForm()
	formulario_registro_departamento = RegistroDepartamentoForm()
	datos = {}
	datos['formulario_inicio_sesion'] = formulario_inicio_sesion
	datos['formulario_registro_departamento'] = formulario_registro_departamento
	return render_to_response('autenticacion/inicio.html', datos, context_instance=RequestContext(request))


@require_http_methods(["POST"])
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
		return render_to_response('autenticacion/registro.html') # decidir a donde redireccionar
		else:
			formulario_registro_departamento.errors['contrasena_invalida'] = u'Las contraseñas ingresadas no coinciden.'			

	formulario_inicio_sesion = InicioSesionForm()
	datos = {}
	datos['formulario_registro_departamento'] = formulario_registro_departamento	
	datos['formulario_inicio_sesion'] = formulario_inicio_sesion
	return render_to_response('autenticacion/inicio.html', datos,context_instance=RequestContext(request))

@require_http_methods(["POST"])
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
				return redirect('calendario')
			else:
				messages.add_message(request, messages.ERROR, u'Su cuenta todavía no ha sido aprobada.')
				return redirect('inicio')
		else:
			messages.add_message(request, messages.ERROR, u'Usuario y/o contraseña incorrecta.')
			return redirect('inicio')
	else:
		messages.add_message(request, messages.ERROR, u'Asegúrese de ingresar su nombre de usuario y contraseña.')
		return redirect('inicio')

def cerrar_sesion(request):
	''' Controlador correspondiente al cierre de sesion

	Parametros:
	request -> Solicitud HTTP '''
	logout(request)
	return redirect('inicio')

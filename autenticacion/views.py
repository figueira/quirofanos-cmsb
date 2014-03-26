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

def inicio(request):
	''' Controlador correspondiente a la pagina de inicio de la aplicacion 

	Parametros:
	request -> Solicitud HTTP '''

	if request.user.is_authenticated():
		return redirect('calendario')

	formulario_inicio_sesion = InicioSesionForm()
	datos = {}
	datos['formulario_inicio_sesion'] = formulario_inicio_sesion

	return render_to_response('autenticacion/inicio.html', datos, context_instance=RequestContext(request))


def registro_departamento(request):
	''' Controlador correspondiente al registro de un departamento

	Parametros:
	request -> Solicitud HTTP '''

	nombre = request.POST.get('nombre-departamento')
	codigo = request.POST.get('codigo-telefono')
	telefono = request.POST.get('telefono-departamento')
	email = request.POST.get('email-departamento')
	usuario = request.POST.get('usuario-departamento')
	contrasena = request.POST.get('contrasena-departamento')

	user = User.objects.create_user(usuario,email,contrasena)

	cuenta = Cuenta()
	cuenta.usuario = user
	cuenta.estado = 'P'
	cuenta.privilegio = '4'

	departamento = Departamento()
	departamento.cuenta = cuenta
	departamento.nombre = nombre
	#codigo
	departamento.telefono = telefono

	return render_to_response('autenticacion/registro.html' )

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

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

from quirofanos_cmsb.models import Cuenta
from quirofanos_cmsb.models import Departamento, Medico, Especializacion
from autenticacion.forms import InicioSesionForm
from autenticacion.forms import RegistroDepartamentoForm
from autenticacion.forms import RegistroMedicoForm

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
		if contrasena_departamento == contrasena_confirmacion:
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
			departamento.telefono = codigo_telefono +'-'+ telefono_departamento
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
def registro_medico(request):

	formulario_registro_medico = RegistroMedicoForm(request.POST)
	if formulario_registro_medico.is_valid():
		nombre_medico = formulario_registro_medico.cleaned_data['nombre_medico']
		apellido_medico = formulario_registro_medico.cleaned_data['apellido_medico']
		cedula_medico = formulario_registro_medico.cleaned_data['cedula_medico']
		especialidad_medico = formulario_registro_medico.cleaned_data['especialidad_medico']
		genero_medico = formulario_registro_medico.cleaned_data['genero_medico']
		codigo_telefono = formulario_registro_medico.cleaned_data['codigo_telefono']
		telefono_medico = formulario_registro_medico.cleaned_data['telefono_medico']
		email_medico = formulario_registro_medico.cleaned_data['email_medico']
		nombre_usuario_medico = formulario_registro_medico.cleaned_data['nombre_usuario_medico']
		contrasena_medico = formulario_registro_medico.cleaned_data['contrasena_medico']
		contrasena_confirmacion = formulario_registro_medico.cleaned_data['contrasena_confirmacion']
		if contrasena_medico == contrasena_confirmacion:
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
			medico.nombre = nombre_usuario_medico
			medico.apellido = apellido_medico
			medico.cedula = cedula_medico
			medico.genero = genero_medico
			medico.telefono = codigo_telefono +'-'+ telefono_medico
			#medico.especializaciones = especialidad_medico
			medico.save()	

			return render_to_response('autenticacion/registro.html')		
		else:
			formulario_registro_medico.errors['contrasena_invalida'] = u'Las contraseñas ingresadas no coinciden.'

	formulario_inicio_sesion = InicioSesionForm()
	datos = {}
	datos['formulario_registro_medico'] = formulario_registro_medico	
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

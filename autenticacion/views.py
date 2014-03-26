from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from quirofanos_cmsb.models import Cuenta, Departamento


# Create your views here.

def inicio(request):
	''' Controlador correspondiente a la pagina de inicio de la aplicacion 

	Parametros:
	request -> Solicitud HTTP '''
	c = {}
	c.update(csrf(request))

	return render_to_response('autenticacion/inicio.html', c)


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



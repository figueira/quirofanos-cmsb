from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def solicitudes_usuarios(request):
	''' Controlador correspondiente al listado de solicitudes de usuarios

	Parametros:
	request -> Solicitud HTTP '''

	return render_to_response('gestion_usuarios/solicitudes_usuarios.html')
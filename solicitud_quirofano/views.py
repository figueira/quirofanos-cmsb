from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def solicitud(request):
	 ''' Controlador correspondiente a la pagina del formulario de una nueva solicitud de quirofano

	 Parametros:
	 request -> Solicitud HTTP '''

	 return render_to_response('solicitud_quirofano/solicitud.html')

def mis_solicitudes(request):
	 ''' Controlador correspondiente a la pagina del listado de solicitudes realizadas por el medico

	 Parametros:
	 request -> Solicitud HTTP '''

	 return render_to_response('solicitud_quirofano/mis_solicitudes.html')
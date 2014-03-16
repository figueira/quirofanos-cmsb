from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def solicitud_quirofano(request):
	 ''' Controlador correspondiente a la pagina del formulario de una nueva solicitud de quirofano

	 Parametros:
	 request -> Solicitud HTTP '''

	 return render_to_response('medico/solicitud_quirofano.html')

def mis_solicitudes(request):
	 ''' Controlador correspondiente a la pagina del listado de solicitudes realizadas por el medico

	 Parametros:
	 request -> Solicitud HTTP '''

	 return render_to_response('medico/mis_solicitudes.html')

def proximas_operaciones(request):
	 ''' Controlador correspondiente a la pagina del listado de las proximas operaciones del medico

	 Parametros:
	 request -> Solicitud HTTP '''

	 return render_to_response('medico/proximas_operaciones.html')
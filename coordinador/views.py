from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def solicitudes_quirofano(request):
	''' Controlador correspondiente al listado de solicitudes de quirofano realizadas por medicos

	Parametros:
	request -> Solicitud HTTP '''

	return render_to_response('coordinador/solicitudes_quirofano.html')
from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def inicio(request):
	''' Controlador correspondiente a la pagina de inicio de la aplicacion 

	Parametros:
	request -> Solicitud HTTP '''

	return render_to_response('autenticacion/inicio.html')

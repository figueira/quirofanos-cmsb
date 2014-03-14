from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def solicitud(request):
	 ''' Controlador correspondiente a la pagina de solicitud de quirofanos

	 Parametros:
	 request -> Solicitud HTTP '''

	 return render_to_response('solicitud_quirofano/solicitud.html')
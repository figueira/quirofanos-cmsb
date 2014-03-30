from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

from quirofanos_cmsb.models import Cuenta

def calendario(request):
	''' Controlador correspondiente al calendario de disponibilidad de quirofanos por mes

	Parametros:
	request -> Solicitud HTTP '''
	nombre_usuario = request.user.username
	privilegio = Cuenta.objects.get(usuario=).privilegio

	return render_to_response('plan_quirurgico/calendario.html')

def plan_dia(request):
	''' Controlador correspondiente al detalle del plan quirurgico por dia

	Parametros:
	request -> Solucitud HTTP '''

	return render_to_response('plan_quirurgico/plan_dia.html')

def plan_dia_obs(request):
	''' Controlador correspondiente al detalle del plan quirurgico por dia

	Parametros:
	request -> Solucitud HTTP '''

	return render_to_response('plan_quirurgico/plan_dia_obs.html')

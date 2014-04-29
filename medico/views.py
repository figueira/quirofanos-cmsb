# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext

from quirofanos_cmsb.helpers.user_tests import es_medico

@require_GET
@login_required
@user_passes_test(es_medico)
def solicitud_quirofano(request):
	 ''' Controlador correspondiente a la pagina del formulario de una nueva solicitud de quirofano

	 Parametros:
	 request -> Solicitud HTTP '''

	 return render_to_response('medico/solicitud_quirofano.html', context_instance=RequestContext(request))

@require_GET
@login_required
@user_passes_test(es_medico)
def mis_solicitudes(request):
	 ''' Controlador correspondiente a la pagina del listado de solicitudes realizadas por el medico

	 Parametros:
	 request -> Solicitud HTTP '''

	 return render_to_response('medico/mis_solicitudes.html', context_instance=RequestContext(request))

@require_GET
@login_required
@user_passes_test(es_medico)
def proximas_operaciones(request):
	 ''' Controlador correspondiente a la pagina del listado de las proximas operaciones del medico

	 Parametros:
	 request -> Solicitud HTTP '''

	 return render_to_response('medico/proximas_operaciones.html', context_instance=RequestContext(request))

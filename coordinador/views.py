# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext

from quirofanos_cmsb.helpers.user_tests import es_coordinador

@require_GET
@login_required
@user_passes_test(es_coordinador)
def solicitudes_quirofano(request):
	''' Controlador correspondiente al listado de solicitudes de quirofano realizadas por medicos

	Parametros:
	request -> Solicitud HTTP '''

	return render_to_response('coordinador/solicitudes_quirofano.html', context_instance=RequestContext(request))

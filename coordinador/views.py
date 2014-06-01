# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.db import transaction

from quirofanos_cmsb.helpers.user_tests import es_coordinador
from quirofanos_cmsb.models import IntervencionQuirurgica, Participacion
from quirofanos_cmsb.helpers.flash_messages import MensajeTemporalError, MensajeTemporalAviso

@require_GET
@login_required
@user_passes_test(es_coordinador)
def solicitudes_quirofano(request):
	''' Controlador correspondiente al listado de solicitudes de quirofano realizadas por medicos

	Parametros:
	request -> Solicitud HTTP '''

	return render_to_response('coordinador/solicitudes_quirofano.html', context_instance=RequestContext(request))

@require_POST
@login_required
@user_passes_test(es_coordinador)
def eliminar_intervencion_quirurgica(request, area, ano, mes ,dia, id_intervencion):
    ''' Controlador correspondiente a la eliminacion de una intervencion quirurgica

    Parametros:
    request -> Solicitud HTTP
    id_intervencion -> identificador de la intervencion quirurgica que sera eliminada '''

    try:
        intervencion_quirurgica = IntervencionQuirurgica.objects.get(pk=id_intervencion)
    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, MensajeTemporalError.ELIMINAR_INTERVENCION_QUIRURGICA_INVALIDA)
        return redirect('plan_dia', area, ano, mes, dia)

    with transaction.atomic():
        reservacion = intervencion_quirurgica.reservacion
        lista_procedimientos = intervencion_quirurgica.procedimientoquirurgico_set.all()
        for procedimiento in lista_procedimientos:
            Participacion.objects.filter(procedimiento_quirurgico=procedimiento).delete()
            procedimiento.delete()

            reservacion.delete()

            intervencion_quirurgica.delete()

    messages.add_message(request, messages.WARNING, MensajeTemporalAviso.INTERVENCION_QUIRURGICA_ELIMINADA)
    return redirect('plan_dia', area, ano, mes, dia)











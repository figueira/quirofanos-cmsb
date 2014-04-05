from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST

from quirofanos_cmsb.models import Cuenta

@require_http_methods(["GET","POST"])
def solicitudes_usuarios(request):
    ''' Controlador correspondiente al listado de solicitudes de usuarios

    Parametros:
    request -> Solicitud HTTP '''
    datos = {}
    if request.method == 'GET':
        lista_solicitudes_usuario_pendientes= Cuenta.objects.all().filter(estado='P')
        lista_solicitudes_usuario_aprobadas = Cuenta.objects.all().filter(estado='A')
        lista_solicitudes_usuario_rechazadas = Cuenta.objects.all().filter(estado='R')

        datos['lista_solicitudes_usuario_pendientes'] = lista_solicitudes_usuario_pendientes
        datos['lista_solicitudes_usuario_aprobadas'] = lista_solicitudes_usuario_aprobadas
        datos['lista_solicitudes_usuario_rechazadas'] = lista_solicitudes_usuario_rechazadas

        return render_to_response('jefe/solicitudes_usuarios.html', datos, context_instance=RequestContext(request))

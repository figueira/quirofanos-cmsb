from django.conf.urls import patterns, include, url

urlpatterns = patterns('jefe.views',
    url(r'^solicitudes_usuarios$', 'solicitudes_usuarios', name='solicitudes_usuarios'),
    url(r'^solicitudes_usuarios/(?P<estado>[a-z]+)$', 'solicitudes_usuarios', name='solicitudes_usuarios'),
    url(r'^solicitudes_usuarios/(?P<estado>[a-z]+)/(?P<periodo>\d)$', 'solicitudes_usuarios', name='solicitudes_usuarios'),
    url(r'^aceptar_solicitud_usuario/(?P<id_cuenta>\d+)$', 'aceptar_solicitud_usuario', name='aceptar_solicitud_usuario'),
    url(r'^rechazar_solicitud_usuario/(?P<id_cuenta>\d+)$', 'rechazar_solicitud_usuario', name='rechazar_solicitud_usuario'),
)
from django.conf.urls import patterns, include, url

urlpatterns = patterns('gestion_usuarios.views',
    url(r'^solicitudes_usuarios$', 'solicitudes_usuarios', name='solicitudes_usuarios'),
)
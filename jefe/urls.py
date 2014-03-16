from django.conf.urls import patterns, include, url

urlpatterns = patterns('jefe.views',
    url(r'^solicitudes_usuarios$', 'solicitudes_usuarios', name='solicitudes_usuarios'),
)
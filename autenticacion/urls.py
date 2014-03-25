from django.conf.urls import patterns, include, url

urlpatterns = patterns('autenticacion.views',
    url(r'^$', 'inicio', name='inicio'),
    url(r'^iniciar_sesion$', 'iniciar_sesion', name='iniciar_sesion'),
)
from django.conf.urls import patterns, include, url

urlpatterns = patterns('mensaje.views',
	url(r'^mis_mensajes/(?P<pk>\d+)$', 'mis_mensajes', name='mis_mensajes'),
	url(r'^mis_mensajes/marcar_leido/(?P<pk>\d+)$', 'marcar_mensaje', name='marcar_mensaje'),
)

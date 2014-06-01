from django.conf.urls import patterns, include, url

urlpatterns = patterns('coordinador.views',
    url(r'^solicitudes_quirofano$', 'solicitudes_quirofano', name='solicitudes_quirofano'),
    url(r'^eliminar_intervencion_quirurgica/(?P<area>[A-Z]+)/(?P<ano>\d{4})/(?P<mes>\d{1,2})/(?P<dia>\d{1,2})/(?P<id_intervencion>\d+)$', 'eliminar_intervencion_quirurgica', name='eliminar_intervencion_quirurgica'),
)

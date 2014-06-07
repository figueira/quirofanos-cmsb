from django.conf.urls import patterns, include, url

urlpatterns = patterns('coordinador.views',
    url(r'^solicitudes_quirofano$', 'solicitudes_quirofano', name='solicitudes_quirofano'),
    url(r'^eliminar_intervencion_quirurgica/(?P<area>[A-Z]+)/(?P<ano>\d{4})/(?P<mes>\d{1,2})/(?P<dia>\d{1,2})/(?P<id_intervencion>\d+)$', 'eliminar_intervencion_quirurgica', name='eliminar_intervencion_quirurgica'),
    url(r'^cambiar_horario_intervencion_quirurgica/(?P<id_intervencion>\d+)/(?P<area>[A-Z]+)/(?P<ano>\d{4})/(?P<mes>\d{1,2})/(?P<dia>\d{1,2})/(?P<id_quirofano>\d+)/(?P<hora_inicio>\d{1,2}[.]([5]|[0]))/(?P<duracion_en_medias_horas>\d+)$', 'cambiar_horario_intervencion_quirurgica', name='cambiar_horario_intervencion_quirurgica'),
)

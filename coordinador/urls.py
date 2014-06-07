from django.conf.urls import patterns, include, url

urlpatterns = patterns('coordinador.views',
    url(r'^solicitudes_quirofanos$', 'solicitudes_quirofanos', name='solicitudes_quirofanos'),
    url(r'^solicitudes_quirofanos/(?P<estado>[a-z]+)$', 'solicitudes_quirofanos', name='solicitudes_quirofanos'),
    url(r'^solicitudes_quirofanos/(?P<estado>[a-z]+)/(?P<periodo>\d)$', 'solicitudes_quirofanos', name='solicitudes_quirofanos'),
    url(r'^aceptar_solicitud_quirofano$', 'aceptar_solicitud_quirofano', name='aceptar_solicitud_quirofano'),
    url(r'^rechazar_solicitud_quirofano$', 'rechazar_solicitud_quirofano', name='rechazar_solicitud_quirofano'),
    url(r'^eliminar_intervencion_quirurgica/(?P<area>[A-Z]+)/(?P<ano>\d{4})/(?P<mes>\d{1,2})/(?P<dia>\d{1,2})/(?P<id_intervencion>\d+)$', 'eliminar_intervencion_quirurgica', name='eliminar_intervencion_quirurgica'),
    url(r'^cambiar_horario_intervencion_quirurgica/(?P<id_intervencion>\d+)/(?P<area>[A-Z]+)/(?P<ano>\d{4})/(?P<mes>\d{1,2})/(?P<dia>\d{1,2})/(?P<id_quirofano>\d+)/(?P<hora_inicio>\d{1,2}[.]([5]|[0]))/(?P<duracion_en_medias_horas>\d+)$', 'cambiar_horario_intervencion_quirurgica', name='cambiar_horario_intervencion_quirurgica'),
)

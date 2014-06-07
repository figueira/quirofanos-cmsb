from django.conf.urls import patterns, include, url

urlpatterns = patterns('coordinador.views',
    url(r'^solicitudes_quirofanos$', 'solicitudes_quirofanos', name='solicitudes_quirofanos'),
    url(r'^solicitudes_quirofanos/(?P<estado>[a-z]+)$', 'solicitudes_quirofanos', name='solicitudes_quirofanos'),
    url(r'^solicitudes_quirofanos/(?P<estado>[a-z]+)/(?P<periodo>\d)$', 'solicitudes_quirofanos', name='solicitudes_quirofanos'),
    url(r'^aceptar_solicitud_quirofano$', 'aceptar_solicitud_quirofano', name='aceptar_solicitud_quirofano'),
    url(r'^rechazar_solicitud_quirofano$', 'rechazar_solicitud_quirofano', name='rechazar_solicitud_quirofano'),
)

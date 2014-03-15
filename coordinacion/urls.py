from django.conf.urls import patterns, include, url

urlpatterns = patterns('coordinacion.views',
    url(r'^solicitudes_quirofano$', 'solicitudes_quirofano', name='solicitudes_quirofano'),
)


from django.conf.urls import patterns, include, url

urlpatterns = patterns('medico.views',
    url(r'^solicitud_quirofano$', 'solicitud_quirofano', name='solicitud_quirofano'),
    url(r'^mis_solicitudes$', 'mis_solicitudes', name='mis_solicitudes'),
    url(r'^proximas_operaciones$', 'proximas_operaciones', name='proximas_operaciones'),
)
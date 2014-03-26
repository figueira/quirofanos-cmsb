from django.conf.urls import patterns, include, url

urlpatterns = patterns('autenticacion.views',
    url(r'^$', 'inicio', name='inicio'),
    url(r'^registro_departamento/$', 'registro_departamento', name='registro_departamento')
)
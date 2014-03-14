from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('autenticacion.urls')),
    url(r'^plan_quirurgico/', include('plan_quirurgico.urls')),
    url(r'^solicitud_quirofano/', include('solicitud_quirofano.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns('',
    url(r'^', include('autenticacion.urls')),
    url(r'^plan_quirurgico/', include('plan_quirurgico.urls')),
    url(r'^medico/', include('medico.urls')),
    url(r'^coordinador/', include('coordinador.urls')),
    url(r'^jefe/', include('jefe.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)

urlpatterns += staticfiles_urlpatterns()

from django.conf.urls import patterns, include, url

urlpatterns = patterns('plan_quirurgico.views',
    url(r'^calendario$', 'calendario', name='calendario'),
    url(r'^calendario/(?P<area_actual>[A-Z]+)/(?P<ano>\d{4})/(?P<mes>\d{1,2})$', 'calendario', name='calendario'),
    url(r'^plan_dia/(?P<area>[A-Z]+)/(?P<ano>\d{4})/(?P<mes>\d{1,2})/(?P<dia>\d{1,2})$', 'plan_dia', name='plan_dia'),
    url(r'^plan_dia_obs/(?P<area>[A-Z]+)/(?P<ano>\d{4})/(?P<mes>\d{1,2})/(?P<dia>\d{1,2})$', 'plan_dia_obs', name='plan_dia_obs'),
)

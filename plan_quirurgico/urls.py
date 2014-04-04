from django.conf.urls import patterns, include, url

urlpatterns = patterns('plan_quirurgico.views',
    url(r'^calendario$', 'calendario', name='calendario'),
    url(r'^calendario/(?P<ano>\d{4})/(?P<mes>\d{1,2})$', 'calendario', name='calendario'),
    url(r'^plan_dia$', 'plan_dia', name='plan_dia'),
    url(r'^plan_dia_obs$', 'plan_dia_obs', name='plan_dia_obs'),
)

from django.conf.urls import patterns, include, url

urlpatterns = patterns('autenticacion.views',
	url(r'^$', 'inicio', name='inicio'),
    url(r'^busqueda_medico$', 'busqueda_medico', name='busqueda_medico'),
    url(r'^busqueda_departamento$', 'busqueda_departamento', name='busqueda_departamento'),
	url(r'^registro_departamento$', 'registro_departamento', name='registro_departamento'),
	url(r'^registro_medico$', 'registro_medico', name='registro_medico'),
	url(r'^iniciar_sesion$', 'iniciar_sesion', name='iniciar_sesion'),
	url(r'^cerrar_sesion$', 'cerrar_sesion', name='cerrar_sesion'),
	url(r'^cambiar_contrasena$', 'cambiar_contrasena', name='cambiar_contrasena'),
    url(r'^recuperar_contrasena$', 'recuperar_contrasena', name ='recuperar_contrasena'),
    url(r'^cambiar_correo_electronico$', 'cambiar_correo_electronico', name='cambiar_correo_electronico'),
)

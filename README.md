Aplicación para la Gestión de Quirófanos del Centro Médico de Caracas
=====================================================================

Aplicación web, desarrollada con la utilización del framework Django, para la gestión de solicitudes de quirófanos del _Centro Médico de Caracas, Venezuela_.

Estructura del Repositorio
--------------------------

- __autenticacion__ controladores y vistas correspondientes a las funcionalidades de autenticación de la aplicación.

- __coordinador__ controladores y vistas correspondientes a las funcionalidades llevadas a cabo por el coordinador de plan quirúrgico de la clínica.

- __jefe__ controladores y vistas correspondientes a las funcionalidades llevadas a cabo por el jefe de plan quirúrgico de la clínica.

- __medico__ controladores y vistas correspondientes a las funcionalidades llevadas a cabo por los médicos usuarios de la aplicación.

- __plan_quirurgico__ controladores y vistas correspondientes a cada una de las funcionalidades correspondientes al despliegue del plan quirúrgico en la aplicación.

- __mensaje__ controladores y vistas correspondientes a las funcionalidades correspondientes a las notificaciones generadas por la aplicación.

- __quirofanos_cmsb__ módulo principal de la aplicación en Django. Aquí se definen parámetros de configuración, el modelo general de datos, módulos de utilidad, entre otros.

- __static__ carpeta que contiene archivos estáticos utilizados por cada uno de los componenetes de la aplicación. Tales como archivos __CSS__, __Javascript__ e __Imágenes__.

- __templates__ carpeta que contiene plantillas __HTML__ que definen la estructura general de la interfaz de usuario de la aplicación.

- __docs__ carpeta que contiene la documentación de la aplicación.

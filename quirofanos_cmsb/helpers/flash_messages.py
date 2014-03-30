# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _

class MensajeTemporalExito():
    SOLICITUD_REGISTRO_EXITOSO = _(u'Su solicitud de registro ha sido enviada. En los próximos días recibirá un correo y/o una llamada telefónica indicándole si su cuenta ha sido aprobada.')
    CAMBIO_CONTRASENA_EXITOSO = _(u'Su contraseña ha sido actualizada exitosamente.')

class MensajeTemporalError():
    AUTENTICACION_FALLIDA = _(u'Usuario y/o contraseña incorrecta.')
    AUTENTICACION_USUARIO_INACTIVO = _(u'Su cuenta todavía no ha sido aprobada.')
    AUTENTICACION_CAMPO_VACIO = _(u'Por favor ingrese su nombre de usuario y contraseña.')
    CAMBIO_CONTRASENA_FALLIDO = _(u'La contraseña actual ingresada no es correcta.')

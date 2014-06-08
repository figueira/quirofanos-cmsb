# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _

def construir_mensaje(mensaje, extra):
    return mensaje + ' ' + extra + '.'

class MensajeTemporalExito():
    ''' Clase que contiene constantes para ser utilizadas como mensajes temporales (flash messages) de exito '''
    SOLICITUD_REGISTRO_EXITOSO = _(u'Su solicitud de cuenta ha sido enviada. De ser aprobada, en los próximos días recibirá un correo y/o una llamada telefónica indicándole su contraseña de ingreso.')
    CAMBIO_CONTRASENA_EXITOSO = _(u'Su contraseña ha sido actualizada exitosamente.')
    RECUPERAR_CONTRASENA_EXITOSO = _(u'Se le ha enviado un correo electrónico con instrucciones para recuperar sus credenciales.')
    SOLICITUD_USUARIO_APROBADA = _(u'La solicitud de registro de usuario ha sido aprobada.')
    ACTUALIZACION_EMAIL_EXITOSO = _(u'Su correo electrónico ha sido actualizado exitosamente.')
    SOLICITUD_QUIROFANO_ENVIADA = _(u'Su solicitud de quirofano ha sido enviada. Se le notificará cuando ésta haya sido aprobada o, en su defecto, rechazada.')
    INTERVENCION_QUIRURGICA_AGREGADA = _(u'Intervención quirúrgica agregada exitosamente.')
    INTERVENCION_QUIRURGICA_HORARIO_CAMBIADO = _(u'Se ha cambiado exitosamente el turno de la intervención quirúrgica.')
    SOLICITUD_QUIROFANO_APROBADA = _(u'La solicitud de quirófano ha sido aprobada.')

class MensajeTemporalError():
    ''' Clase que contiene constantes para ser utilizadas como mensajes temporales (flash messages) de errores '''
    AUTENTICACION_FALLIDA = _(u'Usuario y/o contraseña incorrecta.')
    AUTENTICACION_USUARIO_INACTIVO = _(u'Su cuenta todavía no ha sido aprobada.')
    AUTENTICACION_CAMPO_VACIO = _(u'Por favor ingrese su nombre de usuario y contraseña.')
    CAMBIO_CONTRASENA_FALLIDO = _(u'La contraseña actual ingresada no es correcta.')
    RECUPERAR_CONTRASENA_FALLIDO = _(u'No existe un usuario registrado en el sistema con el nombre de usuario ingresado. Por Favor comuníquese con el administrador del sistema en caso de haber olvidado su nombre de usuario.')
    REGISTRO_MEDICO_CEDULA_MODIFICADA = _(u'Se intentó solicitar una cuenta para una cédula que no corresponde a ningún médico.')
    REGISTRO_DEPARTAMENTO_NOMBRE_MODIFICADO = _(u'Se intentó solicitar una cuenta para un departamento inexistente.')
    REGISTRO_MEDICO_CUENTA_EXISTE = _(u'Se intentó solicitar una cuenta para un médico que ya ha solicitado su cuenta.')
    REGISTRO_DEPARTAMENTO_CUENTA_EXISTE = _(u'Se intentó solicitar una cuenta para un departamento que ya ha solicitado su cuenta.')
    APROBACION_USUARIO_FALLIDA = _(u'Se intentó aprobar una cuenta de usuario no existente.')
    CANCELACION_SOLICITUD_FALLIDA = _(u'Se intentó cancelar una solicitud que no existe.')
    CANCELACION_INTERVENCION_FALLIDA = _(u'Se intentó cancelar una intervención quirúrgica que no existe.')
    RECHAZO_USUARIO_FALLIDO = _(u'Se intentó rechazar una cuenta de usuario no existente.')
    TIPO_PROCEDIMIENTO_QUIRURGICO_INVALIDO = _(u'Se intentó agregar un procedimiento quirúrgico inválido.')
    NO_SE_AGREGO_PROCEDIMIENTO_QUIRURGICO = _(u'Debe agregar al menos un (1) procedimiento quirúrgico.')
    RECUPERAR_CONTRASENA_SIN_EMAIL = _(u'No posee un correo electrónico asociado a esta cuenta. Por Favor comuníquese con el administrador del sistema para la recuperación de su clave de acceso.')
    ELIMINAR_PROCEDIMIENTO_QUIRURGICO_INVALIDO = _(u'Se intentó eliminar un procedimiento quirúrgico inválido.')
    ELIMINAR_INTERVENCION_QUIRURGICA_INVALIDA = _(u'Se intentó eliminar una intervencion quirúrgica inválida.')
    PROBLEMA_GENERANDO_PDF = _(u'Se ha producido un error al generar el archivo PDF.')
    APROBACION_QUIROFANO_FALLIDA = _(u'Se intentó aprobar la reservación de un quirófano no existente.')
    RECHAZO_QUIROFANO_FALLIDO = _(u'Se intentó rechazar la reservación de un quirófano no existente.')

class MensajeTemporalAviso():
    ''' Clase que contiene constantes para ser utilizadas como mensajes temporales (flash messages) de avisos (warnings) '''
    SOLICITUD_QUIROFANO_CANCELADA = _(u'La solicitud de quirófano ha sido cancelada.')
    INTERVENCION_QUIRURGICA_ELIMINADA = _(u'La intervención quirúrgica ha sido eliminada.')
    SOLICITUD_USUARIO_RECHAZADA = _(u'La solicitud de registro de usuario ha sido rechazada.')
    SOLICITUD_QUIROFANO_RECHAZADA = _(u'La solicitud de quirófano ha sido rechazada.')
    INTERVENCION_CANCELADA = _(u'La intervención quirúrgica ha sido cancelada.')

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
    SOLICITUD_USUARIO_RECHAZADA = _(u'La solicitud de registro de usuario ha sido rechazada.')


class MensajeTemporalError():
    ''' Clase que contiene constantes para ser utilizadas como mensajes temporales (flash messages) de errores '''
    AUTENTICACION_FALLIDA = _(u'Usuario y/o contraseña incorrecta.')
    AUTENTICACION_USUARIO_INACTIVO = _(u'Su cuenta todavía no ha sido aprobada.')
    AUTENTICACION_CAMPO_VACIO = _(u'Por favor ingrese su nombre de usuario y contraseña.')
    CAMBIO_CONTRASENA_FALLIDO = _(u'La contraseña actual ingresada no es correcta.')
    RECUPERAR_CONTRASENA_FALLIDO = _(u'El correo electrónico ingresado no está registrado.')
    REGISTRO_MEDICO_CEDULA_MODIFICADA = _(u'Se intentó solicitar una cuenta para una cédula que no corresponde a ningún médico.')
    REGISTRO_DEPARTAMENTO_NOMBRE_MODIFICADO = _(u'Se intentó solicitar una cuenta para un departamento inexistente.')
    REGISTRO_MEDICO_CUENTA_EXISTE = _(u'Se intentó solicitar una cuenta para un médico que ya ha solicitado su cuenta.')
    REGISTRO_DEPARTAMENTO_CUENTA_EXISTE = _(u'Se intentó solicitar una cuenta para un departamento que ya ha solicitado su cuenta.')
    APROBACION_USUARIO_FALLIDA = _(u'Se intentó aprobar una cuenta de usuario no existente.')
    RECHAZO_USUARIO_FALLIDO = _(u'Se intentó rechazar una cuenta de usuario no existente.')
    TIPO_PROCEDIMIENTO_QUIRURGICO_INVALIDO = _(u'Se intentó agregar un procedimiento quirúrgico inválido.')

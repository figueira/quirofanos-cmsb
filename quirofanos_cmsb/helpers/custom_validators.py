# -*- coding: utf-8 -*-
import re


class ExpresionRegular():

    ''' Constantes que contienen expresiones regulares a ser utilizadas en validaciones de modelos y formularios '''
    CODIGO_TELEFONO = re.compile(r'^\d{4}$', re.UNICODE)
    NUMERO_TELEFONO = re.compile(r'^\d{7}$', re.UNICODE)
    NOMBRE_GENERAL = re.compile(r'^(\s|[^\W0-9_])*$', re.UNICODE)
    CEDULA_BD = re.compile(r'^(V-|E-)\d+$', re.UNICODE)
    TELEFONO_BD = re.compile(r'^\d{4}-\d{7}$', re.UNICODE)


class MensajeError():

    ''' Constantes que contienen mensajes de error a ser utilizados en validaciones de modelos y formularios '''
    CODIGO_TELEFONO_INVALIDO = _(
        u'Código de teléfono inválido, debe contener exactamente 4 dígitos.')
    NUMERO_TELEFONO_INVALIDO = _(
        u'Número de teléfono inválido, debe contener exactamente 7 dígitos.')
    NOMBRE_GENERAL_INVALIDO = _(
        u'Nombre inválido, puede contener sólo letras y espacios.')
    CONTRASENAS_NO_COINCIDEN = _(u'Las contraseñas ingresadas no coinciden.')
    CEDULA_BD_INVALIDA = _(
        u'Cédula inválida, debe ser de la forma: V-XXX... ó E-XXX...')
    TELEFONO_BD_INVALIDO = _(
        u'Teléfono inválido, debe ser de la forma: XXXX-XXXXXXX.')
    RIESGO_BD_MALO_SIN_RAZON = _(
        u'La razón del riesgo no puede ser nula si el riesgo es malo.')
    RIESGO_BD_NO_MALO_CON_RAZON = _(
        u'La razón del riesgo debe ser nula si el riesgo es distinto de malo.')
    HORA_FIN_MENOR_HORA_INICIO = _(
        u'La hora de fin debe ser mayor que la hora de inicio.')


class CodigoError():

    ''' Constantes que contienen codigos de error a ser utilizados en validaciones de modelos y formularios '''
    CODIGO_TELEFONO_INVALIDO = "codigo_telefono_invalido"
    NUMERO_TELEFONO_INVALIDO = "numero_telefono_invalido"
    NOMBRE_GENERAL_INVALIDO = "nombre_general_invalido"
    CONTRASENAS_NO_COINCIDEN = "contrasenas_no_coinciden"
    CEDULA_BD_INVALIDA = "cedula_bd_invalida"
    TELEFONO_BD_INVALIDO = "telefono_bd_invalido"
    RIESGO_BD_MALO_SIN_RAZON = "riesgo_bd_malo_sin_razon"
    RIESGO_BD_NO_MALO_CON_RAZON = "riesgo_bd_no_malo_con_razon"
    HORA_FIN_MENOR_HORA_INICIO = "hora_fin_menor_hora_inicio"

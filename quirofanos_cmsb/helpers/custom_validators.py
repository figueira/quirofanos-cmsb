# -*- coding: utf-8 -*-
import re


class ExpresionRegular():

    ''' Constantes que contienen expresiones regulares a ser utilizadas en validaciones de modelos y formularios '''
    CODIGO_TELEFONO = re.compile(r'^\d{4}$')
    NUMERO_TELEFONO = re.compile(r'^\d{7}$')


class MensajeError():

    ''' Constantes que contienen mensajes de error a ser utilizados en validaciones de modelos y formularios '''
    CODIGO_TELEFONO_INVALIDO = u'Código de teléfono inválido, debe contener exactamente 4 dígitos.'
    NUMERO_TELEFONO_INVALIDO = u'Número de teléfono inválido, debe contener exactamente 7 dígitos.'


class CodigoError():

    ''' Constantes que contienen codigos de error a ser utilizados en validaciones de modelos y formularios '''
    CODIGO_TELEFONO_INVALIDO = "codigo_telefono_invalido"
    NUMERO_TELEFONO_INVALIDO = "numero_telefono_invalido"

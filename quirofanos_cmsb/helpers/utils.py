from quirofanos_cmsb.helpers.template_text import TextoMostrable

def obtener_nombre_mes(mes):
    ''' Devuelve el nombre de un mes expresado como numero

    Parametros:
    mes -> Numero del mes '''
    return {
    1: 'Enero',
    2: 'Febrero',
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre',
    }[mes]

def rango_decimal(comienzo, final, paso):
    r = comienzo
    while r < final:
        yield r
        r = r + paso

def obtener_representacion_media_hora(media_hora):
    ''' Devuelve una representacion legible de una media hora del dia

    Parametros:
    media_hora -> Media hora del dia '''
    return {
    7: TextoMostrable.SIETE_AM,
    7.5: TextoMostrable.SIETE_MEDIA_AM,
    8: TextoMostrable.OCHO_AM,
    8.5: TextoMostrable.OCHO_MEDIA_AM,
    9: TextoMostrable.NUEVE_AM,
    9.5: TextoMostrable.NUEVE_MEDIA_AM,
    10: TextoMostrable.DIEZ_AM,
    10.5: TextoMostrable.DIEZ_MEDIA_AM,
    11: TextoMostrable.ONCE_AM,
    11.5: TextoMostrable.ONCE_MEDIA_AM,
    12: TextoMostrable.DOCE_PM,
    12.5: TextoMostrable.DOCE_MEDIA_PM,
    13: TextoMostrable.TRECE_PM,
    13.5: TextoMostrable.TRECE_MEDIA_PM,
    14: TextoMostrable.CATORCE_PM,
    14.5: TextoMostrable.CATORCE_MEDIA_PM,
    15: TextoMostrable.QUINCE_PM,
    15.5: TextoMostrable.QUINCE_MEDIA_PM,
    16: TextoMostrable.DIECISEIS_PM,
    16.5: TextoMostrable.DIECISEIS_MEDIA_PM,
    17: TextoMostrable.DIECISIETE_PM,
    17.5: TextoMostrable.DIECISIETE_MEDIA_PM,
    18: TextoMostrable.DIECIOCHO_PM,
    18.5: TextoMostrable.DIECIOCHO_MEDIA_PM,
    19: TextoMostrable.DIECINUEVE_PM,
    }[media_hora]

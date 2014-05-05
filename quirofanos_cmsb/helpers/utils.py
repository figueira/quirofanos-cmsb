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
    ''' Devuelve un rango de numeros decimales

    Parametros:
    comienzo -> Numero inicial
    fianl -> Numero final
    paso -> Paso entre cada numero '''
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

def obtener_medias_horas():
    ''' Devuelve una lista de todas las medias horas posibles '''
    return [x for x in rango_decimal(7.0, 19.5, 0.5)]

def obtener_turnos_disponibles(duracion_en_medias_horas,medias_horas_no_disponibles, turnos_disponibles, turnos_atravesados):
    ''' Rellena una lista de turnos_disponibles a partir de los cuales puede comenzar una intervencion quirurgica segun la duracion dada en cantidad de medias horas, ademas rellena una lista de turnos atravesados a partir de los cuales no puede comenzar la intervencion quirurgica

    Parametros:
    duracion_en_medias_horas -> Duracion de la intervencion quirurgica en cantidad de medias horas
    medias_horas_no_disponibles -> Lista de las medias horas ocupadas por intervenciones quirurgicas
    turnos_disponibles -> Lista de turnos disponibles que sera rellenada
    turnos_atravesados -> Lista de turnos atravesados que sera rellenada '''
    medias_horas = obtener_medias_horas()
    medias_horas_disponibles = list(set(medias_horas).difference(set(medias_horas_no_disponibles)))
    medias_horas_disponibles.sort()
    indices_por_saltar = 0
    for i in range(0, len(medias_horas_disponibles)):
        disponible = True
        if indices_por_saltar > 0:
            indices_por_saltar = indices_por_saltar - 1
            continue

        for j in range(1, duracion_en_medias_horas):
            if (i + j >= len(medias_horas_disponibles)) or not (medias_horas_disponibles[i+j] == medias_horas_disponibles[i] + j*0.5):
                disponible = False
                break

        if disponible:
            turnos_disponibles.append(medias_horas_disponibles[i])
            indices_por_saltar = duracion_en_medias_horas - 1
        else:
            turnos_atravesados.append(medias_horas_disponibles[i])

def obtener_tipo_usuario(cuenta):
    ''' Devuelve el tipo de usuario de una cuenta determinada

    Parametros:
    cuenta -> cuenta del usuario '''
    tipo_usuario = ''
    if (cuenta.privilegio == "0"):
        tipo_usuario = 'jefepq'
    elif (cuenta.privilegio == "1"):
        tipo_usuario = 'coordinadorpq'
    elif (cuenta.privilegio == "4"):
        tipo_usuario = 'medico'
    else:
        tipo_usuario = 'departamento'

    return tipo_usuario

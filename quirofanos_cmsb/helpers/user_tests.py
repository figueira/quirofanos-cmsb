def es_jefe(user):
    ''' Devuelve un booleano que indica si el usuario tiene privilegio de JEFE_PQ o no

    Parametros:
    user -> usuario que hace la solicitud http '''
    return user.cuenta.privilegio == '0'

def es_coordinador(user):
    ''' Devuelve un booleano que indica si el usuario tiene privilegio de COORDINADOR_PQ o no

    Parametros:
    user -> usuario que hace la solicitud http '''
    return user.cuenta.privilegio == '1' or user.cuenta.privilegio == '0'

def es_medico(user):
    ''' Devuelve un booleano que indica si el usuario tiene privilegio de MEDICO o no

    Parametros:
    user -> usuario que hace la solicitud http '''
    return user.cuenta.privilegio == '4'

def es_medico_o_coordinador(user):
    ''' Devuelve un booleano que indica si el usuario tiene privilegio de COORDINADOR o MEDICO

    Parametros
    user -> usuario que hace la solicitud http '''
    return es_medico(user) or es_coordinador(user)

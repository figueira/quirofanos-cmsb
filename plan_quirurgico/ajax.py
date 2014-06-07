from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

from datetime import datetime

@dajaxice_register
def obtener_hora_actual(request):
    ''' Funcion ajax para calcular la hora actual. Devuelve la hora actual a traves de JSON

    Parametros:
    request -> Solicitud HTTP '''
    hora_actual = datetime.now().time().strftime("%H:%M:%S")
    return simplejson.dumps({'hora_actual': hora_actual})

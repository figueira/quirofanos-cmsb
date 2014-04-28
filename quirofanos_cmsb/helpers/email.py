from django.core import mail
connection = mail.get_connection()

def enviar_email(asunto, contenido_texto, contenido_html, recipiente):
    ''' Envia un correo electronico

    Parametros:
    asunto -> asunto del correo electronico
    contenido_texto -> contenido del correo electronico en texto plano
    contenido_html -> contenido del correo electronico en html (opcional)
    recipiente -> email recipiente del correo '''
    connection.open()
    email = mail.EmailMultiAlternatives(asunto, contenido_texto, [recipiente])
    if contenido_html != '':
        email.attach_alternative(contenido_html, "text/html")
    email.send(fail_silently=False)
    connection.close()

class ContenidoEmailTexto():
    ''' Clase que contiene constantes para ser utilizadas como contenido en texto plano de correos electronicos '''

class ContenidoEmailHTML():
    ''' Clase que contiene constantes para ser utilizadas como contenido en html de correos electronicos '''

class AsuntoEmail():
    ''' Clase que contiene constantes para ser utilizadas como asuntos de correos electronicos '''

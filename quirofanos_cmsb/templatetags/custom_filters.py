from django import template
register = template.Library()

@register.filter
def valor_clave(diccionario, clave):
    return diccionario[clave]

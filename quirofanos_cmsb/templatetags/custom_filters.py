from django import template
register = template.Library()

@register.filter
def valor_clave(diccionario, clave):
    return diccionario[clave]

@register.filter
def ocurrencias(lista, valor):
    return lista.count(valor)

@register.filter
def remover_primeros_caracteres(palabra, cantidad):
    return palabra[cantidad:]

@register.filter
def escoger_primeros_caracteres(palabra, cantidad):
    return [:cantidad]

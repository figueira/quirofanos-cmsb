from django import forms

class InicioSesionForm(forms.Form):
    nombre_usuario = forms.CharField(max_length=30)
    contrasena = forms.CharField(widget=forms.PasswordInput)
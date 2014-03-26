from django import forms

class InicioSesionForm(forms.Form):
    nombre_usuario = forms.CharField(max_length=30)
    contrasena = forms.CharField(widget=forms.PasswordInput)

class RegistroDepartamentoForm(forms.Form):
	nombre_departamento = forms.CharField(max_length=20)
	codigo_telefono = forms.CharField(max_length=4, min_length=4)
	telefono_departamento = forms.CharField(max_length=7, min_length=7)
	email_departamento = forms.EmailField(max_length=75)
	nombre_usuario_departamento = forms.CharField(max_length=30)
	contrasena_departamento = forms.CharField(widget=forms.PasswordInput)
	contrasena_confirmacion = forms.CharField(widget=forms.PasswordInput)
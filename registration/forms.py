from django import forms

# Create your forms here.

class LoginForm(forms.Form):
    email = forms.CharField(label='Correo electrónico:', max_length=100)
    password = forms.CharField(label='Contraseña:', max_length=100)
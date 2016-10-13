from django import forms

class loginForm(forms.Form):
    nombre=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    tipo=forms.CharField()

from django import forms

class loginForm(forms.Form):
    user=forms.CharField()
    password=forms.CharField()
    tipo=forms.CharField()

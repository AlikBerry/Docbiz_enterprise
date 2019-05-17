from django import forms
from django.forms import ModelForm, Textarea, TextInput, CharField


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

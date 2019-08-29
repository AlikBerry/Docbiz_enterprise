from django import forms
from django.forms import ModelForm, Textarea, TextInput, CharField, Form
from docbiz_app.models import Employee, Transactions, Cashboxes


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())







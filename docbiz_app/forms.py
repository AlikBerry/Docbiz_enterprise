from django import forms
from django.forms import ModelForm, Textarea, TextInput, CharField, Form
from docbiz_app.models import Employee, Transactions, Cashboxes


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['created_date', 'incoming', 'expense', 'description']
      

class TransactionSearchForm(forms.Form):
    description =  forms.CharField(
                    required = False,
                    label='Search name or surname!',
                    widget=forms.TextInput(attrs={'placeholder': 'search here!'})
                  )

    




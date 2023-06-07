from django.forms import ModelForm
from django import forms
from .models import client


class ClientForm(forms.ModelForm):
    class Meta:
        model = client
        fields = ['name', 'email']



        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control w-100', 'type': 'text', 'placeholder': 'Name' }),
            'email': forms.EmailInput(attrs={'class': 'form-control w-100', 'type': 'text' ,'placeholder': 'Email' })
        }


class CodeForm(forms.Form):

    class Meta:
        model = client
        fields = ['code']

    code = forms.TextInput(attrs={'class': 'form-control w-100', 'type': 'text', 'placeholder': 'UUID CODE' })



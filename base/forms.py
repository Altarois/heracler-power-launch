from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields =  ['username' , 'email' , 'password1', 'groups']

    CHOICES = (
        (1, 'Coach'),
        (2, 'Client'),
                )

    groups=forms.ChoiceField(label='Rest Time', widget=forms.RadioSelect(attrs={"class": "form-check" }), choices=CHOICES)

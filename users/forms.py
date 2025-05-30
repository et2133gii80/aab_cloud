from cProfile import label
from enum import unique

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    usable_password = None
    class Meta:
        model = User
        fields = ('email', 'username', 'password1','password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field in ['email', 'username']:
            self.fields[field].label = None

        for field_name in ['email', 'username', 'password1','password2']:
            self.fields[field_name].help_text = None


        self.fields['email'].widget.attrs.update({
            'class': 'input-group',
            'placeholder': 'Email'
        })

        self.fields['username'].widget.attrs.update({
            'class': 'input-group',
            'placeholder': 'Username'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'input-group',
            'placeholder': 'Password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'input-group',
            'placeholder': 'Re-password'
        })
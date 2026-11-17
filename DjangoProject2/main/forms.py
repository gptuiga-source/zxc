from typing import Any

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs = {'class': 'form-control', 'placeholder': 'Имя'}
        self.fields['email'].widget.attrs = {'class': 'form-control', 'placeholder': 'Почта'}

    class Meta:
        model = User
        fields = ('username', 'email')


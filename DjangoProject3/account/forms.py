from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginUser(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': "Имя",
            'class': 'username'
        })

        self.fields['password'].widget.attrs.update({
            'placeholder': "Введите пароль",
            'class': 'password'
        })



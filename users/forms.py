from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import CharField

from users.models import User


class UserLoginForm(AuthenticationForm):

    username = CharField(
        label="имя",
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "class": "form-control",
                "placeholder": "Введите ваше имя пользователя",
            }
        ),
    )

    password = CharField(
        label="пароль",
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": "form-control",
                "placeholder": "Введите ваш пароль",
            }
        ),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]

import email

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm 
from django.forms import CharField, ImageField

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


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class ProfileForm(UserChangeForm):
        class Meta:
            model = User
            fields = ('image',
                      'first_name',
                      'last_name',
                      'username',
                      'email',)
            
        image = ImageField(required=False)
        first_name = CharField()
        last_name = CharField()
        username = CharField()
        email = CharField()




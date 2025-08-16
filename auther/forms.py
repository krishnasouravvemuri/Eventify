from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    role = forms.ChoiceField(choices = [('Member', 'Member'), ('Host', 'Host')], required = True)

class SignpForm(UserCreationForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
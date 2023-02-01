from django.contrib.auth.models import User
from .models import Content, NewContent
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, EmailInput, PasswordInput, CharField, EmailField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import models
from django import forms


class CreateForm(ModelForm):
    class Meta:
        model = NewContent
        fields = ['title', 'autor', 'text', 'date']

        widgets = {
            'title': TextInput(attrs = {
                "class":       "form-control",
                "placeholder": "Название",
                }),
            'autor': TextInput(attrs = {
                "class":       "form-control",
                "placeholder": "Автор",
                }),
            'text': Textarea(attrs = {
                "class":       "form-control",
                "placeholder": "Ваш текст",
                }),
            'date': DateTimeInput(attrs = {
                "class":       "form-control",
                "placeholder": "Дата",
                }),
        }

class SignUpForm(UserCreationForm):
    password1 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        widgets = {
            'username':      TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name':    TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name':     TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email':         EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            
        }

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))

class SearchForm(forms.Form):
    query = forms.CharField()

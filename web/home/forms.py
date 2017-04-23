from django import forms
from django.db import models
from django.forms import PasswordInput, extras
from django.core.validators import RegexValidator


basicValidator = RegexValidator(
    regex='^[ a-zA-Z]*$',
    message='Input must only contain a-z, A-Z',
    code='invalid_input'
)
usernameValidator = RegexValidator(
    regex='^[a-zA-Z0-9]*$',
    message='Username must only contain a-z, A-Z, 0-9',
    code='invalid_username'
)
passwordValidator = RegexValidator(
    regex='^[a-zA-Z0-9@$!%*#?&]*$',
    message='Password must only contain a-z, A-Z, 0-9, @$!%*#?&',
    code='invalid_password'
)

skillValidator = RegexValidator(
    regex='^[a-zA-Z0-9@$!%*#?&()-=+~|]*$',
    message='Must only contain a-z, A-Z, 0-9, @$!%*#?&() ',
    code='invalid_input'
)

emailValidator = RegexValidator(
    regex='^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
    message='Invalid Email',
    code='invalid_email'
)

class SignUpForm(forms.Form):
	username = forms.CharField(label='Your username', max_length=100, required=True, validators=[usernameValidator])
	email = forms.CharField(label='Your email', max_length=100, required=True, validators=[emailValidator])
	last_name = forms.CharField(label='Your last name', max_length=100, required=True, validators=[basicValidator])
	first_name = forms.CharField(label='Your first name', max_length=100, required=True, validators=[basicValidator])
	password = forms.CharField(label='Your password', max_length=300, widget=forms.PasswordInput(), required=True, validators=[passwordValidator])
	password2 = forms.CharField(label='Confirm your passworld', max_length=130, widget=forms.PasswordInput(), required=True, validators=[passwordValidator])

class SignInForm(forms.Form):
	username = forms.CharField(label='Your username', max_length=100, required=True, validators=[usernameValidator])
	password = forms.CharField(label='Your password', max_length=300, widget=forms.PasswordInput(), required=True, validators=[passwordValidator])
    

class CreateSkillForm(forms.Form):
    skill = forms.CharField(label='Your skill', max_length=100, required=True, validators=[skillValidator])
    price = forms.DecimalField(label='Your price',  decimal_places=2, required=True)
    desc = forms.CharField(label='Your desc', max_length=100, widget=forms.Textarea(attrs={'rows':5,'cols':40}),required=True)

class SearchForm(forms.Form):
    #search = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter Skill'}))
    search = forms.CharField(label='', max_length=100)

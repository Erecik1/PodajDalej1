from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Sign Up Form
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='Optional',)
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    password = forms.CharField(max_length=64, required=True)

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'type':'login','id':'login'}),label= 'login')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password','id':'password'}),label='haslo')

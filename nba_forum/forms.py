from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


#create class for project form
class PostForm(ModelForm):
    class Meta: 
        model = Post
        fields =('title', 'post','rating', 'team')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['username'].help_text = "Username cannot be longer than 50 characters. Letters, digits and @/,/+/=/? only."
            self.fields['email'].help_text = "example@example.com"
        
        def clean_username(self):
            username = self.cleaned_data.get('username')
            if len(username) > 50:
                raise ValidationError("Username cannot be longer than 50 characters.")
            return username

class Authenticate(AuthenticationForm):
    username = forms.CharField(max_length=50, label="username")

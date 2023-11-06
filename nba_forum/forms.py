from django.forms import ModelForm
from .models import *


#create class for project form
class PostForm(ModelForm):
    class Meta: 
        model = Post
        fields =('title', 'post','rating')

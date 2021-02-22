from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['writer','pub_date']
    

    
   
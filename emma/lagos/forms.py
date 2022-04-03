from django import forms
from .models import Ted

class PostForm(forms.ModelForm):
    class Meta:
        model = Ted
        #fields = ['__all__']
        #fields = ['title','description']
        exclude = ['created_by','date_created']
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'',
            'type':'text', 
            'name':'username', 
            'id':'username', 
            'class':'form-control', 
        })
        
        self.fields["password1"].widget.attrs.update({
            'required':'',
            'type':'password', 
            'name':'password1', 
            'id':'password1', 
            'class':'form-control', 
            
        })
        self.fields["password2"].widget.attrs.update({
            'required':'',
            'type':'password', 
            'name':'password2', 
            'id':'password2', 
            'class':'form-control', 
           
        })
    class Meta:
        model = User
        fields = ['username','password1','password2']
        
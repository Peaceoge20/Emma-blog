from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Ted(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length = 225)
    body = RichTextField(null = True, blank = True)
    description = models.CharField(max_length = 225)
    category = models.CharField(max_length=100, null = True, blank = True) 
    image = models.ImageField(upload_to="image", null = True, blank = True)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)    
    date_created = models.DateTimeField(auto_now_add= True, auto_now= False)
    updated      = models.DateTimeField(auto_now_add= False, auto_now= True)


    def __str__(self):
        return f"{self.title} || {self.author}"



    
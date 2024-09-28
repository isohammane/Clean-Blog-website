from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User
# Create your models here.
class Artical(models.Model):
    title = models.CharField(max_length=500,null=False,blank=False)
    summary = models.TextField(null=True)
    content = CKEditor5Field("TEXT",config_name="extends")
    created = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(User ,on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    

class ContactForm(models.Model):
    name =models.CharField(max_length=100,null=False,blank=False)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
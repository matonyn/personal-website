from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class Ref(models.Model):
    name =  models.CharField(max_length=200, default="NAME")
    surname = models.CharField(max_length=200, default='SURNAME')
    connection = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True)
    email_adress = models.CharField(max_length=400, default="name.surname@gmail.com")
    linkedin_url = models.CharField(max_length=400, default="linkein/url")
    details =  models.CharField(max_length=1000)
    review = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.surname}"
    

class resume(models.Model):
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='Users/madinadairova/Documents/my_website/backend/media', blank=True)
    def __str__(self):
        return self.title
    

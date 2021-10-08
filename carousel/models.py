from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class carousel(models.Model):
    
    title = models.CharField(max_length=50)
    
    image = models.ImageField(upload_to='carousel/')


    def __str__(self):
        return self.title
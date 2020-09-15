from django.db import models

# Create your models here.

class Destination(models.Model):
    
    name =models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics') #inside bracket u have to specified the loaction of image....pic is folder
    desc= models.TextField()
    price =models.IntegerField()
    offer = models.BooleanField(default=False)


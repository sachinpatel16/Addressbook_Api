from django.db import models

# Create your models here.
class Addres(models.Model):
    addres = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    
    def __str__(self):
        return self.country
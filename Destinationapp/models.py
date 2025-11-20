from django.db import models

# Create your models here.
class Destination(models.Model):
    Place = models.CharField(max_length=100)
    Weather = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Map = models.URLField(max_length=300)
    Description = models.CharField(max_length=5000)
    Image = models.ImageField(upload_to='destinations/')
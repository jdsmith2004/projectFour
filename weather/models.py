from django.db import models

# Create your models here.

class Observation(models.Model):
    time = models.DateTimeField()
    temp = models.FloatField()
    sky = models.CharField(max_length=100)

    
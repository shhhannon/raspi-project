from django.db import models

# Create your models here.
class reading(models.Model):
  airQuality = models.CharField(max_length = 20)
  dateTime = models.DateTimeField()
  numDoses = models.IntegerField()

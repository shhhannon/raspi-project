from django.db import models

class readings(models.Model):
  date = models.DateField()
  time = models.TimeField()
  CO2 = models.FloatField()
  doses = models.IntegerField(default=200)

  def __str__(self):
        return f"{self.date} {self.time} - eCO2: {self.eco2_levels} ppm"

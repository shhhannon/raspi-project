from django.db import models

class readings(models.Model):
  date = models.DateField()
  time = models.TimeField()
  CO2 = models.FloatField()
  doses = models.IntegerField(default=200)

  def __str__(self):
      return f"Date: {self.date}, Time: {self.time}, CO2: {self.CO2}, Doses: {self.doses}"

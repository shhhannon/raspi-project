from django.db import models

class sensorData(models.Model):
  date = models.DateField()
  time = models.TimeField()
  eco2Levels = models.FloatField()
  totalVoc = models.FloatField()
  doses = models.IntegerField(default=200)

  def __str__(self):
        return f"{self.date} {self.time} - eCO2: {self.eco2_levels} ppm, VOC: {self.total_voc} ppb"

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Airline(models.Model):
	airline_name = models.CharField(max_length=50)
	flight_type = models.CharField(max_length=20)

	def __str__(self):
		return self.airline_name

class FlightSchedule(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    flight_time = models.CharField(max_length=5)

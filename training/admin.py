from django.contrib import admin
from .models import Airline, FlightSchedule

# Register your models here.
admin.site.register(Airline)
admin.site.register(FlightSchedule)


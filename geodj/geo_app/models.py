from django.db import models
from geopy.geocoders import Nominatim
from datetime import date

class Address(models.Model):
    iteration = models.CharField(max_length = 255, default="")
    address = models.CharField(max_length = 300, default="")
    coordinates = models.CharField(max_length = 300, default = "")
    latitude = models.DecimalField(max_digits=50, decimal_places=7, default=0.00)
    longitude = models.DecimalField(max_digits=50, decimal_places=7, default=0.00)

    def __str__(self):
        return self.address

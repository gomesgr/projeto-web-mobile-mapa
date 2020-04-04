from django.db import models

# Create your models here.
class Location(models.Model):
    lat_from = models.DecimalField(max_digits=8, decimal_places=5)
    long_from = models.DecimalField(max_digits=8, decimal_places=5)
    lat_to = models.DecimalField(max_digits=8, decimal_places=5)
    long_to = models.DecimalField(max_digits=8, decimal_places=5)
    date_created = models.DateTimeField(auto_now=True)
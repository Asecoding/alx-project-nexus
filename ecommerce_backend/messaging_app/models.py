from django.db import models
class product (models.Model):
    name = models.CharField(max_length=200)
    marchant = models.CharField(max_length=100)
    booking_date = models.DateField()

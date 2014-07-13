from django.db import models


# Create your models here.
class Laboratory(models.Model):

    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)

    url = models.URLField(max_length=300)
    adress = models.CharField(max_length=300)

    is_moderated = models.BooleanField(default=False)

    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)

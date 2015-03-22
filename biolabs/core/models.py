from django.db import models


# Create your models here.
class Laboratory(models.Model):

    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300, blank=True, null=True)

    url = models.URLField(max_length=300)
    adress = models.CharField(max_length=300, blank=True, null=True)

    is_moderated = models.BooleanField(default=False)

    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)

    def __unicode__(self):
        return self.name

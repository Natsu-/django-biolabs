from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField


# Create your models here.
class Laboratory(models.Model):

    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300, blank=True, null=True)

    url = models.URLField(max_length=300)
    adress = models.CharField(max_length=300, blank=True, null=True)

    is_moderated = models.BooleanField(default=False)

    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)

    country = CountryField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        super(Laboratory, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

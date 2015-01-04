from biolabs.core import models as core_models
from rest_framework import serializers


class LaboratorySerializer(serializers.HyperlinkedModelSerializer):
    description = serializers.CharField(required=False, max_length=255)
    adress = serializers.CharField(required=False, max_length=255)
    latitude = serializers.DecimalField(required=False, max_digits=23, decimal_places=20)
    longitude = serializers.DecimalField(required=False, max_digits=23, decimal_places=20)

    class Meta:
        model = core_models.Laboratory
        fields = ('name', 'description', 'url', 'adress',
                  'latitude', 'longitude')

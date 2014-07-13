from biolabs.core import models as core_models
from rest_framework import serializers


class LaboratorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = core_models.Laboratory
        fields = ('name', 'description', 'url', 'adress')

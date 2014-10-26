
# Create your views here.
from rest_framework import viewsets

from biolabs.core import models as core_models
from biolabs.core.serializers import LaboratorySerializer


class LaboratoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows labs to be viewed or edited.
    """
    queryset = core_models.Laboratory.objects.filter(is_moderated=True)
    serializer_class = LaboratorySerializer

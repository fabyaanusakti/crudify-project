from rest_framework import viewsets
from core.models import ProjekModels
from .serializers import ProjekSerializer

class ProjekViewSet(viewsets.ModelViewSet):
    queryset = ProjekModels.objects.all()
    serializer_class = ProjekSerializer

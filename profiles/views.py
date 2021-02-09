from rest_framework import viewsets
from .models import Psychotherapist, RawData
from .serializers import PsychotherapistSerializer, RawDataSerializer


class PsychotherapistViewSet(viewsets.ModelViewSet):
    queryset = Psychotherapist.objects.all()
    serializer_class = PsychotherapistSerializer


class RawDataViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = RawData.objects.all()
    serializer_class = RawDataSerializer

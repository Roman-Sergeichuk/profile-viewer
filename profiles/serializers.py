from rest_framework import serializers
from .models import Psychotherapist, RawData


class PsychotherapistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Psychotherapist
        fields = '__all__'


class RawDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = RawData
        fields = '__all__'
from rest_framework import serializers
from core.models import ProjekModels

class ProjekSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjekModels
        fields = '__all__'
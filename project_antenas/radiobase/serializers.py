from rest_framework import serializers 
from .models import Radiobase

class Rb_serial(serializers.ModelSerializer):
    lat = serializers.CharField(source='latitud')
    lng = serializers.CharField(source='longitud')

    class Meta:
        model = Radiobase
        fields = ("lat", "lng", "empresaduena")
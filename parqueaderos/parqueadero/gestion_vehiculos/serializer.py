from rest_framework import serializers

from gestion_vehiculos.models import vehilculo

class vehiculo_serializer(serializers.ModelSerializer):
    class Meta:
        model=vehilculo
        fields=['placa', 'modelo', 'marca', 'color']
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import vehiculo_serializer
from .models import vehilculo
import json

# Create your views here.

class VehiculoApiView(APIView):
    
    def get(self, request, *args, **kwargs):
        lista_vehiculos = vehilculo.objects.all()
        serializador = vehiculo_serializer(lista_vehiculos, many=True)
        return Response(serializador.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data={
            'placa':request.data.get('placa'),
            'marca':request.data.get('marca'),
            'modelo':request.data.get('modelo'),
            'color':request.data.get('color')
        }
        serializador = vehiculo_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)
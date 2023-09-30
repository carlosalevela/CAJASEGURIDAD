from django.db import models

# Create your models here.
class vehilculo(models.Model):
    placa = models.CharField(max_length=6)
    modelo = models.IntegerField()
    color = models.CharField(max_length=10)
    marca = models.CharField(max_length=20)
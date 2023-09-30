from django.contrib import admin

from gestion_vehiculos.models import vehilculo


# Register your models here.

@admin.register(vehilculo)
class vehiculo_admin(admin.ModelAdmin):
    list_display=['placa', 'marca']
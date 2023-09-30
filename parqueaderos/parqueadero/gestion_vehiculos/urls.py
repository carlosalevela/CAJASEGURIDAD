from django.urls import path
from .views import VehiculoApiView


urlpatterns = [
   
    path('vehiculos/', VehiculoApiView.as_view()),



]
from django.urls import path
from .views import calcular_cabida

urlpatterns = [
    path('', calcular_cabida, name='calcular_cabida'),
]

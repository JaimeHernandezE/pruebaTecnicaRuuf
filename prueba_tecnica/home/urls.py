from django.urls import path
from .views import calcular_view

urlpatterns = [
    path('calcular/', calcular_view, name='calcular_cabida'),
]
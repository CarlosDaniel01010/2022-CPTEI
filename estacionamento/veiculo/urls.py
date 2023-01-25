from django.urls import path
from .views import VeiculoView

urlpatterns = [
    path('Veiculos', VeiculoView.as_view(), name='veiculos'),
]
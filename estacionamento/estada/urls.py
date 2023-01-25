from django.urls import path
from .views import EstadaView

urlpatterns = [
    path('estadas', EstadaView.as_view(), name='estadas'),
]
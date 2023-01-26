from django.urls import path
from .views import EstadaView, EstadaAddView, EstadaUpDateView, EstadaDeleteView

urlpatterns = [
    path('estadas', EstadaView.as_view(), name='estadas'),
    path('estada/adicionar', EstadaAddView.as_view(), name='estada_adicionar'),
    path('<int:pk>/estada/editar/', EstadaUpDateView.as_view(), name='estada_editar'),
    path('<int:pk>/estada/apagar/', EstadaDeleteView.as_view(), name='estada_apagar'),
]
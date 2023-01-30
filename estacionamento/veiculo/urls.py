from django.urls import path
from .views import VeiculoView, VeiculoAddView, VeiculoUpDateView, VeiculoDeleteView

#Rotas apontadas para as Classes da View.
urlpatterns = [
    path('Veiculos', VeiculoView.as_view(), name='veiculos'),
    path('veiculo/adicionar', VeiculoAddView.as_view(), name='veiculo_adicionar'),
    path('<int:pk>/veiculo/editar/', VeiculoUpDateView.as_view(), name='veiculo_editar'),
    path('<int:pk>/veiculo/apagar/', VeiculoDeleteView.as_view(), name='veiculo_apagar'),
]
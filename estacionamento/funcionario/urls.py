from django.urls import path
from .views import FuncionarioView, FuncionarioAddView, FuncionarioUpDateView, FuncionarioDeleteView

#Rotas apontadas para as Classes da View.

urlpatterns = [
    path('funcionarios', FuncionarioView.as_view(), name='funcionarios'),
    path('funcionario/adicionar', FuncionarioAddView.as_view(), name='funcionario_adicionar'),
    path('<int:pk>/funcionario/editar/', FuncionarioUpDateView.as_view(), name='funcionario_editar'),
    path('<int:pk>/funcionario/apagar/', FuncionarioDeleteView.as_view(), name='funcionario_apagar')
]
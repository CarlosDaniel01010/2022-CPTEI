from django.urls import path
from .views import FuncionarioView, FuncionarioAddView

urlpatterns = [
    path('funcionarios', FuncionarioView.as_view(), name='funcionarios'),
    path('funcionario/adicionar', FuncionarioAddView.as_view(), name='funcionario_adicionar')
]
from django.shortcuts import render
from django.views.generic import TemplateView

from funcionario.models import Funcionario
from veiculo.models import Veiculo


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        #context['qtd_clientes'] = Cliente.objects.count()
        context['qtd_funcionarios'] = Funcionario.objects.count()
        context['qtd_veiculos'] = Veiculo.objects.count()
        return context

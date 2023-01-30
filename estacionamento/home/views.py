from django.shortcuts import render
from django.views.generic import TemplateView

from cliente.models import Cliente
from funcionario.models import Funcionario
from veiculo.models import Veiculo


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    # O método get_context_data fornece os dados do contexto que serão aplicados na renderização do template
    # Ta contando quantos funcionários, clientes, veiculos tem e jogando nas divs da Pagina principal(HOME)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['qtd_clientes'] = Cliente.objects.count()
        context['qtd_funcionarios'] = Funcionario.objects.count()
        context['qtd_veiculos'] = Veiculo.objects.count()
        return context

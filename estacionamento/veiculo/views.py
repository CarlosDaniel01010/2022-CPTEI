from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from home.utils import HtmlToPdf
from veiculo.forms import VeiculoModelForm
from veiculo.models import Veiculo
from django.core.paginator import Paginator
# Create your views here.

class VeiculoView(ListView):
    model = Veiculo
    template_name = 'veiculos.html'


    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(VeiculoView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(modelo__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 5)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, "Não existem veiculos cadastrados!")

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='veiculos_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(VeiculoView, self).get(*args, **kwargs)

class VeiculoAddView(SuccessMessageMixin, CreateView):
    form_class = VeiculoModelForm
    model = Veiculo
    template_name = 'veiculo_form.html'
    success_url = reverse_lazy('veiculos')
    success_message = 'Veiculo cadastrado com sucesso!'


class VeiculoUpDateView(SuccessMessageMixin, UpdateView):
    form_class = VeiculoModelForm
    model = Veiculo
    template_name = 'veiculo_form.html'
    success_url = reverse_lazy('veiculos')
    success_message = 'Veiculo alterado com sucesso!'

class VeiculoDeleteView(SuccessMessageMixin, DeleteView):
    model = Veiculo
    template_name = 'veiculo_apagar.html'
    success_url = reverse_lazy('veiculos')
    success_message = 'Veiculo excluido com sucesso!'
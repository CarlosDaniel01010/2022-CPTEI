from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

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


        paginator = Paginator(qs, 5)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem


class VeiculoAddView(CreateView):
    form_class = VeiculoModelForm
    model = Veiculo
    template_name = 'veiculo_form.html'
    success_url = reverse_lazy('veiculos')


class VeiculoUpDateView(UpdateView):
    form_class = VeiculoModelForm
    model = Veiculo
    template_name = 'veiculo_form.html'
    success_url = reverse_lazy('veiculos')

class VeiculoDeleteView(DeleteView):
    model = Veiculo
    template_name = 'veiculo_apagar.html'
    success_url = reverse_lazy('veiculos')
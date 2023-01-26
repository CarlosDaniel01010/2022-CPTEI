from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from estada.forms import EstadaModelForm
from estada.models import Estada
# Create your views here.

class EstadaView(ListView):
    model = Estada
    template_name = 'estadas.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(EstadaView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        paginator = Paginator(qs, 5)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem


class EstadaAddView(CreateView):
    form_class = EstadaModelForm
    model = Estada
    template_name = 'estada_form.html'
    success_url = reverse_lazy('estadas')

class EstadaUpDateView(UpdateView):
    form_class = EstadaModelForm
    model = Estada
    template_name = 'estada_form.html'
    success_url = reverse_lazy('estadas')


class EstadaDeleteView(DeleteView):
    model = Estada
    template_name = 'estada_apagar.html'
    success_url = reverse_lazy('estadas')
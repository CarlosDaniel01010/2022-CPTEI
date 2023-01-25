from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, CreateView
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

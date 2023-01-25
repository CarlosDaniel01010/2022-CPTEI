from django.shortcuts import render
from django.views.generic import ListView
from veiculo.models import Veiculo
# Create your views here.

class VeiculoView(ListView):
    model = Veiculo
    template_name = 'veiculos.html'


    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(VeiculoView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(modelo__icontains=buscar)
        return qs

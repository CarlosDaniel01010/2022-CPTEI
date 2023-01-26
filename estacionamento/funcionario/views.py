from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from funcionario.forms import FuncionarioModelForm
from funcionario.models import Funcionario
# Create your views here.


class FuncionarioView(ListView):
    model = Funcionario
    template_name = 'funcionarios.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(FuncionarioView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        paginator = Paginator(qs, 5)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem



class FuncionarioAddView(CreateView):
    form_class = FuncionarioModelForm
    model = Funcionario
    template_name = 'funcionario_form.html'
    success_url = reverse_lazy('funcionarios')


class FuncionarioUpDateView(UpdateView):
    form_class = FuncionarioModelForm
    model = Funcionario
    template_name = 'funcionario_form.html'
    success_url = reverse_lazy('funcionarios')

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = 'funcionario_apagar.html'
    success_url = reverse_lazy('funcionarios')
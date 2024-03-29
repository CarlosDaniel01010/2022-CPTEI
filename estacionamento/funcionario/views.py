from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from funcionario.forms import FuncionarioModelForm
from funcionario.models import Funcionario
from home.utils import HtmlToPdf


# Create your views here.

# Corresponde a uma Página com uma lista de objetos, Enquanto
# a view é executada, o object_list armazena a lista de objetos
# que a view está operando

class FuncionarioView(ListView):
    model = Funcionario
    template_name = 'funcionarios.html'

    #QuerySet:
    #Representa um conjunto de objetos Pode ter zero, um ou vários filtros
    # Os filtros restringem os resultados da consulta com base nos parâmetros fornecidos


    # Método que retorna um QuerySet com as propriedades estabelecidas, por retornar um QuerySet permite a utilização de filtros e outros
    # métodos do QuerySet
    # usando o GET
    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(FuncionarioView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 5)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, "Não existem funcionarios cadastrados!")

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='funcionarios_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(FuncionarioView, self).get(*args, **kwargs)


# Reverse_lazy - Função que permite executar uma reversão de URL

#Classe Adicionar
class FuncionarioAddView(SuccessMessageMixin, CreateView):
    form_class = FuncionarioModelForm
    model = Funcionario
    template_name = 'funcionario_form.html'
    success_url = reverse_lazy('funcionarios')
    success_message = 'Funcionário cadastrado com sucesso!'


#Classe Atualizar
class FuncionarioUpDateView(SuccessMessageMixin, UpdateView):
    form_class = FuncionarioModelForm
    model = Funcionario
    template_name = 'funcionario_form.html'
    success_url = reverse_lazy('funcionarios')
    success_message = 'Funcionário alterado com sucesso!'


#Classe Remover
class FuncionarioDeleteView(SuccessMessageMixin, DeleteView):
    model = Funcionario
    template_name = 'funcionario_apagar.html'
    success_url = reverse_lazy('funcionarios')
    success_message = 'Funcionário excluido com sucesso!'
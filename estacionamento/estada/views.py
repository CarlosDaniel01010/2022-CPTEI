from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from estada.forms import EstadaModelForm, EstadaListForm
from estada.models import Estada
from home.utils import HtmlToPdf


# Create your views here.

class EstadaView(ListView):
    model = Estada
    template_name = 'estadas.html'


    def get_context_data(self, **kwargs):
        context = super(EstadaView, self).get_context_data(**kwargs)

        if self.request.GET:
            form = EstadaListForm(self.request.GET)
        else:
            form = EstadaListForm()

        context['form'] = form

        return context

    def get_queryset(self, *args, **kwargs):
        #buscar = self.request.GET.get('buscar')
        qs = super(EstadaView, self).get_queryset(*args, **kwargs)
        #if buscar:
            #qs = qs.filter(nome__icontains=buscar)
        if self.request.GET:
            form = EstadaListForm(self.request.GET)
            if form.is_valid():
                funcionario = form.cleaned_data.get('funcionario')
                veiculo = form.cleaned_data.get('veiculo')

                if funcionario:
                    qs = qs.filter(funcionario=funcionario)

                if veiculo:
                    qs = qs.filter(veiculo=veiculo)

        if qs.count() > 0:
            paginator = Paginator(qs, 5)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
             return messages.info(self.request, "Não existem estadas cadastradas!")

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='estadas_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(EstadaView, self).get(*args, **kwargs)

class EstadaAddView(SuccessMessageMixin, CreateView):
    form_class = EstadaModelForm
    model = Estada
    template_name = 'estada_form.html'
    success_url = reverse_lazy('estadas')
    success_message = 'Estada cadastrado com sucesso!'

class EstadaUpDateView(SuccessMessageMixin, UpdateView):
    form_class = EstadaModelForm
    model = Estada
    template_name = 'estada_form.html'
    success_url = reverse_lazy('estadas')
    success_message = 'Estada alterada com sucesso!'


class EstadaDeleteView(SuccessMessageMixin, DeleteView):
    model = Estada
    template_name = 'estada_apagar.html'
    success_url = reverse_lazy('estadas')
    success_message = 'Estada excluida com sucesso!'
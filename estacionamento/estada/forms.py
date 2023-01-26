from django import forms

from funcionario.models import Funcionario
from veiculo.models import Veiculo
from .models import Estada


class EstadaListForm(forms.Form):
    funcionario = forms.ModelChoiceField(label='Funcionario', widget=forms.Select(
        attrs={'class': 'select is-fullwidth'}), queryset=Funcionario.objects.all(), required=False)

    veiculo = forms.ModelChoiceField(label='Veiculo', widget=forms.Select(
        attrs={'class': 'select is-fullwidth'}), queryset=Veiculo.objects.all(), required=False)

class EstadaModelForm(forms.ModelForm):
    class Meta:
        model = Estada
        fields = ['entrada', 'saida', 'funcionario', 'veiculo', 'data_pagamento', 'valor']
        widgets = {
            'entrada': forms.TimeInput(
                attrs={'class': 'input', 'placeholder': 'Hora de Entrada'}),
            'saida': forms.TimeInput(
                attrs={'class': 'input', 'placeholder': 'Hora de Saida'}),
            'funcionario': forms.Select(
                attrs={'class': 'input', 'placeholder': 'Selecione o Funcionario'}),
            'veiculo': forms.Select(
                attrs={'class': 'input', 'placeholder': 'Selecione o Veiculo'}),
            'data_pagamento': forms.DateInput(
                attrs={'class': 'input', 'placeholder': 'Data do pagamento'}),
            'valor': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Valor total'}),
        }
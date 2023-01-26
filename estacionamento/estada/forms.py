from django import forms
from .models import Estada

class EstadaModelForm(forms.ModelForm):
    class Meta:
        model = Estada
        fields = ['entrada', 'saida', 'funcionario', 'veiculo', 'data_pagamento', 'valor']
        widgets = {
            #'entrada': forms.TimeField(
                #attrs={'class': 'input', 'type': 'time'}),
            #'saida': forms.TimeField(
                #attrs={'class': 'input', 'type': 'time'}),
            'funcionario': forms.Select(
                attrs={'class': 'input', 'placeholder': 'Selecione o Funcionario'}),
            'veiculo': forms.Select(
                attrs={'class': 'input', 'placeholder': 'Selecione o Veiculo'}),
            #'data_pagamento': forms.DateField(
                #attrs={'class': 'input', 'type': 'date'}),
            'valor': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Valor total'}),
        }
from django import forms
from .models import Veiculo

class VeiculoModelForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'placa', 'cor']
        widgets = {
            'modelo': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o modelo do Carro'}),
            'placa': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite a placa do Carro'}),
            'cor': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o modelo do Carro'}),
        }
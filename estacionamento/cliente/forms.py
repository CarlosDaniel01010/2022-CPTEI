from django import forms
from .models import Cliente

class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email', 'cpf', 'endereco','cnpj']
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite  o nome do Funcionário'}),
            'telefone': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o número de Telefone'}),
            'email': forms.EmailInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o e-mail do Funcionário'}),
            'cpf': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite  o Cpf'}),
            'endereco': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite  o endereço do Funcionário'}),
            'cnpj': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite  o Cnpj'}),
        }
from django import forms
from .models import Funcionario

class FuncionarioModelForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'telefone', 'email', 'cpf', 'endereco', 'funcao', 'foto']
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
            'funcao': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite  a função do Funcionário'}),
            'foto': forms.FileInput(attrs={'class':'input', 'type':'file'})
        }
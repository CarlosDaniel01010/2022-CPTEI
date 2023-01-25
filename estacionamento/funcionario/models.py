from django.db import models
from stdimage import StdImageField
from home.models import Pessoa
# Create your models here.

class Funcionario(Pessoa):
    cpf = models.CharField('Cpf', max_length=25, help_text='Cpf Completo')
    endereco = models.CharField('Endereço', max_length=50, help_text='Endereço Completo')
    funcao = models.CharField('Função', max_length=30, help_text='Função na Empresa')
    foto = StdImageField('Foto', upload_to='funcionarios',
                         variations={'thumbnail': {'width': 100, 'height': 100, 'crop': True}},
                         delete_orphans=True, null=True, blank=True)


    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'


    def __str__(self):
        return super().nome

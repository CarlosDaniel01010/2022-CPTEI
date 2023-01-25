from django.db import models
from stdimage import StdImageField
from home.models import Pessoa


# Create your models here.

class Funcionario(Pessoa):
    funcao = models.CharField('Função', max_length=30, help_text='Função na Empresa')
    foto = StdImageField('Foto', upload_to='funcionarios',
                         variations={'thumbnail': {'width': 100, 'height': 100, 'crop': True}},
                         delete_orphans=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        ordering = ['nome', ]

    def __str__(self):
        return super().nome

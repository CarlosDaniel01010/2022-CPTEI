from django.db import models
from stdimage import StdImageField
from home.models import Pessoa
# Create your models here.

class Cliente(Pessoa):
    cnpj = models.CharField('Cnpj', max_length=25, help_text='Cnpj', blank=True, null=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome', ]

    def __str__(self):
        return super().nome

from django.db import models
from stdimage import StdImageField
from home.models import Pessoa
# Create your models here.

# Aqui que se define as classes da aplicação, os atributos/campos e os seus respectivos tipos.
# Está herdando da classe Pessoa os campos la de Home.models
class Cliente(Pessoa):
    cnpj = models.CharField('Cnpj', max_length=25, help_text='Cnpj Completo', blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome', ]

    def __str__(self):
        return super().nome

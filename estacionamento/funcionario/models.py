from django.db import models
from stdimage import StdImageField
from home.models import Pessoa


# Create your models here.
# Aqui que se define as classes da aplicação, os atributos/campos e os seus respectivos tipos.
# Está herdando da classe Pessoa os campos la de Home.models

class Funcionario(Pessoa):
    CARGOS_OPCOES = (
        ('Nenhum', 'Nenhum'),
        ('CEO', 'CEO'),
        ('Presidente', 'Presidente'),
        ('Diretor', 'Diretor'),
        ('Gerente', 'Gerente'),
        ('Supervisor', 'Supervisor'),
        ('Assistente', 'Assistente'),
    )

    funcao = models.CharField('Função', max_length=30, help_text='Função na Empresa', choices=CARGOS_OPCOES, default='N')
    foto = StdImageField('Foto', upload_to='funcionarios',
                         variations={'thumbnail': {'width': 100, 'height': 100, 'crop': True}},
                         delete_orphans=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        ordering = ['nome', ]

    def __str__(self):
        return super().nome

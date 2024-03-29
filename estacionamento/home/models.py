from django.db import models

# Create your models here.

# Aqui que se define as classes da aplicação, os atributos/campos e os seus respectivos tipos.
class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome Completo')
    telefone = models.CharField('Telefone', max_length=15, help_text='Número do telefone')
    email = models.EmailField('E-mail', max_length=100, help_text='Endereço de e-mail', unique=True)
    endereco = models.CharField('Endereço', max_length=50, help_text='Endereço Completo')
    cpf = models.CharField('Cpf', max_length=25, help_text='Cpf Completo', blank=True, null=True, unique=True)


    class Meta:
        abstract = True

    def __str__(self):
        return  self.nome
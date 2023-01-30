from django.db import models

# Create your models here.

# Aqui que se define as classes da aplicação, os atributos/campos e os seus respectivos tipos.
class Veiculo(models.Model):
    modelo = models.CharField('Modelo', max_length=30, help_text='Modelo do Carro')
    placa = models.CharField('Placa', max_length=12, help_text='Placa do Carro')
    cor = models.CharField('Cor', max_length=15, help_text='Cor do Carro')
    cliente = models.ForeignKey('cliente.Cliente', verbose_name='Cliente', help_text='Nome do Cliente', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'
        ordering = ['modelo', ]

    def __str__(self):
        return self.modelo
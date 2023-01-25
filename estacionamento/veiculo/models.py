from django.db import models

# Create your models here.

class Veiculo(models.Model):
    modelo = models.CharField('Modelo', max_length=30, help_text='Modelo do Carro')
    placa = models.CharField('Placa', max_length=12, help_text='Placa do Carro')
    cor = models.CharField('Cor', max_length=15, help_text='Cor do Carro')


    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'

    def __str__(self):
        return self.modelo
from django.db import models

# Create your models here.

class Estada(models.Model):
    entrada = models.TimeField('Entrada', help_text='Hora de Entrada')
    saida = models.TimeField('Saída', help_text='Hora de Saída')
    funcionario = models.ForeignKey('funcionario.Funcionario', verbose_name='Funcionario', help_text='Nome do Funcionário', on_delete=models.CASCADE)
    veiculo = models.ForeignKey('veiculo.Veiculo', verbose_name='Veiculo', help_text='Nome do Veiculo', on_delete=models.CASCADE)
    data_pagamento = models.DateField('Data de Pagamento', help_text='Data de Pagamento')
    valor = models.DecimalField('Valor', max_digits=5, decimal_places=2, help_text='Valor da Estada')

    class Meta:
        verbose_name = 'Estada'
        verbose_name_plural = 'Estadas'

    def __str__(self):
        return f'Funcionario: {self.funcionario}'
# Generated by Django 4.1.2 on 2023-01-25 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0004_alter_funcionario_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cpf',
            field=models.CharField(help_text='Cpf', max_length=25, verbose_name='Cpf'),
        ),
    ]

# Generated by Django 4.1.2 on 2023-01-25 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0002_alter_funcionario_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cpf',
            field=models.CharField(help_text='Cpf Completo', max_length=25, verbose_name='Cpf1'),
        ),
    ]

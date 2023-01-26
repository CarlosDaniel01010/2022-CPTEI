# Generated by Django 4.1.2 on 2023-01-26 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_alter_cliente_cnpj_alter_cliente_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cnpj',
            field=models.CharField(blank=True, help_text='Cnpj Completo', max_length=25, null=True, unique=True, verbose_name='Cnpj'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(blank=True, help_text='Cpf Completo', max_length=25, null=True, unique=True, verbose_name='Cpf'),
        ),
    ]

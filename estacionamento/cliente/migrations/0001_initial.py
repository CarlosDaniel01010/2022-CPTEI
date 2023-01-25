# Generated by Django 4.1.2 on 2023-01-25 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome Completo', max_length=50, verbose_name='Nome')),
                ('telefone', models.CharField(help_text='Número do telefone', max_length=15, verbose_name='Telefone')),
                ('email', models.EmailField(help_text='Endereço de e-mail', max_length=100, unique=True, verbose_name='E-mail')),
                ('endereco', models.CharField(help_text='Endereço Completo', max_length=50, verbose_name='Endereço')),
                ('cpf', models.CharField(help_text='Cpf', max_length=25, verbose_name='Cpf')),
                ('cnpj', models.CharField(help_text='Cnpj', max_length=25, verbose_name='Cnpj')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['nome'],
            },
        ),
    ]
# Generated by Django 4.1.2 on 2023-01-24 22:29

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome Completo', max_length=50, verbose_name='Nome')),
                ('telefone', models.CharField(help_text='Número do telefone', max_length=15, verbose_name='Telefone')),
                ('email', models.EmailField(help_text='Endereço de e-mail', max_length=100, unique=True, verbose_name='E-mail')),
                ('cpf', models.CharField(help_text='Cpf Completo', max_length=25, verbose_name='Cpf')),
                ('endereco', models.CharField(help_text='Endereço Completo', max_length=50, verbose_name='Endereço')),
                ('funcao', models.CharField(help_text='Função na Empresa', max_length=30, verbose_name='Função')),
                ('foto', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='funcionarios', variations={'thumbnail': {'crop': True, 'height': 100, 'width': 100}}, verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'Funcionario',
                'verbose_name_plural': 'Funcionarios',
            },
        ),
    ]
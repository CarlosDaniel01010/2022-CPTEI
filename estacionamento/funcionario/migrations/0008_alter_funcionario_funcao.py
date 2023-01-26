# Generated by Django 4.1.2 on 2023-01-26 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0007_alter_funcionario_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='funcao',
            field=models.CharField(choices=[('N', '---------'), ('C', 'CEO'), ('P', 'Presidente'), ('D', 'Diretor'), ('G', 'Gerente'), ('S', 'Supervisor'), ('A', 'Assistente')], default='N', help_text='Função na Empresa', max_length=30, verbose_name='Função'),
        ),
    ]

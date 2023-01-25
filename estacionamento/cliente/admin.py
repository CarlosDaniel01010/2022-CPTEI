from django.contrib import admin
from cliente.models import Cliente
from django.utils.html import format_html
# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    fields = ('nome', 'telefone', 'email', 'cpf','endereco','cnpj',)
    list_display = ('nome', 'telefone', 'email')


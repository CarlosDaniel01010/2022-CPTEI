from django.contrib import admin
from funcionario.models import Funcionario
from django.utils.html import format_html
# Register your models here.

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    fields = ('nome', 'telefone', 'email', 'cpf','endereco', 'funcao', 'foto', 'fotografia')
    list_display = ('nome', 'telefone', 'email')
    readonly_fields = ['fotografia']

    def fotografia(self, obj):
        if obj.foto:
            return format_html('<img width="75px" src"{}" />', obj.foto.url)
        pass

from django.contrib import admin

from .models import Estada


# Register your models here.
@admin.register(Estada)
class EstadaAdmin(admin.ModelAdmin):
    list_display = ['entrada', 'saida', 'funcionario', 'data_pagamento', 'valor']
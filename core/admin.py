from django.contrib import admin
from .models import Projeto, Voluntario, Contato, Doacao

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_inicio', 'ativo', 'data_criacao')
    list_filter = ('ativo', 'data_inicio')
    search_fields = ('titulo', 'descricao')

@admin.register(Voluntario)
class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefone', 'area_interesse', 'data_cadastro')
    search_fields = ('usuario__username', 'usuario__email', 'area_interesse')

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'data_envio')
    search_fields = ('nome', 'email', 'assunto')
    list_filter = ('data_envio',)

@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):
    list_display = ('nome_doador', 'tipo', 'valor', 'data_doacao')
    list_filter = ('tipo', 'data_doacao')
    search_fields = ('nome_doador', 'email_doador')

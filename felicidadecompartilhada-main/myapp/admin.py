from django.contrib import admin
from .models import Instituicao, Atividade
from .models import RelatorioAnual
from .models import QRCodePixFelicidade, QRCodePixParceiros


class Filial(admin.ModelAdmin):
    list_display = ('nome_filial')


from django.contrib import admin
from .models import Instituicao

from django.utils.html import format_html

@admin.register(Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('nome_da_instituicao', 'cnpj', 'tempo_de_fundacao', 'publico_alvo', 'capacidade', 'mostrar_link_abrigo')
    search_fields = ('nome_da_instituicao', 'publico_alvo')
    list_filter = ('publico_alvo',)
    fields = ('nome_da_instituicao', 'cnpj', 'tempo_de_fundacao', 'publico_alvo', 'capacidade', 'link_abrigo')

    def mostrar_link_abrigo(self, obj):
        if obj.link_abrigo:
            return format_html('<a href="{}" target="_blank">{}</a>', obj.link_abrigo, obj.link_abrigo)
        return '-'
    
    mostrar_link_abrigo.short_description = 'Link Abrigo' 
    
@admin.register(QRCodePixFelicidade)
class QRCodePixFelicidadeAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if QRCodePixFelicidade.objects.exists():
            return False
        return super().has_add_permission(request)
        
admin.site.index_title = "Painel de Controle Felicidade Compartilhada"

admin.site.register(Atividade)
admin.site.register(RelatorioAnual)
admin.site.register(QRCodePixParceiros)

from django.contrib import admin
from .models import Polo, Indicador, Pergunta, Avaliacao, Resposta


@admin.register(Polo)
class PoloAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cidade', 'responsavel', 'criado_em']
    search_fields = ['nome', 'cidade']


@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    list_display = ['numero', 'nome', 'condicional']
    ordering = ['numero']


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ['indicador', 'ordem', 'texto', 'peso']
    list_filter = ['indicador']
    ordering = ['indicador__numero', 'ordem']


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['polo', 'data', 'status', 'score_total']
    list_filter = ['status', 'polo']


@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ['avaliacao', 'pergunta', 'valor']
    list_filter = ['valor']
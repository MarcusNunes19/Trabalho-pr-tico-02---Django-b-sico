from django.contrib import admin
from .models import Prato, Categoria_prato
from .models import Jogo, RegistroUsoJogo

# Register your models here.

@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):
    list_display = ('nome_prato', 'categoria', 'preco_prato', 'tipico')
    list_filter = ('categoria', 'tipico')
    search_fields = ('nome_prato', 'descricao_prato', 'ingredientes_prato')

@admin.register(Categoria_prato)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome_categoria', 'descricao_categoria')

class RegistroUsoJogoInline(admin.TabularInline):
    model = RegistroUsoJogo
    extra = 1  # mostra 1 linha vazia pra adicionar novos registros
    fields = ('quantidade',) 

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'total_copias', 'copias_em_uso', 'copias_disponiveis')
    search_fields = ('nome', 'tipo')
    inlines = [RegistroUsoJogoInline]

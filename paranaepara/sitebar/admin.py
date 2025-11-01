from django.contrib import admin
from .models import Prato, Categoria_prato

# Register your models here.

@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):
    list_display = ('nome_prato', 'categoria', 'preco_prato', 'tipico')
    list_filter = ('categoria', 'tipico')
    search_fields = ('nome_prato', 'descricao_prato', 'ingredientes_prato')

@admin.register(Categoria_prato)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome_categoria', 'descricao_categoria')
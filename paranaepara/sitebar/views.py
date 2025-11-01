from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Categoria_prato, Prato

# Create your views here.

def index(request):
    template = loader.get_template('sitebar/index.html')
    return HttpResponse(template.render())

def cardapio_comida(request):
    categorias = Categoria_prato.objects.filter(pratos__tipico=False).distinct()
    pratos = Prato.objects.order_by('categoria__nome_categoria', 'nome_prato')
    return render(request, 'sitebar/cardapio-comida.html', {
        'categorias': categorias,
        'pratos': pratos
    })

def cardapio_tipica(request):
    categorias = Categoria_prato.objects.filter(pratos__tipico=True).distinct()
    pratos = Prato.objects.order_by('categoria__nome_categoria', 'nome_prato')
    return render(request, 'sitebar/cardapio-tipicas.html', {
        'categorias': categorias,
        'pratos': pratos
    })

def catalogo_jogo(request):
    template = loader.get_template('sitebar/catalogo-jogos.html')
    return HttpResponse(template.render())

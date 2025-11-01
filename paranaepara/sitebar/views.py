from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Categoria_prato, Prato

# Create your views here.

def index(request):
    template = loader.get_template('sitebar/index.html')
    return HttpResponse(template.render())

def cardapio_comida(request):
    categorias = Categoria_prato.objects.all()
    pratos = Prato.objects.filter(disponibilidade=True).order_by('categoria__nome_categoria', 'nome_prato')
    return render(request, 'sitebar/cardapio-comida.html', {
        'categorias': categorias,
        'pratos': pratos
    })

def cardapio_tipica(resquest):
    template = loader.get_template('sitebar/cardapio-tipicas.html')
    return HttpResponse(template.render())

def catalogo_jogo(resquest):
    template = loader.get_template('sitebar/catalogo-jogos.html')
    return HttpResponse(template.render())

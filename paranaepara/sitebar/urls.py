from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('cardapio/comida/', views.cardapio_comida, name='cardapio_comida'),
    path('cardapio/tipicas/', views.cardapio_tipica, name='cardapio_tipica'),
    path('catalogo/jogos/', views.catalogo_jogo, name='catalogo_jogo'),
]
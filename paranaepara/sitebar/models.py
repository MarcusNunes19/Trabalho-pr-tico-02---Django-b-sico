from django.db import models

# Create your models here.

class Categoria_prato(models.Model):
    nome_categoria = models.CharField(max_length=50)
    descricao_categoria = models.TextField(blank=True)

    def __str__(self):
        return self.nome_categoria
    

class Prato(models.Model):
    categoria = models.ForeignKey(Categoria_prato, on_delete=models.CASCADE, related_name='pratos')
    nome_prato = models.CharField(max_length=50)
    descricao_prato = models.TextField(blank=True)
    ingredientes_prato = models.TextField(blank=True)
    preco_prato = models.DecimalField(max_digits=6, decimal_places=2)
    imagem_prato = models.ImageField(upload_to='imagens/', blank=True, null=True)
    tipico = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome_prato} ({self.categoria.nome_categoria})"
    
class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    jogadores = models.CharField(max_length=20, help_text="Ex: 2-6 jogadores")
    tempo_partida = models.CharField(max_length=50)
    descricao_curta = models.CharField(max_length=200)
    descricao_detalhada = models.TextField()
    imagem = models.ImageField(upload_to='jogos/', blank=True, null=True)
    total_copias = models.PositiveIntegerField(default=1)

    def copias_em_uso(self):
        return sum(registro.quantidade for registro in self.registros.all())   
    
    def copias_disponiveis(self):
        return max(self.total_copias - self.copias_em_uso(), 0)
    
    def __str__(self):
        return self.nome
    
class RegistroUsoJogo(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE, related_name='registros')
    quantidade = models.PositiveIntegerField(default=1)
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantidade} cópias de {self.jogo.nome} em uso"
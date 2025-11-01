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
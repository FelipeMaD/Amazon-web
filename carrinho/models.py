from django.db import models
from produtos.models import Produtos


# Create your models here.

class Carrinho(models.Model):
    image = models.ImageField(upload_to='carrinho/', null=True, blank=True)
    titulo = models.CharField(max_length=300, null=True)
    descricao = models.TextField(null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    cor = models.CharField(max_length=100, null=True)


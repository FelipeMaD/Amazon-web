from django.db import models

# Create your models here.

class Produtos(models.Model):
    classe = models.CharField(max_length=100, null=True, blank=True)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    titulo = models.CharField(max_length=200, null=True, blank=True)
    preco = models.CharField(max_length=20, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.titulo
    
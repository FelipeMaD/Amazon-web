from django.db import models

# Create your models here.

class Produtos(models.Model):
    classe = models.CharField(max_length=100, null=True)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    titulo = models.CharField(max_length=200)
    preco = models.CharField(max_length=20)
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.titulo
    
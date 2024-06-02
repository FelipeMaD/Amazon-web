from django.db import models

# Create your models here.

class Comprar_novamente(models.Model):
    produtocomprarnovamente = models.ForeignKey('carrinho.Carrinho', on_delete=models.CASCADE)
    
# class Comprar_novamente(models.Model):
    
#     imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
#     titulo = models.CharField(max_length=200,null=True)
#     preco = models.CharField(max_length=20,null=True)
#     descricao = models.TextField(null=True)
#     data = models.DateTimeField(auto_now_add=True,null=True)


# def __str__(self):
#     return self.titulo
from django.http import HttpResponse
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from produtos.models import Produtos
from .models import Carrinho

def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produtos, pk=produto_id)
    carrinho = Carrinho(produtocarrinho=produto)
    carrinho.save()
    return redirect('carrinho')


# def exibir_carrinho(request):
#     itens_carrinho = Carrinho.objects.all()
#     return render(request, 'carrinho2.html', {'itens_carrinho': itens_carrinho})


class CarrinhoListView(ListView):
    model = Carrinho
    template_name = 'carrinho2.html'
    context_object_name = 'carrinho'
    
def delete_carrinho(request, carrinho_id):
    carrinho = Carrinho.objects.get(pk=carrinho_id)
    carrinho.delete()
    return redirect('carrinho')  

    
    
  

'''
# Create your views here.
def carrinho(request):
    return render(request, 'carrinho.html')'''
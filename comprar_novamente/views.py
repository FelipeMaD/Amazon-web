from django.shortcuts import render , redirect
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView, TemplateView
from .models import Comprar_novamente
from django.shortcuts import get_object_or_404
from carrinho.models import Carrinho
from django.http import HttpResponse
from carrinho.views import delete_carrinho

# Create your views here.
class Comprar_novamenteListView(ListView):
    model = Comprar_novamente
    template_name = 'comprar_novamente.html'
    context_object_name = 'comprar_novamente'

def add_comprar_novamente(request, produto_id):
    produto = get_object_or_404(Carrinho, pk=produto_id)
    comprar_novamente = Comprar_novamente(produtocomprarnovamente=produto)
    comprar_novamente.save()

    return redirect('comprar_novamente')
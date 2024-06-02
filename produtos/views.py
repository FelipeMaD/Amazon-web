from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Produtos
from django.views.generic import ListView, DetailView
from django.db.models import Q

class ProdutosListView(ListView):
    model = Produtos
    template_name = 'produtos.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = super().get_queryset()
        if query:
            queryset = queryset.filter(titulo__icontains=query)
        return queryset


class ProdutosDetailView(DetailView):
    model = Produtos
    template_name = 'detalhesProdutos.html'


'''
def produtos(request):
    produtos = Produtos.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})'''
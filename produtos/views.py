from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Produtos
from django.views.generic import ListView

# Create your views here.

class ProdutosListView(ListView):
    model = Produtos
    template_name = 'produtos.html'
    context_object_name = 'produtos'
    '''
    def get_queryset (self):
        queryset = super().get_queryset()
        query = self.request.GET.get('')
        if query:
            queryset = queryset.filter( title__icontains =query)
            return queryset'''
'''
def produtos(request):
    produtos = Produtos.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})'''
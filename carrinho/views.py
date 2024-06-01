from django.http import HttpResponse
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from django.urls import reverse_lazy
from carrinho.models import Carrinho


class CarrinhoListView(ListView):
    model = Carrinho
    template_name = 'carrinho2.html'
    context_object_name = 'carrinho'

    
  

'''
# Create your views here.
def carrinho(request):
    return render(request, 'carrinho.html')'''
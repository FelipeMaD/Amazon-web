from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Produtos


# Create your views here.
def produtos(request):
    produtos = Produtos.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})
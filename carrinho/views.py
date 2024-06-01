from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.
def carrinho(request):
    return render(request, 'carrinho.html')
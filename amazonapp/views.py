from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import TempModel
# from produtos.models import Produtos


# Create your views here.
# def home(request):
#         return render(request, 'home.html')

class homeView(ListView):
    model = TempModel
    template_name = 'home.html'
    context_object_name = 'home'

# def verOfertasDoDia(request):
#     produtos = Produtos.objects.filter(classe="40")
#     return render(request, 'produtos.html', {'produtos': produtos})
#     # return HttpResponse("Oferta do dia")
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Create your views here
class loginView(TemplateView):
    template_name = 'login.html'
    context_object_name = 'login'

def login_view(request):
    return HttpResponse('teste')
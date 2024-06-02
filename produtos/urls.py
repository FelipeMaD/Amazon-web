from django.urls import path
from . import views
from django.views.generic import ListView
from .views import ProdutosListView, ProdutosDetailView
from carrinho.views import adicionar_ao_carrinho


urlpatterns = [
    path('', ProdutosListView.as_view(), name='produtos'),
    path('<int:pk>/', ProdutosDetailView.as_view(), name='detalhes'),
    path('carrinho/adicionar_ao_carrinho/<int:produto_id>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    ]
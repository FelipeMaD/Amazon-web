from django.urls import path
from . import views
from django.views.generic import ListView
from .views import ProdutosListView, ProdutosDetailView

urlpatterns = [
    path('', ProdutosListView.as_view(), name='produtos'),
    path('<int:pk>/', ProdutosDetailView.as_view(), name='detalhes')
    ]
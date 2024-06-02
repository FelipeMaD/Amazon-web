from django.urls import path
from . import views
from django.views.generic import ListView
from .views import ProdutosListView

urlpatterns = [
    path('', ProdutosListView.as_view(), name='produtos'),
    ]
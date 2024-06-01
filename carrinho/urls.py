from django.urls import path
from . import views
from . views import CarrinhoListView


urlpatterns = [
    path('', CarrinhoListView.as_view(), name='carrinho'),
]
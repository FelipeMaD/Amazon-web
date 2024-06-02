from django.urls import path
from . import views
from . views import CarrinhoListView
from comprar_novamente.views import add_comprar_novamente


urlpatterns = [
    # path('', views.exibir_carrinho, name='exibir_carrinho'),
    path('', CarrinhoListView.as_view(), name='carrinho'),
    path('comprar_novamente/add_comprar_novamente/<int:produto_id>/', add_comprar_novamente, name='add_comprar_novamente'),
]
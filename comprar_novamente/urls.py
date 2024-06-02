from django.urls import path
from . import views
from . views import Comprar_novamenteListView


urlpatterns = [
    path('', Comprar_novamenteListView.as_view(), name='comprar_novamente'),
]
from django.urls import path
from . import views
from django.views.generic import ListView
from .views import homeView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', homeView.as_view(), name='home'),
    
    ]
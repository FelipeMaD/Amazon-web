from django.urls import path
from . import views
from django.views.generic import ListView
from .views import loginView

urlpatterns = [
    path('', views.login_view(), name='login')
    ]
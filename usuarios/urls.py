from django.urls import path
from . import views

urlpatterns = [
    path('perfil/', views.perfil, name = 'perfil'),
    path('login/', views.logar, name = 'login'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('gerarNota/', views.gerarNota, name='gerarNota'),
    path('notasGeradas/', views.notasGeradas, name='notasGeradas'),
    path('notasGeradas/enviarNota', views.enviarNota, name='enviarNota'),
]
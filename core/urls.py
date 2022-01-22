from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('gerarNota/', views.gerarNota, name='gerarNota'),
    path('notasGeradas/', views.notasGeradas, name='notasGeradas'),
    path('ModalEnviarNota/<int:idNFE>', views.abrirModalEnviarNota, name='abrirModalEnviarNota'),
    #path('ModalEnviarNotaV2/<int:idNFE>', views.abrirModalEnviarNotaV2.get_form_kwargs()),
]
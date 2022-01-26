from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('gerarNota/', views.gerarNota, name='gerarNota'),
    path('notasGeradas/', views.notasGeradas, name='notasGeradas'),
    path('verificarNota/<int:idNFE>', views.mostrarDadosDaNota, name="verificarNota"),
    path('enviarJson/<int:idNFE>', views.enviarJsonPlugNotas, name='enviarJsonPlugNotas'),
    path('statusNota/<str:idRetorno>', views.pesquisarStatus, name='pesquisarStatus'),
    path('baixarPDF/<str:idRetorno>', views.baixarPDF, name="baixarPDF")
]
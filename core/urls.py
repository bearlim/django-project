from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('gerarNota/', views.gerarNota, name='gerarNota'),
    path('notasGeradas/', views.notasGeradas, name='notasGeradas'),
    path('verificarNota/<int:idNFE>', views.mostrarDadosDaNota, name="verificarNota"),
    path('enviarJson/<int:idNFE>', views.enviarJsonPlugNotas, name='enviarJsonPlugNotas'),
    path('statusNota/<str:idRetorno>', views.pesquisarStatus, name='pesquisarStatus'),
    path('baixarPDF/<str:idRetorno>', views.baixarPDF, name="baixarPDF"),
    path('visualizarXML/<str:idRetorno>', views.baixarXML, name="baixarXML"),
    path('solicitarCancelamento/<str:idRetorno>', views.solicitarCancelamento, name="solicitarCancelamento"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.PDF_ROOT, document_root=settings.PDF_ROOT)
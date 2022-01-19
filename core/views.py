from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.shortcuts import render

# Importando model
from .models import tbNOTAFISCAL as NF
# Importando form
from .forms import gerarNotaFiscal

def index(request):
    return render(request, 'index.html')

# Função irá trazer modal para realizar a emissão de notas
def gerarNota(request):

    if request.method == 'POST':
        form = gerarNotaFiscal(request.POST)
    else:
        form = gerarNotaFiscal()
    
    context = {
        'form': form,
    }
    return render(request, 'crudGerarNotas.html', context)

# Função irá puxar todas as notas que estão salvas no banco de dados
def notasGeradas(request):
    # Buscando as notas
    notasGeradas = NF.objects.all()
    # Definindo o nome do template
    template_name = 'crudNotasGeradas.html'
    # Adicionando contexto
    context = {
        'notasGeradas': notasGeradas
    }
    # Retornando os parâmetros do Request
    return render(request, template_name, context)
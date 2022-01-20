from distutils.command.install_egg_info import safe_name
from multiprocessing import context
from django.shortcuts import render

# Importando model
from .models import tbNOTAFISCAL as NF
# Importando form
from .forms import FormGerarNota
from .control import *

def index(request):
    return render(request, 'index.html')

# Função irá trazer modal para realizar a emissão de notas
def gerarNota(request):
    context = {}
    if request.method == 'POST':
        form = FormGerarNota(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(form.visible_fields())
            json = montarJson(form)
            form = FormGerarNota()
    else:
        context = {
            'form': FormGerarNota()
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
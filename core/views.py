from django.shortcuts import render, redirect

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
        if form.is_valid():            
            formX = form.save()
            print(formX.idNFE)
            json = montarJson(formX)
            form = FormGerarNota()
            return  redirect('/notasGeradas/')
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
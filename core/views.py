from asyncio.windows_events import NULL
from re import template
from this import d
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .control import Gerarjson
from django.urls import reverse
from django.views.generic import DetailView
from django.views.decorators.csrf import csrf_exempt
from django.forms import modelformset_factory as FS
from .models import tbNOTAFISCAL as NF
from .forms import FormGerarNota, global_fields, global_widgets

app_name = "core"

def index(request):
    return render(request, 'index.html')

# Função irá trazer modal para realizar a emissão de notas
def gerarNota(request):
    context = {}
    if request.method == 'POST':
        form = FormGerarNota(request.POST)                        
        if form.is_valid():            
            formX = form.save()                        
            form = FormGerarNota()
            return  redirect('/notasGeradas/')
    else:        
        context = {
            'form': FormGerarNota()
        }
    
    return render(request, 'crudGerarNotas.html', context)

# Função irá puxar todas as notas que estão salvas no banco de dados
def notasGeradas(request, idNFE=NULL):
    notasGeradas = NF.objects.all()    
    template_name = 'crudNotasGeradas.html'
    formX = FS(NF, fields=global_fields, widgets=global_widgets, exclude=('idNFE',))    
    form = formX(queryset=NF.objects.filter(idNFE=idNFE))
    context = {
        'notasGeradas': notasGeradas,
        'form': form[0]
    }

    return render(request, template_name, context)

@csrf_exempt
def mostrarDadosDaNota(request, idNFE):
    formX = FS(NF, fields=global_fields, widgets=global_widgets, exclude=('idNFE',))    
    form = formX(queryset=NF.objects.filter(idNFE=idNFE))

    return render(request, 'modalEnviarNota.html', {'form':form})


@csrf_exempt
def enviarJsonPlugNotas(request, idNFE):
    NFS = NF.objects.filter(idNFE=idNFE)
    json = Gerarjson(NFS)

    return redirect("/notasGeradas/")


def enviarNota(request, idNFE):
    context = {}
    NFE = NF.objects.get(idNFE=idNFE)
    json = Gerarjson(NFE)

    form = FormGerarNota(request.POST or None, instance=NFE)

    if form.is_valid():        
        return redirect('/notasGeradas/')
    else:
        context = {
            'form': FormGerarNota()
        }
    
    return render(request, 'crudNotasGeradas.html', context)
        
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .control import *
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.forms import modelformset_factory as FS
from .models import tbNOTAFISCAL as NF
from .forms import FormGerarNota, global_fields, global_widgets
from django.conf import settings

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
def notasGeradas(request, idNFE=None):
    notasGeradas = NF.objects.all()    
    template_name = 'crudNotasGeradas.html'
    formX = FS(NF, fields=global_fields, widgets=global_widgets, exclude=('idNFE',))    
    form = formX(queryset=NF.objects.filter(idNFE=idNFE))
    context = {
        'notasGeradas': notasGeradas
    }

    return render(request, template_name, context)

@csrf_exempt
def mostrarDadosDaNota(request, idNFE):
    formX = FS(NF, fields=global_fields, widgets=global_widgets, exclude=('idNFE',))    
    form = formX(queryset=NF.objects.filter(idNFE=idNFE))

    return render(request, 'modalVerificarDadosDaNota.html', {'form':form[0]})


@csrf_exempt
def enviarJsonPlugNotas(request, idNFE):
    NFS = NF.objects.get(idNFE=idNFE)
    json = Gerarjson(NFS)
    idRetorno = enviarJson(json)
    inserirIdRetorno(idRetorno, NFS)
        
    return redirect("/notasGeradas/")

@csrf_exempt
def pesquisarStatus(request, idRetorno):
    NFS = NF.objects.get(idRetorno=idRetorno)
    dsStatus = verificarStatusNota(idRetorno)
    NFS.dsStatus = dsStatus
    NFS.save()

    return redirect('/notasGeradas/')


@csrf_exempt
def baixarPDF(request, idRetorno):
    NFS = NF.objects.get(idRetorno=idRetorno)
    urlPDF = getPDF(idRetorno)
    NFS.urlPDF = urlPDF
    NFS.save()

        
from re import template
from this import d
from django.shortcuts import render, redirect
from .control import Gerarjson
from django.urls import reverse
from django.views.generic import DetailView
from django.views.decorators.csrf import csrf_exempt
from .models import tbNOTAFISCAL as NF
from .forms import FormGerarNota

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

@csrf_exempt
def abrirModalEnviarNota(request, idNFE):
    context = {}
    
    form = NF.objects.get(idNFE = idNFE)
    template_name = 'crudNotasGeradas.html'

    context = {
        'form': form
    }
    return render(request, template_name, context)

class abrirModalEnviarNotaV2(DetailView):
    model = NF
    form = FormGerarNota

    def get_form_kwargs(self):
        kwargs = super(abrirModalEnviarNotaV2, self).get_form_kwargs()
        kwargs['user'] = self.request.user.username
        return kwargs

    def post(self, request, *args, **kwargs):
        form = FormGerarNota(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("abrirModalEnviarNotaV2", args=[post.pk]))


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
        
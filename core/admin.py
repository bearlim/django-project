from re import search
from django.contrib import admin
from .models import tbNOTAFISCAL, tbNOTAFISCALERRO

# Modificando o crud do admin
class Modificacoes(admin.ModelAdmin):
    # Irá mostrar esse campos na tabela de exibição 
    list_display = ['cdServico', 'dsDiscriminacao']
    # Irá criar um input para pesquisar algo digitado, que será pesquisado apartir dos itens contidos na lista
    search_fields = ['cdServico', 'cdCPFTomador']

# Classe modificacoes sendo chamada 
admin.site.register(tbNOTAFISCAL, Modificacoes)
admin.site.register(tbNOTAFISCALERRO)
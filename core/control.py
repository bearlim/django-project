import requests

def montarJson(form):
    print(form.cleaned_data['cdServico'])
    print(form.data['idNFE'])
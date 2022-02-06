from django.http import response
import json
import urllib3
from django.conf import settings
import os

urlAPI = "https://api.sandbox.plugnotas.com.br/nfse"
headerAPI = {'x-api-key': '2da392a6-79d2-4304-a8b7-959572c7e44d', 'Content-Type': 'application/json'}
http = urllib3.PoolManager()


def Gerarjson(NFS):
    jsonEnviar = [
        {
        "idIntegracao": NFS.idNFE,
        "prestador": 
            {"cpfCnpj": NFS.cdCNPJPrestador}
        ,
        "tomador": 
            {
                "cpfCnpj": NFS.cdCPFTomador,
                "razaoSocial": NFS.nmTomador,
                "endereco": 
                    {
                        "descricaoCidade": NFS.cdCidadeTomador,
                        "cep": NFS.cdCEPTomador,
                        "tipoLogradouro": NFS.dsTipoLogradouroTomador,
                        "logradouro": NFS.dsEnderecoTomador,
                        "tipoBairro": NFS.dsTipoBairroTomador,
                        "codigoCidade": NFS.cdCidadeTomador,
                        "estado": NFS.sgEstadoTomador,
                        "numero": NFS.nrEnderecoTomador,
                        "bairro": NFS.dsBairroTomador
                    }
            },
        "servico": [{
            "codigo": NFS.cdServico,
            "codigoTributacao": NFS.cdTributacao,
            "discriminacao": NFS.dsDiscriminacao,
            "cnae": NFS.cdCNAE,
            "iss": {
                "tipoTributacao": 7,
                "exigibilidade": 1,
                "aliquota": 3
            },
            "valor": {
                "servico": NFS.vrServico,
                "liquido": NFS.vrLiquido
            }
        }
        ]
    }
    ]
    jsonFormatador = json.dumps(jsonEnviar)
    return jsonFormatador


def enviarJson(jsonFormatado):
    r = http.request(
        "POST", 
        urlAPI,
        body=jsonFormatado,
        headers=headerAPI
        )

    json_obj = json.loads(r.data)
    idRetorno = json_obj.get("documents")[0].get("id")
    
    return idRetorno


def inserirIdRetorno(idRetorno, NFS):
    NFS.idRetorno = idRetorno
    NFS.save()


def verificarStatusNota(idRetorno):
    r = http.request(
        "GET", 
        urlAPI + '/' + idRetorno,
        headers=headerAPI
    )

    json_obj = json.loads(r.data)
    dsStatus = json_obj.get('status')

    return dsStatus


def getPDF(idRetorno):
    direct = str(settings.BASE_DIR) + '/staticfiles/pdfNotas/'
    urlPDF = f"{direct}{idRetorno}.pdf"
    url = ""
    
    if os.path.isdir(direct):
        r = http.request(
            "GET",
            f"{urlAPI}/pdf/{idRetorno}",
            headers=headerAPI
        )
        with open(urlPDF, "wb") as pdf:
            pdf.write(r.data)
        return urlPDF
    else: 
        os.mkdir(f"{settings.BASE_DIR}/staticfiles/pdfNotas")
        r = http.request(
            "GET",
            f"{urlAPI}/pdf/{idRetorno}",
            headers=headerAPI
        )
        with open(urlPDF, "wb") as pdf:
            pdf.write(r.data)
        return urlPDF

def get_xml(idRetorno):
    direct = str(settings.BASE_DIR) + '/staticfiles/xmlNotas/'
    urlXML = f"{direct}{idRetorno}.xml"
    url = ""

    if os.path.isdir(direct):
        r = http.request(
            "GET",
            f"{urlAPI}/xml/{idRetorno}",
            headers=headerAPI
        )
        with open(urlXML, "wb") as xml:
            xml.write(r.data)
        return urlXML
    else:
        os.mkdir(f"{settings.BASE_DIR}/staticfiles/xmlNotas")
        r = http.request(
            "GET",
            f"{urlAPI}/xml/{idRetorno}",
            headers=headerAPI
        )
        with open(urlXML, "wb") as xml:
            xml.write(r.data)
        return urlXML

from django.http import response
import requests
import json
import urllib3

urlAPI = "https://api.sandbox.plugnotas.com.br/nfse"
headerAPI = {'x-api-key': '2da392a6-79d2-4304-a8b7-959572c7e44d', 'Content-Type': 'application/json'}

class JsonRetorno:
    
    def __init__(self, documents=None, message=None, protocol=None, erro=None, data=None):
        self.idRetorno = documents[0]['id']
        self.message = message
        self.protocol = protocol
    
    @classmethod
    def deserialize_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_string)
    

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
    response = requests.post(urlAPI, json=jsonFormatado, headers=headerAPI)
    try:
        jsonRetornoFormatado = JsonRetorno.deserialize_json(response.content)
    except:
        pass    

    idRetorno = jsonRetornoFormatado.idRetorno

    return idRetorno

def enviarJsonV2(jsonFormatado):
    http = urllib3.PoolManager()
    r = http.request(
        "POST", 
        urlAPI,
        body=jsonFormatado,
        headers=headerAPI
        )

    jsonRetornoFormatado = JsonRetorno.deserialize_json(r.data.decode('utf-8'))

    idRetorno = jsonRetornoFormatado.idRetorno


def inserirIdRetorno(idRetorno, NFS):
    NFS.idRetorno = idRetorno
    NFS.save()
from django.http import response
import requests
import json

urlAPI = "https://api.sandbox.plugnotas.com.br/nfse"
headerAPI = {'x-api-key': '2da392a6-79d2-4304-a8b7-959572c7e44d'}

def Gerarjson(NFS):
    json = {
        "idIntegracao": NFS.idNFE,
        "prestador": [
            {"cpfCnpj": NFS.cdCNPJPrestador}
        ],
        "tomador": [
            {
                "cpfCnpj": NFS.cdCPFTomador,
                "razaoSocial": NFS.nmTomador,
                "endereco": [
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
                ]
            }
        ],
        "servico": [{
            "codigo": NFS.cdServico,
            "codigoTributacao": NFS.cdTributacao,
            "discriminacao": NFS.dsDiscriminacao,
            "cnae": NFS.cdCNAE,
            "iss": [{
                "tipoTributacao": 7,
                "exigibilidade": 1,
                "aliquota": 3
            }],
            "valor": [{
                "servico": NFS.vrServico,
                "liquido": NFS.vrLiquido
            }]
        }]

    }
    jsonFormatado = json.dumps(json)
    return jsonFormatado



def enviarJson(jsonFormatado):
    response = requests.post(urlAPI, jsonFormatado, headers=headerAPI)
    jsonRetornoFormatado = json.loads(response)

    idRetorno = jsonRetornoFormatado['documents']['id']

    return idRetorno
from django.http import response
import requests
import json

urlAPI = "https://api.sandbox.plugnotas.com.br/nfse"
headerAPI = {'x-api-key': '2da392a6-79d2-4304-a8b7-959572c7e44d'}

def Gerarjson(form):
    json = {
        "idIntegracao": form.idNFE,
        "prestador": [
            {"cpfCnpj": form.cdCNPJPrestador}
        ],
        "tomador": [
            {
                "cpfCnpj": form.cdCPFTomador,
                "razaoSocial": form.nmTomador,
                "endereco": [
                    {
                        "descricaoCidade": form.cdCidadeTomador,
                        "cep": form.cdCEPTomador,
                        "tipoLogradouro": form.dsTipoLogradouroTomador,
                        "logradouro": form.dsEnderecoTomador,
                        "tipoBairro": form.dsTipoBairroTomador,
                        "codigoCidade": form.cdCidadeTomador,
                        "estado": form.sgEstadoTomador,
                        "numero": form.nrEnderecoTomador,
                        "bairro": form.dsBairroTomador
                    }
                ]
            }
        ],
        "servico": [{
            "codigo": form.cdServico,
            "codigoTributacao": form.cdTributacao,
            "discriminacao": form.dsDiscriminacao,
            "cnae": form.cdCNAE,
            "iss": [{
                "tipoTributacao": 7,
                "exigibilidade": 1,
                "aliquota": 3
            }],
            "valor": [{
                "servico": form.vrServico,
                "liquido": form.vrLiquido
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
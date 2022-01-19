from tabnanny import verbose
from django.db import models

class NotaFiscalManager(models.Manager):
    def pesquisar(self, query):
        return self.get_queryset().filter(
            models.Q(dsDiscriminacao__icontains=query) | \
            models.Q(cdCPFTomador__icontains=query)
        )

# Create your models here.
class tbNOTAFISCAL(models.Model):
    idNFE = models.IntegerField(primary_key=True)
    idRetorno = models.CharField(null=True, max_length=255)

    # Dados de serviço
    cdServico = models.CharField('Código de Serviço',max_length = 150)
    cdTributacao = models.CharField('Código de Tributação', max_length = 150, blank=True)
    dsDiscriminacao = models.CharField(max_length = 150)
    cdCNAE = models.CharField('Código CNAE',max_length = 150, blank=True)    
    vrServico = models.FloatField('Valor do Serviço')
    vrLiquido = models.FloatField('Valor líquido do Serviço')

    # Dados do prestador
    cdCNPJPrestador = models.CharField('CNPJ do Prestador',max_length = 255)

    #Dados do Tomador    
    cdCPFTomador = models.CharField('CPF do Tomador', max_length = 255)
    cdCEPTomador = models.CharField('CEP do Tomador', max_length = 150)
    dsTipoLogradouroTomador = models.CharField('Tipo logradouro do Tomador', max_length = 50)
    dsEnderecoTomador = models.CharField('Endereço do Tomador', max_length = 255)
    dsTipoBairroTomador = models.CharField('Tipo do bairro do Tomador', max_length = 100)
    cdCidadeTomador = models.CharField('Cidade do Tomador',max_length = 150)
    sgEstadoTomador = models.CharField('Estado do Tomador', max_length = 50)
    nrEnderecoTomador = models.IntegerField('Número do endereço do Tomador')    
    dsBairroTomador = models.CharField('Bairro do Tomador', max_length = 150) 
    urlPDF = models.CharField(max_length = 255, null=True, blank=True)
    urlXML = models.CharField(max_length = 255, null=True, blank=True)    
    
    #Dados da nota
    dtEmissao = models.DateTimeField(auto_now_add=True, null=True)
    dsStatus = models.CharField(max_length=100, null=True)
    flErro = models.BinaryField(null=True)

    objects = NotaFiscalManager()

    def __str__(self) -> str:
        return self.dsDiscriminacao

    class Meta:
        verbose_name = "Nota Fiscal"
        verbose_name_plural = "Notas Fiscais"

class tbNOTAFISCALERRO(models.Model):
    idErro = models.IntegerField(primary_key=True)

    #Dados do Erro 
    idNFE = models.IntegerField()
    dsErro = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.dsErro
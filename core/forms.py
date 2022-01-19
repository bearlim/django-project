from django import forms

class gerarNotaFiscal(forms.Form):
    cdServico = forms.CharField(label='Código de Serviço', max_length=150, \
        widget=forms.TextInput(attrs={'placeholder': 'Código de Serviço', 'class': 'form-control'}))
    cdTributacao = forms.CharField(label='Código de Tributação', max_length=150, \
        widget=forms.TextInput(attrs={'placeholder': 'Código de Tributação', 'class': 'form-control'}), required=False)
    dsDiscriminacao = forms.CharField(label='Discriminação', max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cdCNAE = forms.CharField(label='Código CNAE', max_length=150, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    vrServico = forms.FloatField(label='Valor do Serviço', widget=forms.TextInput(attrs={'placeholder': 'R$0,00', 'class': 'inputMoney form-control'}))
    vrLiquido = forms.FloatField(label='Valor líquido do Serviço', widget=forms.TextInput(attrs={'class': 'inputMoney', 'class': 'form-control'}))

    # Dados do prestador
    cdCNPJPrestador = forms.CharField(label='CNPJ do Prestador', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    # Dados do Tomador
    cdCPFTomador = forms.CharField(label='CPF do Tomador', max_length = 255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cdCEPTomador = forms.CharField(label='CEP do Tomador', max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    dsTipoLogradouroTomador = forms.CharField(label='Tipo logradouro do Tomador', max_length = 50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    dsEnderecoTomador = forms.CharField(label='Endereço do Tomador', max_length = 255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    dsTipoBairroTomador = forms.CharField(label='Tipo do bairro do Tomador', max_length = 100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cdCidadeTomador = forms.CharField(label='Cidade do Tomador',max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sgEstadoTomador = forms.CharField(label='Estado do Tomador', max_length = 50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nrEnderecoTomador = forms.IntegerField(label='Número do endereço do Tomador', widget=forms.TextInput(attrs={'class': 'form-control'}))
    dsBairroTomador = forms.CharField(label='Bairro do Tomador', max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control'})) 
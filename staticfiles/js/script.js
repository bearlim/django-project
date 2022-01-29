// Evento para enviar o id para o modal
$('BODY').on('click', '#tbNotasGeradas #btVerificarNota', function () {
    let idNFE = $(this).attr('data-id');
        
    $.ajax({
        type: "GET",
        url: "/verificarNota/" + idNFE,
        success: function (response) {
            
        }
    });
});



// Evento para enviar requisão para envio de nota 
$('BODY').on('click', '#tbNotasGeradas #btEnviarJson', function(){
    let idNFE = $(this).attr('data-id');

    $.ajax({
        type: "POST",
        url: "/enviarJson/" + idNFE,
        success: function (response) {
            
        }
    });
});


// Evento para enviar requisção de status 
$('BODY').on('click', '#tbNotasGeradas #btConsulta', function(){
    let idRetorno = $(this).attr('data-idretorno');

    $.ajax({
        type: "GET",
        url: '/statusNota/' + idRetorno,
        success: function(response){
            document.location.reload(true);
        }
    });
});

// Evento para baixar PDF 
$('BODY').on('click', '#tbNotasGeradas #btBaixarPDF', function(){
    let idRetorno = $(this).attr('data-idretorno');

    $.ajax({
        type: "GET",
        url: "/baixarPDF/" + idRetorno,
        success: function(response){
            document.location.reload(true);
        }
    });
});

// Evento para visualizar o PDF
$('BODY').on('click', '#tbNotasGeradas #btVisualizarPDF', function(){
    let idRetorno = $(this).attr('data-idretorno');

    $.ajax({
        type: "GET",
        url: "/visualizarPDF/" + idRetorno,
        success: function(response){
        }
    });
});

function mostrarNotificacao(tipo, titulo, texto) {
    var opts = {
        title: titulo,
        text: texto,
        addclass: 'stack-bottomright',
        styling: 'bootstrap',
    };
    switch (tipo) {
        case 'erro':
            opts.delay = '2800';
            opts.type = 'error';
            break;
        case 'info':
            opts.delay = '3000';
            opts.type = 'info';
            break;
        case 'sucesso':
            opts.delay = '900';
            opts.type = 'success';
            break;
    }
    $.pnotify(opts);
}
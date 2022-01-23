$('BODY').on('click', 'table#tbNotasGeradas #btConsulta', function () {
    let idNFE = $(this).attr('data-id');

    alert(idNFE);
});

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
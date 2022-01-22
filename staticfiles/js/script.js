$('BODY').on('click', 'table#tbNotasGeradas #btConsulta', function () {
    let idNFE = $(this).attr('data-id');

    alert(idNFE);
});

$('BODY').on('click', '#tbNotasGeradas #btEnviarJson', function () {
    let modal = $(this).attr('data-bs-target'),
        idNFE = $(this).attr('data-id');

    $.ajax({
        type: "GET",
        url: "/ModalEnviarNotaV2/" + idNFE,
        data: idNFE,        
        success: function (response) {
            $(modal).modal('show');
        }
    });
});
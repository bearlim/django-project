$('BODY').on('click', 'table#tbNotasGeradas #btConsulta', function () {
    let idNFE = $(this).attr('data-id');

    alert(idNFE);
});

$('BODY').on('click', '#tbNotasGeradas #btEnviarJson', function(){    
    // $.ajax({
    //     type: "POST",
    //     url: "/enviarNota",
    //     data: {
    //         idNFE: $(this).attr('data-id')
    //     },        
    //     success: function (response) {
            
    //     }
    // });

    $.post("/enviarNota/" + $(this).attr('data-id'), {idNFE: $(this).attr('data-id')},
        function (data, textStatus, jqXHR) {
            alert("funcionou");
        },        
    );
});
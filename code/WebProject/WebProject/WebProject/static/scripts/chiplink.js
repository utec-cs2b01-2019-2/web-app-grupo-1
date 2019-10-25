function linkchip()
{
    console.log("Comprobando. . .");
    var numero = $('#InputNumero').val();
    var credentials = JSON.stringify({ "numero": numero });
    console.log(credentials);
    $.ajax({
        url: '/addchips',
        type: 'post',
        dataType: 'json',
        contentType: 'application/json',
        data: credentials,
        success: function (data) {
            console.log("Linked!");
            var url = 'http://' + document.domain + ':' + location.port + '/home';
            $(location).attr('href', url);

        }
    })

}
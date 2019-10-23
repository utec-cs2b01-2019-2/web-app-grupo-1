function Register() {

        $('#action').append('<div class="text-center">Comprobando. . .</div>');
        console.log("Comprobando. . .");
        var email = $('#Email').val();
        var password = $('#Password').val();
        var confirmpassword = $('#confirmPassword').val();
        var name = $('#Name').val();
        var lastname = $('#Lastname').val();

    if (password === confirmpassword && password != 0 && confirmpassword !== 0) {

        var message = JSON.stringify({
            "Email": email,
            "Password": password,
            "Name": name,
            "Lastname": lastname,
            
        });
        $.ajax({
            url: '/user',
            type: 'POST',
            contentType: 'application/json',
            data: message,
            dataType: 'json',
            success: function (response) {
                $('#action').html("");
                if (response['status'] == 401) {
                    $('#action').append('<div class="text-center">Datos ingresados incorrectamente</div>');
                    console.log("Datos ingresados incorrectamente");
                }

                else {
                    console.log("Datos ingresados correctamente, pasa a loguearte en tu nueva cuenta");
                    $('#action').append('<div class="text-center">Datos ingresados correctamente, pasa a loguearte en tu nueva cuenta</div>');
                    var url = 'http://' + document.domain + ':' + location.port + '/login';
                    $(location).attr('href', url);
                }

            },
            error: function (response) {
                $('#action').html("");
                if (response['status'] == 401) {
                    $('#action').append('<div class="text-center">Datos ingresados incorrectamente</div>');
                    console.log("Datos ingresados incorrectamente");
                }
                else {
                    $('#action').append('<div class="text-center">Datos ingresados correctamente, pasa a loguearte en tu nueva cuenta</div>');
                    console.log("Datos ingresados correctamente, pasa a loguearte en tu nueva cuenta");
                    var url = 'http://' + document.domain + ':' + location.port + '/login';
                    $(location).attr('href', url);
                }
            }
        });
    } else
        alert("Las contraseñas no coinciden");
}

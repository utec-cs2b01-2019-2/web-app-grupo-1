function Register() {

        $('#action').append('<div class="text-center">Comprobando. . .</div>');
        console.log("Comprobando. . .");
        var email = $('#email').val();
        var password = $('#password').val();
        var confirmpassword = $('#confirmpassword').val();
        var fullname = $('#fullname').val();
  

    if (password === confirmpassword && password != 0) {

        var message = JSON.stringify({
            "fullname": fullname,
            "email": email,
            "password": password
                       
        });
        $.ajax({
            url: '/users',
            type: 'post',
            dataType: 'json',
            contentType: 'application/json',
            data: message,
            
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
        alert("Las contrase�as no coinciden");
}

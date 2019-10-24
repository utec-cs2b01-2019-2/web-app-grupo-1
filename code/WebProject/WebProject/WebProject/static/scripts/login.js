function Login() {
    console.log("Comprobando. . .");
    var email = $('#InputEmail').val();
    var password = $('#InputPassword').val();

    if (password != 0) {
        var credentials = JSON.stringify({ "email": email, "password": password });
        console.log(credentials);
        $.ajax({
            url: '/authenticate',
            type: 'post',
            dataType: 'json',
            contentType: 'application/json',
            data: credentials,
            success: function (data) {
                console.log("Authenticated!");
                var url = 'http://' + document.domain + ':' + location.port + '/home';
                $(location).attr('href', url);

            },

        });
    } else {
        alert("Escribe la contraseña");
    }

}
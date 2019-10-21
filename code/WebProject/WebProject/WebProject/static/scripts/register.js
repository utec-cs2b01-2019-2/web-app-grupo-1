function Register(){
        $('#action').append('<div class="text-center">Comprobando. . .</div>');
        var email = $('#email').val();
        var password = $('#password').val();
        var confirmedpassword = $('#confirmedpassword').val();
        var name = $('#name').val();
        var lastname = $('#lastname').val();
        var message = JSON.stringify({
                "email": email,
                "password": password,
                "name":name,
                "lastname":lastname,
                "confirmedpassword":confirmedpassword
            });
        $.ajax({
            url:'/registering',
            type:'POST',
            contentType: 'application/json',
            data : message,
            dataType:'json',
            success: function(response){
                $('#action').html("");
                if(response['status']==401){
                    $('#action').append('<div class="text-center">Datos ingresados incorrectamente</div>');}
                else{
                $('#action').append('<div class="text-center">Datos ingresados correctamente, pasa a loguearte en tu nueva cuenta</div>')
                var url = 'http://' + document.domain + ':' + location.port + '/static/login.html';
                 $(location).attr('href',url);
                }

            },
            error: function(response){
                $('#action').html("");
                if(response['status']==401){
                    $('#action').append('<div class="text-center">Datos ingresados incorrectamente</div>');}
                else{
                $('#action').append('<div class="text-center">Datos ingresados correctamente, pasa a loguearte en tu nueva cuenta</div>')
                var url = 'http://' + document.domain + ':' + location.port + '/static/login.html';
                 $(location).attr('href',url);
                }
            }
        });
}

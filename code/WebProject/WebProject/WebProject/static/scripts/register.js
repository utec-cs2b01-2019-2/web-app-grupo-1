function Register(){
        $('#action').append('<div class="text-center">Comprobando. . .</div>');
        var email = $('#Email').val();
        var password = $('#Password').val();
        var confirmedpassword = $('#confirmPassword').val();
        var name = $('#Name').val();
        var lastname = $('#Lastname').val();
        var message = JSON.stringify({
                "Email": Email,
                "Password": Password,
                "Name":Name,
                "Lastname":Lastname,
                "confirmPassword":confirmPassword
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
                var url = 'http://' + document.domain + ':' + location.port + '/login';
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

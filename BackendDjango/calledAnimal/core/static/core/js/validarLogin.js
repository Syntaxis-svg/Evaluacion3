var mail = document.getElementById('login-mail');
var pass = document.getElementById('login-pass')

var form = document.getElementById('formulario');
    form.addEventListener('submit', function(evt){
        evt.preventDefault();
        alert('Escuchando')
        var msgError = [];

        if(mail.value === null || mail.value === ''){
            msgError.push('Ingrese mail')
        }
        if(pass.value === null || pass.value ===''){
            msgError.push('Ingresa tu contraseña')
        }
        error.innerHTML = msgError.join(', ')
    })
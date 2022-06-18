var r_mail = document.getElementById('registerMail')
var r_name = document.getElementById('r-name')
var pass = document.getElementById('r-pass')
var conf_pass = document.getElementById('r-conf_pass')

var r_form = document.getElementById('r-form')
    r_form.addEventListener('submit', function(evt){
        evt.preventDefault();
        var errores = [];

        if(r_mail.value == null || r_mail.value === ''){
            errores.push('Ingrese mail')
        }
        if(r_name.value === null || r_name.value === ''){
            errores.push('Ingrese nombre correcto')
        }
        if(pass.value === null || pass.value ===''){
            errores.push('Ingrese contraseña correcta')
        }
        if(conf_pass.value === null || conf_pass.value === ''){
            errores.push('Ingrese ingrese registro contraseña')
        }
        if(pass.value != conf_pass.value){
            errores.push('Contraseñas tienen que ser iguales')
        }
        r_error.innerHTML = errores.join(', ')
    })
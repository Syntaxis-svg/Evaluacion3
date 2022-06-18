const form = document.getElementById('form');
const password = document.getElementById('password');
const Password2 = document.getElementById('password2');
form.addEventListener('submit', e => {
    e.preventDefault();
    checkInputs();
});
function checkInputs(){
    const passwordValue = password.value.trim();
    const password2Value = password2.value.trim();
    if(passwordValue === ''){
        setErrorFor(password, "no puede dejar este campo en blanco");
    }else{
        setSuccessFor(password);
    }
    if(password2Value === ''){
        setErrorFor(password2, "no puede dejar este campo en blanco");
    }else if(passwordValue !== password2Value){
        setErrorFor(password2, "contraseñas no son iguales");
    }else{
        setSuccessFor(password2);
    }
}
function setErrorFor(input, message){
    const formControl = input.parentElement;
    const small = formControl.querySelector('small');
    formControl.className = 'form-control error';
    small.innerText = message;
}

function setSuccessFor(input){
    const formControl = input.parentElement;
    formControl.className = 'form-control success';
}
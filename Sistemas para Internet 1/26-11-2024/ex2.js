function upperCase(campo){
    campo.value = campo.value.toUpperCase();
}
function validaIdade(campo){
    let idade = parseInt(campo.value);
    if(idade < 0 || idade > 120){
        alert("Idade inválida");
        campo.value = "";
    }
}
function validaSenha(campo){
    if(campo.value.length < 8){
        alert("Senha inválida");
        campo.value = "";
    }
}
var password = document.getElementById("password")
  , confirm_password = document.getElementById("confirm_password");

function validatePassword(){
  if(password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Senhas diferentes!");
  } else {
    confirm_password.setCustomValidity('');
  }
}




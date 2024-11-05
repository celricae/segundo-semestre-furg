function data(){
    var dataAtual = new Date();
    horas = dataAtual.getHours();
    minutos = dataAtual.getMinutes();
    segundos = dataAtual.getSeconds();
    if (horas >=6 && horas <= 11){
        alert("Bom dia!")
    }
    else if (horas >=12 && horas <=19){
        alert("Boa tarde!")
    }
    else{
        alert("Boa noite!")
    }
}
window.onload;data()
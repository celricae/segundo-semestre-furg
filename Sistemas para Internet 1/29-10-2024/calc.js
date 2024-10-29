function funcaosoma(){
    var x = document.getElementById("v1");
    var y = document.getElementById("v2");
    soma = parseInt(x.value) + parseInt(y.value);
    alert(soma)
}
function funcaomult(){
    var x = document.getElementById("v1");
    var y = document.getElementById("v2");
    mult = parseInt(x.value) * parseInt(y.value);
    alert(mult)
}
function funcaosub(){
    var x = document.getElementById("v1");
    var y = document.getElementById("v2");
    sub = parseInt(x.value) - parseInt(y.value);
    alert(sub)
}
function funcaodiv(){
    var x = document.getElementById("v1");
    var y = document.getElementById("v2");
    if(y.value==0)
        alert("Impossível dividir por zero.")
    else{
        div = parseInt(x.value) / parseInt(y.value);
        alert(div)
    }
}
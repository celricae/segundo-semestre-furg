function maxmin(){
    for(c=0; c<5; c++){
        var num = prompt("Digite um valor")
        if (c == 0){
            var maior = num
            var menor = num
        }
        if (num > maior){
            maior = num
        }
        if (num < maior){
            menor = num
        }
    }
    alert("O maior numero e: " + maior + " o menor numero e: " + menor)
}

function num(){
    n1 = parseFloat(document.getElementById("n1").value);
    n2 = parseFloat(document.getElementById("n2").value);
    i = n1
    while (i <= n2){
        x = "numero " + i + "</br>"
            document.write(x);
            i++;
    }
}
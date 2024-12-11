#gere as tabuadas de 0 a N em html(tabela?) e salve em arquivo.html
def tabuada (N):
    arquivo = open('tabuada.html', 'w')
    arquivo.write('<html><head><title>Tabuada de 0 a ' + str(N) + '</title></head><body>')
    arquivo.write('<table border="1">')
    for i in range(N+1):
        arquivo.write('<tr>')
        for j in range(11):
            arquivo.write('<td>' + str(i) + ' x ' + str(j) + ' = ' + str(i*j) + '</td>')
        arquivo.write('</tr>')
    arquivo.write('</table></body></html>')
    arquivo.close()
    return
tabuada(10)
'''
N = int(input('Digite um número: '))
saida = "O Incrivel sistemas de Tabuadas <hr>"

for um_n in range(N+1):
    saida += "<table border='1'>"
    for i in range(11):
        mult = um_n * i
        saida += f"<tr><td>{um_n} x {i} = {mult}</td></tr>"
    saida += "</table><br>"
with open('tabuada.html', 'w') as arq:
    arq.write(saida)
'''
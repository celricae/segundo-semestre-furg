#arq = ponteiro para o arquivo 
#poema.txt = nome do arquivo 
#r= Read 
#w= Write 
#a=Append
arq = open('poema.txt','r')

print(arq)

texto=arq.read()

print(texto)
print('--------------')
lista = arq.readlines()
print(lista)

#fecha o arquivo
arq.close()



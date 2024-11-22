#Leia o arquivo alunos.csv e escreva.
arq = open('alunos.csv','r')
texto = arq.read()

print(texto)
arq.close()
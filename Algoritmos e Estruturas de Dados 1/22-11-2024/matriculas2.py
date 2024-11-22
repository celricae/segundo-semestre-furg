#Leia o arquivo alunos.csv e liste apenas os nomes dos alunos.
arq = open('alunos.csv','r')

lista = arq.readlines()
def mostra_nomes(lista)
    for linha in lista:
        colunas = linha.split(';')
        print(colunas[1])

arq.close()
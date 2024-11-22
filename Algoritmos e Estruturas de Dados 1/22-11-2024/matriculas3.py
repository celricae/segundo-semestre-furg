#Leia o arquivo alunos.csv e mostre quem é o aluno mais novo.
arq = open('alunos.csv','r')

lista = arq.readlines()
def mostra_nomes(lista):
    for linha in lista:
        colunas = linha.split(';')
        print(colunas[1])
def mais_novo(lista):
    novo = '10251231'
    nome_do_novo = ''
    dt_original = ''
    for linha in lista[1:]:
        colunas = linha.split(';')
        data = colunas[2][:-1]
        lista_data = data.split('/')
        data_padrao = lista_data[2] + lista_data [1] + lista_data[0]
        if data_padrao > novo:
            novo = data_padrao
            nome_do_novo = colunas[1]
            dt_original = data
    print(nome_do_novo,novo)

tudo = arq.readlines()
mostra_nomes(tudo)
mais_novo(tudo)


#escreva um programa que receba duas listas do usuário e retorne uma nova lista contendo apenas os elementos comuns entre as duas listas
lista1 = []
lista2 = []
lista3 = []
pala1 = ' '
pala2 = ' '

while pala1 != '':
    pala1 = input("Digite uma palavra (ou não digite nada para encerrar): ")
    lista1.append(pala1)
while pala2 != '':
    pala2 = input("Digite mais palavras (ou não digite nada para encerrar): ")
    lista2.append(pala2)
print(set(lista1) & set(lista2))
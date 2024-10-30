#Dada uma lista de números inteiros informada pelo usuário, escreva um programa em python que conte quantos números único (diferentes) estão presentes na lista. A digitação dos elementos da lista deve encerrar quando for digitado o número zero.
lista1 = []
lista2 = []
num1 = " "
num2 = " "
while num1 != 0:
    num1 = int(input("Digite um número (ou digite zero para finalizar): "))
    lista1.append(num1)
while num2 != 0:
    num2 = int(input("Digite mais números (ou digite zero para finalizar): "))
    lista2.append(num2)
diferenca = list(set(lista1) - set(lista2))
print(diferenca)
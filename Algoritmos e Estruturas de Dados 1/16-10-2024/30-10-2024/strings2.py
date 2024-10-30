#escreva um programa que receba uma lista de números e retorne uma lista contendo apenas os números pares.
nume = []
pares = []

num = ' '

while num != 0:
	num = int(input("Digite um número (ou digite zero para finalizar): "))
	if num%2 == 0:
		pares.append(num)
print(pares)
#escreva um programa que leia uma lista de palaras do usuário e retorne outra lista contendo apenas as palavras com mais de 5 caracteres.

palavras = []
maisde5 = []

pala = ' '

while pala != '':
	pala = input("Digite uma palavra (ou não digite nada para finalizar o programa): ")
	if len(pala) > 5:
		maisde5.append(pala)
print(maisde5)
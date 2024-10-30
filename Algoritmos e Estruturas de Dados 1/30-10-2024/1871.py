'''
mandar para o beecrowd
'''
def tirazero(num):
    num = str(num)
    saida = ''
    for algarismo in num:
        if algarismo != '0':
            saida += algarismo
    return(saida)

def somatirazero():
    while True:   
        nume = input("")
        nume = nume.split(' ')
        num1 = int(nume[0])
        num2 = int(nume[1])
        soma = num1 + num2
        if soma == 0:
            return False
        print(tirazero(soma))
somatirazero()




    
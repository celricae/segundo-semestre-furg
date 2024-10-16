def dobro(num):
    saida = num*2
    return(saida)

num = int(input("Digite o número: "))
duplo = dobro(num)
print(f"O número + 1 é: {duplo + 1}")

def par(valor):
    if valor % 2 == 0:
        return True
    return False

if par(num):
    print("PAR!")
else:
    print("IMPAR!")
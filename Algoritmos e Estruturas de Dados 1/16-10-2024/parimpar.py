def par(valor):
    if valor % 2 == 0:
        return True
    return False

num = int(input("Digite o número: "))

if par(num):
    print("PAR!")
else:
    print("IMPAR!")
    
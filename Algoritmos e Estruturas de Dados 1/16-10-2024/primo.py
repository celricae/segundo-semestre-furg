num = int(input("Digite um número: "))
def primo(num):
    if num == 1:
        return False
    cont = 2
    div = 0
    while cont < num:
        if num % cont == 0:
            div += 1
        cont += 1
    if div == 0: 
        return True
    return False

if primo(num):
    print(f"{num} é primo")
else:
    print(f"{num} não é primo")
'''
for i in range(101):
    if primo(i):
        print(f"{i} é primo")
    else:
        print(f"{i} não é primo")
'''
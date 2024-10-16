'''
num = 7

for i in range (11):
    mult = num * i
    print(f"{num} X {i} = {mult}")
'''

def tabuada(num):
    saida = ''
    for i in range (11):  
        mult = num * i
        saida = saida + f"{num} X {i} = {mult}\n"
    return (saida)
#print(tabuada(8))

for i in range(11):
    print(f"---Tabuada do {i}---")
    print(tabuada(i))
    print("---------------------")

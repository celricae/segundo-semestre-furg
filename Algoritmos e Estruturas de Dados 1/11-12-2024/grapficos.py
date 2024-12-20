import graphics as gf
import random as rd
rd.seed()

def foi_no_botao(botao, onde_cliquei):
    bt_x = botao.getP1().getX()
    bt_y = botao.getP1().getY()
    bt2_x = botao.getP2().getX()
    bt2_y = botao.getP2().getY()
    print(f'----> {bt_x} {bt_y} {bt2_x} {bt2_y}')
    if onde_cliquei.getX() > bt_x and onde_cliquei.getX() < bt2_x and onde_cliquei.getY() > bt_y and onde_cliquei.getY() < bt2_y:
        return True
    return False

def cria_botao(x1,y1,x2,y2):
    novo_botao = gf.Rectangle(gf.Point(x1,y1), gf.Point(x2,y2))
    novo_botao.setFill("yellow")
    novo_botao.draw(win)
    lista_botoes.append(novo_botao)
    return novo_botao

def aciona_botao(onde_cliquei)
    for um_botao in lista_botoes:
        if foi_no_botao(um_botao,onde_cliquei):
            um_botao.setFill("red")
        else:
            um_botao.setFill("yellow")

lista_botoes = []
win = gf.GraphWin("Minha Janela", 400, 350) # Cria uma janela

botao = cria_botao(10,60,190,100)
botao = cria_botao(100,160,290,200)
botao = cria_botao(140,200,400,500)

print(lista_botoes)

while True:
    onde_cliquei = win.getMouse()
    aciona_botao(onde_cliquei)






'''
win = gf.GraphWin("Minha Janela", 400, 350)

c = gf.Circle(gf.Point(100,150), 10)
cores = ['red', 'blue', 'green', 'yellow', 'black', 'white', 'purple', 'orange', 'pink', 'brown']
c.setFill("red")
c.draw(win)
cont = 0

while True:
    onde_cliquei = win.getMouse()
    print(onde_cliquei.getX(), onde_cliquei.getY())
    nova_bolinha = gf.Circle(onde_cliquei, 10)
    nova_bolinha.setFill(cores[cont])
    cont += 1
    if cont == len(cores):
        cont = 0
    nova_bolinha.draw(win)
'''
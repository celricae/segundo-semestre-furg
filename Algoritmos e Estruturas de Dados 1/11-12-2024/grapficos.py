import graphics as gf






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

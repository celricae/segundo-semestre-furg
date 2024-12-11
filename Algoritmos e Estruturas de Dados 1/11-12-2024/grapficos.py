import graphics as gf






win = gf.GraphWin("Minha Janela", 400, 350)

c = gf.Circle(gf.Point(100,150), 10)
c.setFill("red")
c.draw(win)
onde_cliquei = win.getMouse()
print(onde_cliquei.getX(), onde_cliquei.getY())
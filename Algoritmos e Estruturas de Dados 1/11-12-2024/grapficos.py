import graphics as gf






win = gf.GraphWin("Minha Janela", 400, 350)

c = gf.Circle(gf.point(100,150), 10)
c.setFill("red")
c.draw(win)
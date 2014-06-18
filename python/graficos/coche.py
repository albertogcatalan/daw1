from graphics import *

# parte 1
interfaz = GraphWin('Coche', 800, 400)
rectangulo = Rectangle(Point(150, 250), Point(300, 275))
rectangulo.setFill('red')
rectangulo.draw(interfaz)

# parte superior
superior = Rectangle(Point(180, 250), Point(270, 230))
superior.setFill('grey')
superior.draw(interfaz)

# rueda 1
rueda1 = Circle(Point(180, 275), 11)
rueda1.setFill('black')
rueda1.draw(interfaz)

# rueda 2
rueda2 = Circle(Point(280, 275), 11)
rueda2.setFill('black')
rueda2.draw(interfaz)

# movimiento
limite = 1
while limite == 1:

    time.sleep(0.081)
    rectangulo.move(15, 0)
    superior.move(15, 0)
    rueda1.move(15, 0)
    rueda2.move(15, 0)


interfaz.getMouse()

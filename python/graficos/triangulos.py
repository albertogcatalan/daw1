from graphics import *
import random

g = GraphWin('Ejemplo Graphics', '640', '480')
colores = ['red', 'yellow', 'green', 'blue', 'purple']
random.shuffle(colores)
puntos = []

while True:
    for x in range(3):
        p = g.getMouse()
        p.draw(g)
        puntos.append(p)

    pol = Polygon(puntos)
    pol.draw(g)
    posicion = random.randint(0, 4)
    pol.setFill(colores[posicion])
    puntos = []

g.getMouse()

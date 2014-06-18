from graphics import *
import random

g = GraphWin('Ejemplo Graphics', '640', '480')
colores = ['red', 'yellow', 'green', 'blue', 'black']
random.shuffle(colores)

#for x in range(10):
while True:
    p = g.getMouse()
    tam = random.randint(10, 50)
    c = Circle(p, tam)
    c.draw(g)
    posicion = random.randint(0, 4)
    #c.setFill(colores.pop())
    c.setFill(colores[posicion])


g.getMouse()

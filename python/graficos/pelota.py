from graphics import *
import random
import time

g = GraphWin('Ejemplo Graphics', '640', '480')
colores = ['red', 'yellow', 'green', 'blue', 'purple']
random.shuffle(colores)
h = 1
v = 1

tam = random.randint(10, 50)
c = Circle(Point(100, 100), tam)
c.draw(g)
posicion = random.randint(0, 4)
c.setFill(colores[posicion])

while True:
    '''p = g.checkMouse()
    if p != 'None':
        c = Circle(p, tam)
        c.draw(g)
        c.setFill(colores[posicion])'''

    c.move(10 * h, 10 * v)
    if c.p1.x <= 0 or c.p2.x >= 640:
        h *= -1
    if c.p1.y <= 0 or c.p2.y >= 480:
        v *= -1

    time.sleep(0.02)


g.getMouse()

from graphics import *
import random

g = GraphWin('Ejemplo Graphics', '640', '480')
c = Circle(Point(100, 100), 100)
c.draw(g)
for r in range(255):
    for v in range(255):
        for a in range(255):
            c.setFill(color_rgb(r, v, a))

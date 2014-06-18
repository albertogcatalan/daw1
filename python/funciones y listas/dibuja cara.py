# -*- coding: cp1252 -*-
from graphics import *

g = GraphWin ('Cara', 300, 300)

def dibuja_cara(centro, tam, ventana, color, color2):
    c = Circle(centro, tam)
    c.setFill(color)
    c.draw(ventana)

    c1 = Circle(Point(165, 140), 5)
    c1.setFill(color2)
    c1.draw(ventana)

    c2 = Circle(Point(135, 140), 5)
    c2.setFill(color2)
    c2.draw(ventana)

    l1 = Rectangle(Point(137, 170), Point(165, 175))
    l1.setFill(color2)
    l1.draw(ventana)
    
centro = Point(150, 150)
ventana = g
tam = 40
color = 'Red'
color2 = 'Blue'
dibuja_cara(centro, tam, ventana, color, color2)

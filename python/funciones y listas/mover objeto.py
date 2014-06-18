# -*- coding: cp1252 -*-
from graphics import *

g = GraphWin ('Cara', 300, 300)

centro = Point(150, 150)
ventana = g
tam = 40
color = 'Red'

c = Circle(centro, tam)
c.setFill(color)
c.draw(ventana)

def mover_a(forma, nuevo_centro):
    g.move(nuevo_centro)
    
    
    
    

forma = g
nuevo_centro = Point(140, 200)
g.getMouse()
mover_a(forma, nuevo_centro)

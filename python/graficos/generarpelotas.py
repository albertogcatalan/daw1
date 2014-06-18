# -*- coding: cp1252 -*-
from graphics import *
from random import randint
import random
import time

g = GraphWin('Bolas locas', 640, 480)
colores = ['red', 'yellow', 'green', 'blue', 'purple', 'seagreen', 'chocolate']
random.shuffle(colores)

def crea_pelota(pantalla): #función para crear pelotas
    r = randint(10, 50)
    x = randint(r, pantalla.width - r)
    y = randint(r, pantalla.height - r)
    c = Circle(Point(x, y), r)
    c.setFill(colores[randint(0, 4)])
    c.dx = 20
    c.dy = 20
    c.draw(pantalla)
    return c

def mueve_pelota(pelota, pantalla): #función para mover pelotas
    pelota.move(pelota.dx, pelota.dy)
    centro = pelota.getCenter()
    
    if pelota.dx > 0:
        if pelota.radius + centro.x > pantalla.width:
            pelota.dx *= -1
    elif centro.x - pelota.radius < 0:
        p.dx *= -1

    if pelota.dy > 0:
        if pelota.radius + centro.y > pantalla.height:
            pelota.dy *= -1
    elif centro.y - pelota.radius < 0:
        p.dy *= -1

def tocada(pelota, mouse):
    radio = pelota.getRadius()
    centro = pelota.getCenter()

    x = centro.x
    y = centro.y
    
    if mouse.x in int(x + radio) and mouse.y in int(y - radio):
        return True
    else:
        return False
    

antes = time.time()  
pel = []

'''for x in range(15):
    pel.append(crea_pelota(g))'''

while True:

    
    ahora = time.time()
    if ahora - antes > 2:
        pel.append(crea_pelota(g))
        antes = ahora
        
    for p in pel: 
       mueve_pelota(p, g)
       if tocada(p, g.getMouse()) == True:
           p.undraw()

       time.sleep(0.01)


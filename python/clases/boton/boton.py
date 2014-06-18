# -*- coding: utf-8 -*-
'''
Created on 09/12/2011

@author: Alberto
'''

from graphics import GraphWin, Rectangle, Point, Text

class Rectangulo_centro(object):#clase para crear rectangulos centrados
    def __init__(self, ventana):
        ancho = ventana.width / 2
        alto = ventana.height / 2
        p1 = Point(ancho - 20, alto - 10)
        p2 = Point(ancho + 20, alto + 10)
        self.r = Rectangle(p1, p2)
        self.r.draw(ventana)
    def color(self, c):
        self.r.setFill(c)
        
class Boton(object):
    def __init__(self, v, centro, ancho, alto, etiqueta):
        #calculo de la posicion
        x, y = centro.getX(), centro.getY()
        w, h = ancho /2, alto /2
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        #creacion del boton y etiqueta
        self.boton = Rectangle(p1, p2)
        self.boton.draw(v)
        self.boton.setFill('#CCC')
        self.etiqueta = Text(centro, etiqueta)
        self.etiqueta.setTextColor('#666')
        self.etiqueta.draw(v)
        self.desactivar()
    def color(self, c):
        self.boton.setFill(c)
    def pulsado(self, p):
        if p.getX() in range(self.xmin, self.xmax) and p.getY() in range(self.ymin, self.ymax):
            return True
        else:
            return False
    def activar(self):
        self.etiqueta.setTextColor('#000')
        self.estado = True
        
    def desactivar(self):
        self.etiqueta.setTextColor('#666')
        self.estado = False
        
        
        
    
w = GraphWin('Mi boton', 600, 400)
b1 = Boton(w, Point(300, 200), 80, 40, 'Okey')
b2 = Boton(w, Point(300, 250), 80, 40, 'Activar')

while True:
    p = w.getMouse()
    if b1.pulsado(p):
        b1.color('blue')
    if b2.pulsado(p):
        if b2.estado:
            b2.desactivar()
        else:
            b2.activar()
        
w.getMouse()
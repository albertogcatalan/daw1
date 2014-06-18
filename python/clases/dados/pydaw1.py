'''
Created on 15/12/2011

@author: Alberto
'''
from graphics import Rectangle, Point, Text
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
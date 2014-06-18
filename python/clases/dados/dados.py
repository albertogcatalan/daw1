# -*- coding: utf-8 -*-
'''
Created on 09/12/2011

@author: Alberto
'''

from graphics import GraphWin, Rectangle, Point, Circle, Text
from random import choice
from pydaw1 import Boton #importamos nuestra libreria con boton


class Dado(object):
    def __init__(self, v, centro, ancho, alto):
        x, y = centro.getX(), centro.getY()
        w, h = ancho /2, alto /2
        self.ventana = v
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.dado = Rectangle(p1, p2)
        self.dado.draw(v)
        self.dado.setFill('#FF0000')
        '''pintamos los circulos del dado con las posiciones reescalables de los puntos
    
            pos1            pos5
            pos2    pos4    pos6
            pos3            pos7
            
        '''
        self.pos1 = Point(self.xmin + w /2, self.ymin + h /2)
        self.pos2 = Point(self.xmin + w / 2, self.ymin + h)
        self.pos3 = Point(self.xmin + w / 2, self.ymin + h * 1.5)
        self.pos4 = Point(self.xmin + w, self.ymin + h)
        self.pos5 = Point(self.xmin + w * 1.5, self.ymin + h /2)
        self.pos6 = Point(self.xmin + w * 1.5, self.ymin + h)
        self.pos7 = Point(self.xmin + w * 1.5, self.ymin + h * 1.5)
        
        self.c1 = Circle(self.pos1, 4)
        self.c1.setOutline('#fff')
        self.c1.setFill('#fff')
        self.c1.draw(self.ventana)
            
        self.c2 = Circle(self.pos2, 4)
        self.c2.setOutline('#fff')
        self.c2.setFill('#fff')
        self.c2.draw(self.ventana)
            
        self.c3 = Circle(self.pos3, 4)
        self.c3.setOutline('#fff')
        self.c3.setFill('#fff')
        self.c3.draw(self.ventana) 
            
        self.c4 = Circle(self.pos4, 4)
        self.c4.setOutline('#fff')
        self.c4.setFill('#fff')
        self.c4.draw(self.ventana)
            
        self.c5 = Circle(self.pos5, 4)
        self.c5.setOutline('#fff')
        self.c5.setFill('#fff')
        self.c5.draw(self.ventana)
            
        self.c6 = Circle(self.pos6, 4)
        self.c6.setOutline('#fff')
        self.c6.setFill('#fff')
        self.c6.draw(self.ventana)
            
        self.c7 = Circle(self.pos7, 4)
        self.c7.setOutline('#fff')
        self.c7.setFill('#fff')
        self.c7.draw(self.ventana)
        
        self.limpiar()
        
    def colorDado(self, c):#personalizar el dado
        self.dado.setFill(c)
        
    def colorPunto(self, c):#personalizar los puntos del dado
        self.c1.setOutline(c)
        self.c1.setFill(c)
        self.c2.setOutline(c)
        self.c2.setFill(c)
        self.c3.setOutline(c)
        self.c3.setFill(c)
        self.c4.setOutline(c)
        self.c4.setFill(c)
        self.c5.setOutline(c)
        self.c5.setFill(c)
        self.c6.setOutline(c)
        self.c6.setFill(c)
        self.c7.setOutline(c)
        self.c7.setFill(c)
        
    def pulsado(self, p):#funcion para saber si se ha pulsado
        if p.getX() in range(self.xmin, self.xmax) and p.getY() in range(self.ymin, self.ymax):
            return True
        else:
            return False
        
    def ponValor(self, valor=1):#funcion para establecer la cara visible del dado
        self.limpiar()
        if valor == 1:
            self.c4.draw(self.ventana)
        elif valor == 2:
            self.c1.draw(self.ventana)
            self.c7.draw(self.ventana)
        elif valor == 3:
            self.c1.draw(self.ventana)
            self.c4.draw(self.ventana)
            self.c7.draw(self.ventana)
        elif valor == 4:
            self.c1.draw(self.ventana)
            self.c3.draw(self.ventana)
            self.c5.draw(self.ventana)
            self.c7.draw(self.ventana)
        elif valor == 5:
            self.c1.draw(self.ventana)
            self.c3.draw(self.ventana)
            self.c4.draw(self.ventana)
            self.c5.draw(self.ventana)
            self.c7.draw(self.ventana)
        elif valor == 6:
            self.c1.draw(self.ventana)
            self.c2.draw(self.ventana)
            self.c3.draw(self.ventana) 
            self.c5.draw(self.ventana)
            self.c6.draw(self.ventana)
            self.c7.draw(self.ventana)
            
    def limpiar(self):#limpiar el dado antes de pintar
        self.c1.undraw()
        self.c2.undraw()
        self.c3.undraw()
        self.c4.undraw()
        self.c5.undraw()
        self.c6.undraw()
        self.c7.undraw()
        
    def tirarDado(self):#funcion para visualizar aleatoriamente una cara
        posibles = [1, 2, 3, 4, 5, 6]
        num = choice(posibles)
        self.ponValor(num)
        return num
        
#creamos la ventana con 3 dados y 1 boton
w = GraphWin('Dados aleatorios', 600, 400)

etiqueta = Text(Point(300, 70), 'Puntos: 0')
etiqueta.draw(w)
        
d1 = Dado(w, Point(130, 150), 100, 100)
d1.colorDado('blue')
d1.colorPunto('red')
d1.ponValor()

d2 = Dado(w, Point(300, 150), 100, 100)
d2.ponValor()

d3 = Dado(w, Point(470, 150), 100, 100)
d3.colorDado('green')
d3.colorPunto('blue')
d3.ponValor()

b1 = Boton(w, Point(230, 270), 100, 40, 'Lanzar dados')
b1.activar()

b2 = Boton(w, Point(370, 270), 100, 40, 'Salir')
b2.activar()

while True:
    p = w.getMouse()
    
    if b1.pulsado(p):
        if b1.estado:
            num1 = d1.tirarDado()
            num2 = d2.tirarDado()
            num3 = d3.tirarDado()
            numtotal = num1 + num2 + num3
            etiqueta.undraw()
            etiqueta = Text(Point(300, 70), 'Puntos: %d' % numtotal)
            etiqueta.draw(w)
            
            
    if b2.pulsado(p):
        if b2.estado:
            exit()

        
w.getMouse()
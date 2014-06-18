# -*- coding: utf-8 -*-
from graphics import *
import string

g = GraphWin ('Agenda', 640, 640) #iniciamos la ventana
g.setCoords (0, 0, 3, 3) #establecemos nuevas coordenadas para la ventana

texto('Tres en Raya', 1.5, 2.5, 36, 'seagreen')
l = Line (Point(0.5, 2.1), Point(2.5, 2.1))
l.draw(g)
l.setFill('seagreen')

texto('Build 0.1.12.3 Master Pro', 1.5, 2.2, 28, 'seagreen')
texto('P1 vs P2', 0.5, 1.5, 25, 'chocolate')
texto('P1 vs CPU', 2.5, 1.5, 25, 'chocolate')
texto('CPU vs CPU', 1.5, 1.1, 25, 'chocolate')
texto('Salir', 1.5, 0.1, 25, 'chocolate')

lista_amigos = []

def checklista(a):
    if a == '':
        for n, letra in enumerate(lista_amigos):
            print letra,
            if (n+1) % 3 == 0:
                print
        
    else:
        if a not in lista_amigos:
            lista_amigos.append(a)
        else:
            print 'Ya estas dado de alta'
            
            


while True:
    
    amigo = raw_input('Introduce nombre y apellidos: ')
    checklista(amigo)
    
    amigo = raw_input('Introduce email: ')
    checklista(amigo)
    
    amigo = raw_input('Introduce teléfono: ')
    checklista(amigo)





    
    
    

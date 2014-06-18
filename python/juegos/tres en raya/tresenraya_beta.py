# -*- coding: cp1252 -*-
from graphics import *
import random

cpu = 0
cpu_pos = [0, 1, 2]
jugar = 0
ganar = 0
tablas = 0
posiciones =  ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] #posiciones
pGanadora = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 5, 9],
    [2, 5, 8],
    [3, 5, 7],
    [1, 4, 7],
    [3, 6, 9]
    
] #array bidimensional de las posiciones ganadoras

def tablero(g): #función para cargar el tablero

    r1 = Rectangle(Point(0, 0), Point(3,3))
    r1.draw(g)
    r1.setFill('GhostWhite')
    
    p1 = Point (1,3)
    p2 = Point (1,0)
    p3 = Point (2,3)
    p4 = Point (2,0)
    p5 = Point (0,2)
    p6 = Point (3,2)
    p7 = Point (0,1)
    p8 = Point (3,1)

    l1 = Line (p1,p2)
    l1.draw(g)
    l1.setFill('black')
    l2 = Line (p3,p4)
    l2.draw(g)
    l2.setFill('black')
    l3 = Line (p5,p6)
    l3.draw(g)
    l3.setFill('black')
    l4 = Line (p7,p8)
    l4.draw(g)
    l4.setFill('black')
    
def coord(x, y): #función para conseguir la posición
    
    pos = 0
    if x == 0 and y == 0:
        pos = 1
    elif x == 1 and y == 0:
        pos = 2
    elif x == 2 and y == 0:
        pos = 3
    elif x == 0 and y == 1:
        pos = 4
    elif x == 1 and y == 1:
        pos = 5
    elif x == 2 and y == 1:
        pos = 6
    elif x == 0 and y == 2:
        pos = 7
    elif x == 1 and y == 2:
        pos = 8
    elif x == 2 and y == 2:
        pos = 9
        
    return pos

def texto(texto, x, y, tam, color):#función para crear texto con formato
    t = Text(Point(x, y), texto)
    t.setTextColor(color)
    t.setSize(tam)       
    t.setStyle('bold')
    t.draw(g)
    

##########INICIO DEL JUEGO#################

g = GraphWin ('Tres en Raya', 640, 640) #iniciamos la ventana
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

    
while True:
    click = g.getMouse()
    xg = int(click.x)
    yg = int(click.y)

    if xg == 0 and yg == 1:#p1 vs p2
        tablero(g)
        jugar = 1
    elif xg == 2 and yg == 1:#p1 vs cpu
        tablero(g)
        jugar = 1
        cpu = 1
    elif xg == 1 and yg == 1:#cpu vs cpu
        tablero(g)
        jugar = 1
        cpu = 2
    elif xg == 1 and yg == 0:#salimos del juego
        g.close()
        
    ##########P1 VS P2#################
    while jugar == 1:
        if tablas == 0: #comprobar si están en tablas
            for n in range (1, 11): #bucle de acciones
                for p in range(0, 8): #comprobar quién gana
                    if 'O' in posiciones[pGanadora[p][0]] and 'O' in posiciones[pGanadora[p][1]] and 'O' in posiciones[pGanadora[p][2]]:
                        
                        r2 = Rectangle(Point(0.3, 1.3), Point(2.7, 1.7))
                        r2.draw(g)
                        r2.setFill('chocolate')
                        texto('Ha ganado el Jugador 1', 1.5, 1.5, 30, 'seagreen')
                        
                        ganar = 1
                   
                    elif 'X' in posiciones[pGanadora[p][0]] and 'X' in posiciones[pGanadora[p][1]] and 'X' in posiciones[pGanadora[p][2]]:
                        
                        r2 = Rectangle(Point(0.3, 1.3), Point(2.7, 1.7))
                        r2.draw(g)
                        r2.setFill('chocolate')
                        texto('Ha ganado el Jugador 2', 1.5, 1.5, 30, 'seagreen')
                        
                        ganar = 1

                
                if n == 10 and ganar == 0:
                    tablas = 1
                    ganar = 2
                    
                    
                if ganar == 0: #si no gana
                    
                    if cpu == 1:
                        if n%2:
                            p = g.getMouse()
                            x = int(p.x)
                            y = int(p.y)
                        else:
                            x = random.choice(cpu_pos)
                            y = random.choice(cpu_pos)
                            print n
                    elif cpu == 2:
                        x = random.choice(cpu_pos)
                        y = random.choice(cpu_pos)
                    elif cpu == 0:
                        p = g.getMouse()
                        x = int(p.x)
                        y = int(p.y)


                    cuadro = coord(x, y)
                    c = Circle(Point(x + 0.5, y + 0.5), 0.3)
                    c.draw(g)
                    
                    if posiciones[cuadro] == 'X' or posiciones[cuadro] == 'O': #si está ocupada la posición
                        print 'Posición ocupada'
                        if cpu == 1:
                            if n%2:
                                print 'Jugador 1 espera'
                            else:
                                x = random.choice(cpu_pos)
                                y = random.choice(cpu_pos)
                                
                        elif cpu == 2:
                            x = random.choice(cpu_pos)
                            y = random.choice(cpu_pos)

                        cuadro = coord(x, y)
                        c = Circle(Point(x + 0.5, y + 0.5), 0.3)
                        c.draw(g)
                        c.setFill('red')
                        
                        posiciones.insert(cuadro, 'X')
                        posiciones.pop(cuadro+1)
                        
                    else:
                        if n%2:
                            #si es jugador 1 insertamos posicion
                            c.setFill('blue')
                            posiciones.insert(cuadro, 'O')
                            posiciones.pop(cuadro+1)
                        
                        else:
                            #si es jugador 2 insertamos posicion
                            c.setFill('red')
                            posiciones.insert(cuadro, 'X')
                            posiciones.pop(cuadro+1)
                            
        else:
            if ganar == 2 and tablas == 1: #si queda en tablas
                
                r2 = Rectangle(Point(0.3, 1.3), Point(2.7, 1.7))
                r2.draw(g)
                r2.setFill('chocolate')
                        
                texto('Has quedado en tablas', 1.5, 1.5, 30, 'seagreen')
                break
            else:
                break
    
    
g.getMouse()

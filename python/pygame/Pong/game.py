# -*- coding: utf-8 -*-

'''
Created on 11/01/2012

@author: Alberto
'''
import pygame
import sys
from pygame.locals import *
from gamelib import *

pygame.init()

# objetos
pelota = Pelota()
j1 = Raqueta(50)
j2 = Raqueta(740)
reloj = pygame.time.Clock()
marcador = Marcador()
escenario = Escenario()

# pantalla
visor = pygame.display.set_mode((800,600), FULLSCREEN)

# cargar pantalla inicial
escenario.draw(visor)

while True:
    # fps
    reloj.tick(60)
    
    # eventos
    for evento in pygame.event.get():
        if evento.type == KEYDOWN:
            if evento.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
    # updates
    pelota.update()
    j1.update_left(pelota)
    j2.update_right(pelota)
    
    if j1.puntos == 11 or j2.puntos == 11:
        escenario.update(visor, j1.puntos, j2.puntos)
        j1.puntos = 0
        j2.puntos = 0
        escenario.draw(visor)
        
    # draw
    visor.fill((0,0,0))
    pelota.draw(visor)
    j1.draw(visor)
    j2.draw(visor)
    marcador.draw(visor, j1.puntos, j2.puntos)
    
    pygame.display.update()
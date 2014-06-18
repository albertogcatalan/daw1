# -*- coding: utf-8 -*-

'''
Created on 16/12/2011

@author: Alberto
'''

import pygame
from pygame.locals import *
from personajes import Pingu, Bomba
import time
import random
import sys
import os

pygame.init()

ANCHO, ALTO = 640, 480
COLOR_FONDO = [255, 0, 0]

FPS_clock = pygame.time.Clock()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego en pygame")

FPS = 0

#cargar recursos
ruta_fondo = os.path.join('img', 'volley.png')
fondo = pygame.image.load(ruta_fondo)

bomba = Bomba()
pingu = Pingu(10)

font = pygame.font.SysFont('raavi', 32)
#font = pygame.font.Font(os.path.join('font', 'ARIAL.TTF'), 32)

jugando = True
lista_bombas = []
i = 1
while jugando:
    FPS = FPS_clock.tick(30)
    
    #eventos
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            jugando = False
        
    #mover, comprobar
    if random.randint(1, 30) == 1:
        lista_bombas.append(Bomba())
        
        
    bomba.mover()
    pingu.mover()
    pingu.update()
    
    for bomba in lista_bombas:
        if pingu.choca(bomba):
            lista_bombas.remove()
        else:
            bomba.update()
            
    #pintar
    pantalla.blit(fondo, (0, 0))
    
    mensaje_fps = font.render("FPS: %d" % FPS, False, (0, 0, 0))
    pantalla.blit(mensaje_fps, (10, 10))
    mensaje_marcador = font.render("Vidas: %d" % pingu.vidas, False, (0, 0, 0))
    pantalla.blit(mensaje_marcador, (10, 40))
    mensaje_bomba = font.render("Bombas: %d" % (bomba.explosion), False, (0, 0, 0))
    
    pantalla.blit(mensaje_bomba, (10, 70))
    pantalla.blit(pingu.imagen, pingu.rect)
    for bomba in lista_bombas:
        pantalla.blit(bomba.imagen, bomba.rect)
    
    pygame.display.flip()
    

sys.exit()
    
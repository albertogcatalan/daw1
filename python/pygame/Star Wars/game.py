# -*- coding: utf-8 -*-
'''
Clon de Space Invaders
(Basado en un script original de Kevin Harris)

A partir de un ejercicio de Fernando Salamero
'''

import pygame
from pygame.locals import *
from starwarslib import *

random.seed()

pygame.init()

visor = pygame.display.set_mode( (ANCHO, ALTO) )
pygame.display.set_caption( "Star Wars" )
pygame.mouse.set_visible(False)

fondo_imagen = cargar_imagen( "background.bmp" )
visor.blit(fondo_imagen, (0,0))


xwing = XWing()
# grupo de Xwing para colisiones
xwingGrupo = pygame.sprite.RenderUpdates(xwing)
# grupod de naves enemigas
tiefighterGrupo = pygame.sprite.RenderUpdates()
# inicialización: tres naves
tiefighterGrupo.add( TIEFighter( 150 ) )
tiefighterGrupo.add( TIEFighter( 400 ) )
tiefighterGrupo.add( TIEFighter( 650 ) )
    
jugando = True
intervaloEnemigos = 0
reloj = pygame.time.Clock()

while jugando:
    reloj.tick( 60 )  # FPS
    
    for event in pygame.event.get():
        if event.type == QUIT:
            jugando = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                jugando = False
            if event.key == K_SPACE:
                xwing.dispara()
        elif event.type == KEYUP:
            xwing.dx , xwing.dy = 0 , 0
    
    teclasPulsadas = pygame.key.get_pressed()
    # Movimiento nave
    if teclasPulsadas[K_LEFT]:
        xwing.dx = -4
    if teclasPulsadas[K_RIGHT]:
        xwing.dx = 4
    if teclasPulsadas[K_UP]:
        xwing.dy = -4
    if teclasPulsadas[K_DOWN]:
        xwing.dy = 4

    intervaloEnemigos += 1
    if intervaloEnemigos >= 200:
        tiefighterGrupo.add( TIEFighter( 320 ) )
        intervaloEnemigos = 0
    
    # Actualiza
    xwingGrupo.update()
    XWing.laser_grupo.update()
    tiefighterGrupo.update()
    TIEFighter.laser_grupo.update()
    
    # Elimina enemigos tocados
    for pum in pygame.sprite.groupcollide(tiefighterGrupo, XWing.laser_grupo, 1, 1):
        pum.explota()
        xwing.puntos += 3
        
        
    if pygame.sprite.groupcollide(xwingGrupo, TIEFighter.laser_grupo, 0, 0):
        xwing.vidas -= 1
        xwing.explotando = 29
        if xwing.vidas == 0:
            print "FUCK"
            
                
            
        

    # Borra
    TIEFighter.laser_grupo.clear( visor, fondo_imagen )
    tiefighterGrupo.clear( visor, fondo_imagen )
    XWing.laser_grupo.clear( visor, fondo_imagen)
    xwingGrupo.clear( visor, fondo_imagen )
    
    # Dibuja
    TIEFighter.laser_grupo.draw( visor )
    XWing.laser_grupo.draw( visor )
    tiefighterGrupo.draw( visor )
    xwingGrupo.draw( visor )
    
    # Actualiza
    pygame.display.update()
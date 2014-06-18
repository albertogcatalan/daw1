# -*- coding: utf-8 -*-

'''
Created on 13/01/2012

@author: Alberto
'''
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------
# mario07.py
# Movimiento de plataforma
#-------------------------------------------------------------------
import sys
import pygame
from pygame.locals import *

# Clase MiSprite
class MiSprite( pygame.sprite.Sprite ):
    # Inicializador de la clase
    def __init__( self, dibujo ):
        # Importante: Primero hay que inicializar la clase Sprite original
        pygame.sprite.Sprite.__init__( self )
        # Almacenar en el sprite la imagen deseada
        self.image = pygame.image.load(dibujo)
        self.image = self.image.convert()
        # Definir el rect del sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 150)
        # Definir las velocidades
        self.dx = 5.0
        self.dy = 1.0
        
    def update(self):
    # Modificar la posición del sprite
        self.rect.move_ip(self.dx,self.dy)
        # Comprobar si hay que cambiar el movimiento
        if self.rect.left < 0 or self.rect.right > 640:
            self.dx = -self.dx
            self.image = pygame.transform.flip( self.image, True, False )
            self.rect.move_ip(self.dx,self.dy)
        if self.rect.top < 0 or self.rect.bottom > 480:
            self.dy = -self.dy
            self.rect.move_ip(self.dx,self.dy)
        # Simular la gravedad sumando una cantidad a la velocidad vertical
        self.dy = self.dy + 0.5
        
# Inicializar PyGame y crear la Surface del juego
pygame.init()
visor = pygame.display.set_mode((640, 480))

# Inicializar el sprite
sprite = MiSprite("data/mario.bmp")
grupo = pygame.sprite.RenderUpdates( sprite )

# Crear un reloj para controlar la animación
reloj = pygame.time.Clock()

# El bucle de la animación
while 1:
    #Fijar la animación a 60 fps
    reloj.tick(60)
    
    # Gestionar los eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    # Actualizar el sprite
    grupo.update()
    # Dibujar la escena
    visor.fill((255,255,255))
    grupo.draw( visor )
    # Mostrar la animación
    pygame.display.update()
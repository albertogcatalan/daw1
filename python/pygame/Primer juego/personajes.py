# -*- coding: utf-8 -*-

'''
Created on 16/12/2011

@author: Alberto
'''
import os
import pygame
from pygame.locals import *
import random

class Mono(object):
    def __init__(self):
        self.imagen = pygame.image.load(os.path.join('img', 'monkey_normal.png'))
        self.rect = self.imagen.get_rect()
        self.iniciar()
        
    def iniciar(self):
        self.rect.centerx = 320
        self.rect.centery = 240
        self.avance_x = 1
        self.avance_y = 1
        self.rebotes = 0
        
    def mover(self):
        if self.rect.right > 640:
            self.avance_x *= -1.4
            self.rect.right = 640
            self.rebotes += 1
        elif self.rect.left < 0:
            self.avance_x *= -1.4
            self.rebotes += 1
        
        if self.rect.top < 0:
            self.rect.top = 0
            self.avance_y *= -1.4
            self.rebotes += 1
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
            self.avance_y *= -1.4
            self.rebotes += 1
        
        self.rect.centerx += self.avance_x
        self.rect.centery += self.avance_y
        
class Estrella(object):
    def __init__(self):
        self.imagen = pygame.image.load(os.path.join('img', 'estrella.png'))
        self.rect = self.imagen.get_rect()
        self.iniciar()
        
    def iniciar(self):
        self.rect.centerx = 320
        self.rect.centery = 240
        self.avance_x = 2
        self.avance_y = 2
        
    def mover(self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.rect.centerx += 4
        elif keys[K_LEFT]:
            self.rect.centerx -= 4
            
        if self.rect.right > 640:
            self.rect.right = 640

class Pingu(object):
    def __init__(self, v):
        self.imagen = pygame.image.load(os.path.join('img', 'pingu.png'))
        self.rect = self.imagen.get_rect()
        ancho = self.rect.width / 10
        #recortamos imagen
        self.foto1 = self.imagen.subsurface(0, 0, ancho, self.rect.height)
        self.foto2 = self.imagen.subsurface(ancho, 0, ancho, self.rect.height)
        self.foto3 = self.imagen.subsurface(ancho*2, 0, ancho, self.rect.height)
        self.foto4 = self.imagen.subsurface(ancho*3, 0, ancho, self.rect.height)
        self.foto5 = self.imagen.subsurface(ancho*4, 0, ancho, self.rect.height)
        self.foto6 = self.imagen.subsurface(ancho*5, 0, ancho, self.rect.height)
        self.foto7 = self.imagen.subsurface(ancho*6, 0, ancho, self.rect.height)
        self.foto8 = self.imagen.subsurface(ancho*7, 0, ancho, self.rect.height)
        self.foto9 = self.imagen.subsurface(ancho*8, 0, ancho, self.rect.height)
        self.foto10 = self.imagen.subsurface(ancho*9, 0, ancho, self.rect.height)
        self.imagen = self.foto5
        self.iniciar(v)
        
    def iniciar(self, v):
        self.rect.left = 0
        self.rect.centery = 400
        self.avance_x = 2
        self.avance_y = 2
        self.vidas = v
        self.contador = 0
        
    def update(self):
        self.contador += 1
        if self.contador >= 10:
            self.contador = 0
            if self.imagen == self.foto1:
                self.imagen = self.foto2
            else:
                self.imagen = self.foto1
                
    def mover(self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.rect.centerx += 4
        elif keys[K_LEFT]:
            self.rect.centerx -= 4
            
        if self.rect.right > 640:
            self.rect.right = 640
            
    def choca(self, bomba):
        # devuelve true cuando toca la bomba
        return self.rect.colliderect(bomba.rect)
            
class Bomba(object):
    def __init__(self):
        self.imagen = pygame.image.load(os.path.join('img', 'bomba.png'))
        self.rect = self.imagen.get_rect()
        ancho = self.rect.width / 2
        #recortamos imagen
        self.bombapeque = self.imagen.subsurface(0, 0, ancho, self.rect.height)
        self.bombagrande = self.imagen.subsurface(ancho, 0, ancho, self.rect.height)
        self.imagen = self.bombapeque
        self.iniciar()
        
    def iniciar(self):
        self.rect.centerx = random.randint(0, 640)
        self.rect.centery = 0
        self.avance_x = 2
        self.avance_y = 2
        self.explosion = 0
        self.contador = 0
        self.explota = False
        
    def update(self):
        self.contador += 1
        if self.contador >= 10:
            self.contador = 0
            if self.imagen == self.bombapeque:
                self.imagen = self.bombagrande
            else:
                self.imagen = self.bombapeque
            
    def mover(self):
        if self.rect.top < 0:
            self.rect.top = 0
            self.avance_y *= -1.4
        elif self.rect.bottom > 480:
            self.rect.top = 0
            self.rect.centerx = random.randint(0, 640)
            self.explosion += 1
            self.explota = True
        
        self.rect.centery += self.avance_y
        
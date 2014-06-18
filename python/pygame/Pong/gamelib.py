# -*- coding: utf-8 -*-

'''
Created on 11/01/2012

@author: Alberto
'''
import pygame
from pygame.locals import *
import os
import time

# constantes
BLANCO = (255,255,255)
AMARILLO = (255,255,0)

class Pelota(object):
    def __init__(self):
        self.x = 400
        self.y = 300
        self.dx = 5
        self.dy = 5
        ruta_sonido = os.path.join('data', 'sonidoPelota.wav')
        self.sonido = pygame.mixer.Sound(ruta_sonido)
    def update(self):
        if self.y < 5 or self.y > 595:
            self.dy *= -1
            self.sonido.play()
        self.x += self.dx
        self.y += self.dy
    def draw(self, screen):
        pygame.draw.circle(screen, BLANCO, (self.x, self.y),4,0)
        
class Raqueta(object):
    def __init__(self, x):
        self.x = x
        self.y = 250
        self.dy = 5
        ruta_sonido = os.path.join('data', 'sonidoRaqueta.wav')
        self.sonido = pygame.mixer.Sound(ruta_sonido)
        self.puntos = 0
    def update_left(self, pelota):
        teclas = pygame.key.get_pressed()
        if teclas[K_a]:
            self.y += self.dy
        if teclas[K_q]:
            self.y -= self.dy
        self.resize()
        diff1 = pelota.y - self.y
        if pelota.x == self.x + 10 and diff1 >= 0 and diff1 <= 50:
            pelota.dx = -pelota.dx
            self.sonido.play()
        if pelota.x > 800:
            self.puntuaciones(pelota)
    def update_right(self, pelota):
        teclas = pygame.key.get_pressed()
        if teclas[K_l]:
            self.y += self.dy
        if teclas[K_p]:
            self.y -= self.dy
        self.resize()
        diff2 = pelota.y - self.y
        if pelota.x == self.x and diff2 >= 0 and diff2 <= 50:
            pelota.dx = -pelota.dx
            self.sonido.play()
        if pelota.x < 0:
            self.puntuaciones(pelota)
    def resize(self):
        if self.y < 0:
            self.y = 0
        elif self.y > 550:
            self.y = 550
    def puntuaciones(self, pelota):
        ruta_sonido = os.path.join('data', 'sonidoError.wav')
        self.sonido_error = pygame.mixer.Sound(ruta_sonido)
        self.sonido_error.play()
        time.sleep(1)
        self.puntos += 1
        # debug: print self.puntos
        pelota.x = 400
        pelota.dx = -pelota.dx
    def draw(self, screen):
        pygame.draw.rect(screen, BLANCO, (self.x,self.y,10,50))
        
class Marcador(object):
    def draw(self, screen, j1, j2):
        for i in range(10):
            pygame.draw.rect(screen, BLANCO, (398,10+60*i,4,30))
        ruta_letra = os.path.join('data', 'Grandezza.ttf')
        marcador = pygame.font.Font(ruta_letra, 96)
        screen.blit(marcador.render(str(j1), True, BLANCO), (270,20,50,50))
        screen.blit(marcador.render(str(j2), True, BLANCO), (470,20,50,50))
        
class Escenario(object):
    def draw(self, screen):
        fondo = pygame.image.load(os.path.join('data', 'pingpong.jpg')).convert()
        screen.blit(fondo, (0,0))
        mensaje1 = 'PONG'
        ruta_letra = os.path.join('data', 'Grandezza.ttf')
        tipoLetra = pygame.font.Font(ruta_letra, 96)
        tipoLetra2 = pygame.font.Font(ruta_letra, 24)
        texto1 = tipoLetra.render(mensaje1, True, AMARILLO)
        mensaje2 = 'Pulsa una tecla para comenzar'
        texto2 = tipoLetra2.render(mensaje2, True, BLANCO)
        screen.blit(texto1, (50,100,200,100))
        screen.blit(texto2, (235,340,350,30))
        pygame.display.update()
        
        esperar = True
        while esperar:
            for evento in pygame.event.get():
                if evento.type == KEYDOWN:
                        esperar = False
        ruta_sonido = os.path.join('data', 'sonidoLaser.wav')
        self.sonido_play = pygame.mixer.Sound(ruta_sonido)
        self.sonido_play.play()
        
    def update(self, screen, j1, j2):
        ruta_sonido = os.path.join('data', 'sonidoAplausos.wav')
        self.sonido_aplausos = pygame.mixer.Sound(ruta_sonido)
        self.sonido_aplausos.play()
        if j1 == 11:
            ganador = 'Jugador 1'
        else:
            ganador = 'Jugador 2'
        mensaje = 'Ganador: '+ ganador
        ruta_letra = os.path.join('data', 'Grandezza.ttf')
        tipoLetra3 = pygame.font.Font(ruta_letra, 48)
        texto = tipoLetra3.render(mensaje, True, AMARILLO)
        screen.blit(texto, (110,350,600,100))
        pygame.display.update()
        
        esperar = True
        while esperar:
            for evento in pygame.event.get():
                if evento.type == KEYDOWN:
                        esperar = False
        self.sonido_play.play()
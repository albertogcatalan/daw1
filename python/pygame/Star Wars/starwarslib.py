# -*- coding: utf-8 -*-


import os
import pygame
import random

# vars globales
ANCHO  = 800
ALTO = 600

def cargar_imagen(archivo, usarTransparencia = False):
    '''
    cargar_imagen(archivo) --> imagen
    Carga una imagen desde un archivo, devolviendo el objeto apropiado)
    '''
    lugar = os.path.join( "data", archivo )
    try:
        imagen = pygame.image.load(lugar)
    except pygame.error, mensaje:
        print "No puedo cargar la imagen:", lugar
        raise SystemExit, mensaje
    imagen = imagen.convert()
    if usarTransparencia:
        colorTransparente = imagen.get_at( (0,0) )
        imagen.set_colorkey( colorTransparente )
    return imagen


def cargar_sonido( archivo ):
    '''
    cargar_sonido(archivo) --> devuelve objeto Sound
    '''
    class SinSonido:
        def play( self ):
            pass

    if not pygame.mixer or not pygame.mixer.get_init():
        return SinSonido()

    lugar = os.path.join( "data", archivo )

    try:
        sound = pygame.mixer.Sound( lugar )
    except pygame.error, message:
        print "No puedo cargar el sonido:", lugar
        raise SystemExit, message

    return sound


class XWing( pygame.sprite.Sprite ):
    '''
    Nave del jugador
    '''
    laser_grupo = pygame.sprite.RenderUpdates()

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.normal = cargar_imagen("xwing.bmp", True)
        self.motor = cargar_imagen("xwing_motor.bmp", True)
        self.image = self.normal
        self.ciclos = 0
        self.disparo = cargar_sonido( "rebel_laser.wav" )
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO/2,ALTO)
        self.dx = 0
        self.dy = 0
        self.vidas = 3
        self.puntos = 0
        self.lista_exp = []
        self.lista_explosion()
        self.explotando = 0
        
    def anima(self):
        self.ciclos += 1
        if self.ciclos > 5:
            if self.ciclos < 10:
                self.image = self.motor
            else:
                self.ciclos = 0
                self.image = self.normal
    def update(self):               
        self.anima()
        self.explota()
        self.rect.move_ip((self.dx, self.dy))
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > ANCHO:
            self.rect.right = ANCHO

        if self.rect.top <= ALTO/2:
            self.rect.top = ALTO/2
        elif self.rect.bottom >= ALTO:
            self.rect.bottom = ALTO
    def dispara(self):
        XWing.laser_grupo.add(XWingLaser(self.rect.midtop))
        self.disparo.play()
        
    def lista_explosion(self):
        for i in range(1, 7):
            self.lista_exp.append(cargar_imagen("fire1_ 0"+str(i)+".png", True))
            
    def explota(self):
        if self.explotando > 0:
            self.image = self.lista_exp[self.explotando / 5]
            self. explotando -= 1
        #self.explosion.play()
        
        
class TIEFighter( pygame.sprite.Sprite ):
    '''
    Nave enemiga
    '''
    laser_grupo = pygame.sprite.RenderUpdates()
    def __init__( self, posx ):
        pygame.sprite.Sprite.__init__( self )
        self.image = cargar_imagen( "tie_fighter.bmp", True )
        self.disparo = cargar_sonido( "empire_laser.wav" )
        self.explosion =  cargar_sonido( "explode1.wav" )
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = 120
        self.dx = random.randint( -5, 5 )
        self.dy = random.randint( -5, 5 )
        
    def update( self ):
        self.rect.move_ip( (self.dx, self.dy) )

        if self.rect.left < 0 or self.rect.right > ANCHO:
            self.dx = -(self.dx)

        if self.rect.top < 0 or self.rect.bottom > ALTO/2:
            self.dy = -(self.dy)

        disparar = random.randint( 1, 60 )
        if disparar == 1:
            TIEFighter.laser_grupo.add(TIEFighterLaser(self.rect.midbottom ))
            self.disparo.play()
    def explota(self):
        self.explosion.play()
        


class XWingLaser( pygame.sprite.Sprite ):
    '''
    Disparos del jugador
    '''
    
    def __init__( self, pos ):
        pygame.sprite.Sprite.__init__( self )
        self.image = cargar_imagen( "rebel_laser2.bmp", True )
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update( self ):
        if self.rect.bottom <= 0:
            self.kill()
        else:
            self.rect.move_ip( (0,-4) )
            

class TIEFighterLaser( pygame.sprite.Sprite ):
    '''
    Disparos del enemigo
    '''
    
    def __init__( self, pos ):
        pygame.sprite.Sprite.__init__( self )
        self.image = cargar_imagen( "empire_laser2.bmp", True )
        self.rect = self.image.get_rect()
        self.rect.midtop = pos
        
    def update( self ):
        if self.rect.bottom >= ALTO:
            self.kill()
        else:
            self.rect.move_ip( (0,4) )
            

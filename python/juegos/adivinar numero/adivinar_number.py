# -*- coding: utf-8 -*-

from easygui import *
import random

numero = random.randint(1,100) # generamos el numero aleatorio
contador = 0 # contador del while
vidas = 10 # contador de vidas

while contador == 0:
    if vidas <> 0:
        # caja inicial del juego
        secreto = enterbox('Adivina el número', 'Vidas restantes: %d' % vidas)
        secreto = int(secreto)
        if secreto == numero:
            # en caso de acierto
            msgbox('Has acertado el número')
            contador = 1
        elif secreto > numero:
            # en caso de numero oculto menor
            msgbox('El numero oculto es menor')
            vidas -= 1
        elif secreto < numero:
            # en caso de numero oculto mayor
            msgbox('El numero oculto es mayor')
            vidas -= 1
    else:
        # en caso de perder por tener menos de 10 vidas
        msgbox('Has perdido :(')
        contador = 1
        
        
    

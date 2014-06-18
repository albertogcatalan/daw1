from easygui import *
import random

# rango de posibles palabras
palabras = ['python', 'culebrilla', 'serpiente', 'sorin', 'alberto', 'zoo', 'zocalo', 'zapato', 'zaragoza',
            'cigarro', 'feisbuc', 'tuiter', 'iahuu', 'gogle', 'hinchado', 'mujeres', 'drojas', 'dinero',
            'abecedario', 'colinas', 'dado', 'burro', 'electroiman', 'papel', 'zanahoria', 'cocodrilo',
            'teclado', 'android', 'abelabs', 'arnold schwarzenegger']


secreto = random.choice(palabras) # devuelve una palabra al azar

acertado = secreto # el jugador ha adivinado la palabra
intentos =  8 # intentos
letra = ''


while contador == 0:
    if intentos <> 0:
        # ventana principal
        ventana=indexbox(msg='Intentos restantes: %d' % intentos, title='Juego del Ahorcado', choices=('Jugar', 'Salir'), image=imagen)
        if ventana == 0:
            # introducir palabras
            introducir = enterbox('Pista: La palabra es %s' % inicial, 'Inserta una letra')
            '''for x in secreto:'''
            if introducir == secreto:
                letra += introducir
                # en caso de acertar
                msgbox('Has acertado una letra.', 'Juego del Ahorcado')
                    
                
                else:
                    # en caso de fallar
                    msgbox('Incorrecto!', 'Juego del Ahorcado')
                intentos -= 1
                if intentos == 7:
                    imagen = '2.gif'
                elif intentos == 6:
                    imagen = '3.gif'
                elif intentos == 5:
                    imagen = '4.gif'
                elif intentos == 4:
                    imagen = '5.gif'
                elif intentos == 3:
                    imagen = '6.gif'
                elif intentos == 2:
                    imagen = '7.gif'
                elif intentos == 1:
                    imagen = '8.gif'
            
            
        else:
            break
    else:
        # en caso de perder por tener menos de 10 vidas
        msgbox('Has perdido :(', 'Juego del Ahorcado')
        contador = 1

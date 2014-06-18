from easygui import *
import random

# rango de posibles palabras
palabras = ['python', 'culebrilla', 'serpiente', 'sorin', 'alberto', 'zoo', 'zocalo', 'zapato', 'zaragoza',
            'cigarro', 'feisbuc', 'tuiter', 'iahuu', 'gogle', 'hinchado', 'mujeres', 'drojas', 'dinero',
            'abecedario', 'colinas', 'dado', 'burro', 'electroiman', 'papel', 'zanahoria', 'cocodrilo',
            'teclado', 'android', 'abelabs', 'arnold schwarzenegger']


secreto = random.choice(palabras) # devuelve una palabra al azar
imagen = '1.gif' # imagen
contador = 0 # contador del bucle
intentos =  8 # intentos
cont = 0
letra = ''
palabra = ''
i = 0
print secreto
inicial = (' _ ')*len(secreto)
while contador == 0:
    if intentos <> 0:
        # ventana principal
        ventana = indexbox(msg='Intentos restantes: %d' % intentos, title='Juego del Ahorcado', choices=('Jugar', 'Salir'), image=imagen)
        if ventana == 0:

            # introducir palabras
            introducir = enterbox('La palabra es %s' % inicial, 'Inserta una letra')
            
            for x in secreto:
                if introducir == x:
                    cont += 1
                    letra += introducir
                    print letra

            if cont >= 1:
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

            
            inicial = ''
            for x in secreto:
                if x in letra:
                    inicial += ' '+x+' '
                else:
                    inicial += ' _ '
                
        else:
            break
    else:
        # en caso de perder por tener menos de 8 vidas
        msgbox('Has perdido :(', 'Juego del Ahorcado')
        contador = 1

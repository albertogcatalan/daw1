'''
Escribe un programa que calcula la suma de
los números de 1 a 20 (incluyendo ambos números)
Version EASYGUI
'''

from easygui import *

# etiqueta resultado inicializada a 0
resultado = 0

# Valor inicial y valor final
inicial = int(enterbox('Introduce el valor inicial:'))
final = int(enterbox('Introduce el valor final:'))



# for ...range para recorrer valor inicial al final
# incrementando resultado en cada iteración
for num in range(inicial, final+1): # +1 porque range no coge que valor final
    resultado += num
    # resultado = resultado + num == sería lo mismo
    # print ' >   res:', resultado

    # para hacer directamente: sum(range(1,21)):
    
# mostrar resultado
msgbox('La suma es %d' % resultado)



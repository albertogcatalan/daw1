# -*- coding: utf-8 -*-
'''
Escribe un programa que pida un número (el número de notas que vamos a introducir). Después pedirá las notas y calculará la media.
'''
from easygui import *

notas = int(enterbox('Introduce la cantidad de notas: '))
resultado = 0

for i in range(notas): 
    notalol = float(enterbox('Introduce una nota: '))
    resultado += notalol
    
media = resultado / float(notas)
msgbox('La media es %.2f' % media)



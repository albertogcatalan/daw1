# -*- coding: utf-8 -*-

from easygui import *

ano = int(enterbox('Introduce año: '))
divisible = ano % 4

if divisible == 0:
    msgbox('Es año bisiesto')
elif divisible <> 0:
    msgbox('Nada')

        
    

# -*- coding: utf-8 -*-

from easygui import *

ph = float(enterbox('Introduce el ph de la solución: '))

if ph < 7.0 and ph >= 3.0:
    msgbox('La solución es ácida.')
elif ph < 3.0:
    msgbox('La solución es peligrosamente ácida.')

# -*- coding: cp1252 -*-
'''
Programa que calcula el perímetro
'''

import easygui

base = easygui.enterbox('Introduce la base', 'Área rectángulo')
base = int(base)

altura = easygui.enterbox('Introduce la altura', 'Área rectángulo')
altura = int(altura)

area = base * altura

easygui.msgbox('El resultado es: ' + str(area), 'LOL')

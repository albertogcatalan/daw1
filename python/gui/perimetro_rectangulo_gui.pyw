# -*- coding: cp1252 -*-
'''
Programa que calcula el perímetro
'''

import easygui

base = easygui.enterbox('Introduce la base', 'Área rectángulo')
base = int(base)

altura = easygui.enterbox('Introduce la altura', 'Área rectángulo')
altura = int(altura)

perimetro = 2*base + 2*altura
area = base * altura

mensaje = 'El área es ' + str(area)

mensaje2 = 'y el perímetro es ' + str(perimetro)

mensaje3 = easygui.msgbox(mensaje.center(100)+'\n'+mensaje2.center(100), 'Resultados')

# -*- coding: cp1252 -*-
'''
Programa que calcula el per�metro
'''

import easygui

base = easygui.enterbox('Introduce la base', '�rea rect�ngulo')
base = int(base)

altura = easygui.enterbox('Introduce la altura', '�rea rect�ngulo')
altura = int(altura)

perimetro = 2*base + 2*altura
area = base * altura

mensaje = 'El �rea es ' + str(area)

mensaje2 = 'y el per�metro es ' + str(perimetro)

mensaje3 = easygui.msgbox(mensaje.center(100)+'\n'+mensaje2.center(100), 'Resultados')

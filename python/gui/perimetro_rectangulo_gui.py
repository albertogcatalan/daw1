# -*- coding: cp1252 -*-
'''
Programa que calcula el per�metro
'''

import easygui

base = easygui.enterbox('Introduce la base', '�rea rect�ngulo')
base = int(base)

altura = easygui.enterbox('Introduce la altura', '�rea rect�ngulo')
altura = int(altura)

area = base * altura

easygui.msgbox('El resultado es: ' + str(area), 'LOL')

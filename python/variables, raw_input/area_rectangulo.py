# -*- coding: cp1252 -*-

x1 = int(raw_input('Escribe la coordenada x1: '))
x2 = int(raw_input('Escribe la coordenada x2: '))
y1 = int(raw_input('Escribe la coordenada y1: '))
y2 = int(raw_input('Escribe la coordenada y2: '))

lado = int(x2 - x1)
lado1 = int(y2 - y1)
area = int(lado) * int(lado1)
print area

# -*- coding: cp1252 -*-
from math import sqrt
cateto1 = raw_input('Escribe el cateto1: ')
cateto2 = raw_input('Escribe el cateto2: ')
hipotenusa =  int(cateto1)**2 + int(cateto2)**2
resultado = sqrt(int(hipotenusa))
print resultado

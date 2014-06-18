# -*- coding: cp1252 -*-
from graphics import *

def sumaNCubos(n):
    resultado = 0
    for num in range(1, n+1):
        resultado += int(num**3)
    return resultado

numero = int(raw_input('Introduce cantidad de numeros: '))
print sumaNCubos(numero)

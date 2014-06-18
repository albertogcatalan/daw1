# -*- coding: cp1252 -*-
from graphics import *

def sumaN(n):
    resultado = 0
    for num in range(1, n+1):
        resultado += num
    return resultado

numero = int(raw_input('Introduce cantidad de numeros: '))
print sumaN(numero)

# -*- coding: utf-8 -*-
'''lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for numero in lista:
    print numero,
    if numero % 3 == 0:
        print

lista = ['a', 'b', 'c', 'd']
contador = 1
for letra in lista:
    print letra,
    if contador % 3 == 0:
        print
    contador += 1

for n, letra in enumerate(lista):
    print letra,
    if (n+1) % 3 == 0:
        print'''

lista_alumnos = 'Luis Pérez,Sorin Vleju,Alberto González'.split(',')
for n, alumno in enumerate(lista_alumnos):
    print n+1, alumno

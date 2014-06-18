# -*- coding: utf-8 -*-
 
'''
Programa que procesa el archivo de texto
alumnos.txt, que tiene el nombre de un alumno
y sus notas en cada línea.
 
Created on 28/11/2011

'''
 
import sys
from operator import itemgetter
 
try:
    # Instrucción con riesgo
    f = open('alumnos.txt')
except IOError:
    print "Error, el fichero alumnos no existe"
    sys.exit()
   
# f : objeto file abierto en modo lectura
alumnos = []
for linea in f:
    alumno = linea.split()
    if len(alumno) == 3:
        nombre = alumno[0]
        nota = int(alumno[1]) + int(alumno[2])
        # cálculo de media usando map + sum
        media = sum(map(int, alumno[1:]))/2.
        alumnos.append((nombre, media))
        #print nombre, nota/2., media
   
# Mostrar ordenado por nombre
for al in sorted(alumnos):
    print u"%-12s %5.1f" % al
 
print '*' * 40
# Mostrar ordenado por nota
alumnos.sort(key=itemgetter(1), reverse=True)
for al in alumnos:
    print u"%-12s %5.1f" % al

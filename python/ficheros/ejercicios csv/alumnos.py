# -*- coding: utf-8 -*-

'''
Created on 02/12/2011

@author: Alberto
'''

import csv
from operator import itemgetter

def media(alumno):
    nota1 = int(alumno['nota1'])
    nota2 = int(alumno['nota2'])
    nota3 = int(alumno['nota3'])
    return round(nota1 + nota2 + nota3)/3.
    
    
fin = open('alumnos.csv')
alumnos = []
#lector = csv.reader(fin, delimiter=";") #lista/posiciones
lector = csv.DictReader(fin, delimiter=";") #diccionario
for fila in lector:
    alumnos.append((fila['alumno'], media(fila)))
    
alumnos.sort()
print 'Orden por nombre'
for al in alumnos:
    print "%-10s %6.2f" % al
    
    
fw = open('lista_ordenada_notas.csv', 'w')
csvwriter = csv.writer(fw, delimiter=';')
for al in alumnos:
    csvwriter.writerow(al)
    
fw.close()
# -*- coding: utf-8 -*-
 
'''
Created on 28/11/2011

@author: Alberto
'''

import sys
from operator import itemgetter
 
try:
    # Instrucción con riesgo
    f = open('temperaturas.txt')
    f.readline()
except IOError:
    print "Error, el fichero temperaturas no existe"
    sys.exit()
   
# f : objeto file abierto en modo lectura
temperaturas = []
for linea in f:
    temp = linea.split()
    if len(temp) == 12:
        a = temp[0]
        media = temp[1]
        temperaturas.append((a, media))
        #print nombre, nota/2., media
   

for al in temperaturas:
    print u"%-12s %s" % al

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
   
temperaturas_total = []
temperaturas_media = []
for linea in f:
    temp = linea.split()
    if len(temp) == 12:
        temperaturas_total.append((temp[0], temp[1], temp[2], temp[3]))
        temperaturas_media.append((temp[0], temp[1]))
    

temperaturas_media.sort(key=itemgetter(1), reverse=True)
    
f = open('temperaturas.html', 'w')
f.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>Temperaturas de Zaragoza</title></head><body><h1 align="center">Temperaturas de Zaragoza</h1><p align="center"><a href="http://www.tutiempo.net/clima/Zaragoza_Aeropuerto/81600.htm">Más información aquí.</a></p><table border="1" bordercolor="#666" cellpadding="10" align="center">')
f.write('<tr bgcolor="#00FFFF"><td>Año</td><td>Temp. Media (ºC)</td><td>Temp. Máxima (ºC)</td><td>Temp. Mínima (ºC)</td></tr>')
for al in temperaturas_total:
    f.write('<tr><td align="center">%s</td><td align="center">%s</td><td align="center">%s</td><td align="center">%s</td></tr>' % al)
    
f.write('</table></body></html>')
f.close()

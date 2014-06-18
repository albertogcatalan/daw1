# -*- coding: utf-8 -*-

'''
Created on 30/11/2011

@author: Alberto
'''
from urllib2 import urlopen
from json import load
 
urlt = 'http://www.zaragoza.es/trafico/estado/estado.json'
urlid = 'http://www.zaragoza.es/trafico/estado/tramoswgs84.json'
estado = load(urlopen(urlt))
coord = load(urlopen(urlid))
 
# datos de estado en estados
estado = estado['estados']
coord = coord.get('tramos')


i =0
negro = []
rojo = []
amarillo = []


#bucle para listar los indices de cada tramo/color
for salto in estado:
    if salto == 'b':
        negro.append(i)
    if salto == 'y':
        amarillo.append(i)
    if salto == 'r':
        rojo.append(i)        
    i+=1
     
print negro, amarillo, rojo

# comprobamos estado del tramo
if len(negro) == 0:
    print "No hay tráfico en negro"
else:
    for a in negro:
        print coord[a]['name']
        
        
if len(rojo) == 0:
    print "No hay tráfico en rojo"
else:
    for a in rojo:
        print coord[a]['name']
        
        
if len(amarillo) == 0:
    print "No hay tráfico en amarillo"
else:
    for a in amarillo:
        print coord[a]['name']
    
        
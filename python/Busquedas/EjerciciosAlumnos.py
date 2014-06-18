# -*- coding: utf-8 -*-

'''
Created on 15/02/2012

@author: Alberto
'''

class Alumno(object):
    def __init__(self, nombre):
        self.nombre = nombre
        
def buscar(nombre, lista):
    '''devuelve el indice del alumno en la lista
    si no devuelve -1
    '''
    i = 0
    for i, valor in enumerate(lista):
        if valor.nombre == nombre:
            return i
    return -1
        
        
if __name__ == '__main__':
    # profile
    import time
    lista = []
    for x in range(10000):
        lista.append(Alumno('Pepito'))
    lista.append(Alumno('Pepita'))
    
    timein = time.time()
    for x in range(100):
        buscar('Pepita', lista)
    timefin = time.time()
    print 'Búsqueda con for', (timefin-timein)*1000
    
    
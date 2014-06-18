# -*- coding: utf-8 -*-

'''
Created on 20/02/2012

@author: Alberto
'''
import time

def busca_mayores_1(lista):
    
    copia = lista[:]
    def mayor(l):
        '''devuelve el indice del elemento mayor'''
        i = 0
        for n, valor in enumerate(l):
            if l[i] < valor:
                i = n
        return i
   
    mayor1 = mayor(copia)
    copia.pop(mayor1)
    mayor2 = mayor(copia)
    
    if mayor2 >= mayor1:
        mayor2 += 1
    
    return [mayor1, mayor2]


def busca_mayores_2(lista):
    '''devuelve el indice del elemento'''
    mayor1, mayor2 = sorted(lista, reverse=True)[:2]
    imayor1 = None
    imayor2 = None
    
    for n, valor in enumerate(lista):
        if imayor1 == None and mayor1 == valor:
            imayor1 = n
        elif mayor2 == valor:
            imayor2 = n
        if imayor1 != None and imayor2 != None:
            break
    return [imayor1, imayor2]
    
def busca_mayores_3(lista):
    if lista[0] >= lista[1]:
        mayor1 = lista[0]
        mayor2 = lista[1]
        indice1 = 0
        indice2 = 1
    else:
        mayor1 = lista[1]
        mayor2 = lista[0]
        indice1 = 1
        indice2 = 0
    
    for n, valor in enumerate(lista[2:]):
        if valor >= mayor1:
            indice2 = indice1
            mayor2 = mayor1
            indice1 = n+2
            mayor1 = valor
        elif mayor2 < valor:
            indice2 = n+2
            mayor2 = valor
        
    return [indice1, indice2]

def time_it(busqueda, L):
    tini = time.time()
    busqueda(L)
    tfin = time.time()
    return (tfin - tini) * 1000


if __name__ == '__main__':
    LISTA = range(100000)
    print time_it(busca_mayores_1,LISTA)
    print time_it(busca_mayores_2,LISTA)
    print time_it(busca_mayores_3,LISTA)
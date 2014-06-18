# -*- coding: utf-8 -*-

'''
Created on 13/02/2012

@author: Alberto
'''
import unicodedata

def textplain(s):
    def normalize(c):
        return unicodedata.normalize("NFD", c)[0]
    return ''.join(normalize(c) for c in s)

def cuenta_vocales(cadena):
    '''
    devuelve el numero de vocales de una cadena
    '''
    contador = 0
    cadena = unicode(cadena, encoding= 'utf-8')
    cadena = cadena.lower()
    cadena = textplain(cadena)
    
    for letra in cadena:
        if letra in 'aeiou':
            contador += 1
    return contador

'''if __name__ == '__main__':
    print cuenta_vocales('frío')'''
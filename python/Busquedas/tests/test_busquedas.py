# -*- coding: utf-8 -*-

'''
Created on 15/02/2012

@author: Alberto
'''

from algoritmos_busqueda import *

lista_n = range(1000)
lista_pal = ['hola', 'adiós', 'me', 'python']

def test_blineal_w():
    assert busqueda_lineal_w(0, lista_n) == 0
    assert busqueda_lineal_w(10000, lista_n) == 1000
    assert busqueda_lineal_w(50, lista_n) == 50
    
def test_blineal_w_palabras():
    assert busqueda_lineal_w('noesta', lista_pal) == 4
    assert busqueda_lineal_w('python', lista_pal) == 3
    
def test_blineal_f_palabras():
    assert busqueda_lineal_for('noesta', lista_pal) == 4
    assert busqueda_lineal_for('adiós', lista_pal) == 1

def test_blineal_forenum_palabras():
    assert busqueda_lineal_forenum('noesta', lista_pal) == 4
    assert busqueda_lineal_forenum('hola', lista_pal) == 0
    assert busqueda_lineal_forenum('me', lista_pal) == 2

def test_blineal_centinela_palabras():
    assert busqueda_lineal_centinela('noesta', lista_pal) == 4
    assert busqueda_lineal_centinela('hola', lista_pal) == 0
    assert busqueda_lineal_centinela('me', lista_pal) == 2
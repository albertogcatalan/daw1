# -*- coding: utf-8 -*-

'''
Created on 20/02/2012

@author: Alberto
'''

from buscar import *
import time

lista1 = [1,2,3,4,5]
lista2 = [1,20,30,4,5]
lista3 = [8,9,1,2,3,4,5]
lista4 = [10,9,1,2,3,4,5]
lista5 = [9,9,1,2,3,4,5]

def test_busca_mayores_inicio():
    assert busca_mayores_1(lista1) == [4,3]
    assert busca_mayores_2(lista1) == [4,3]
    assert busca_mayores_3(lista1) == [4,3]
    assert lista1 == [1,2,3,4,5]
    
def test_busca_mayores_medio():
    assert busca_mayores_1(lista2) == [2,1]
    assert busca_mayores_2(lista2) == [2,1]
    assert busca_mayores_3(lista2) == [2,1]
    assert lista2 == [1,20,30,4,5]
    
def test_busca_mayores_fin():
    assert busca_mayores_1(lista3) == [1,0]
    assert busca_mayores_2(lista3) == [1,0]
    assert busca_mayores_3(lista3) == [1,0]
    assert lista3 == [8,9,1,2,3,4,5]
    
def test_busca_mayores_reves():
    assert busca_mayores_1(lista4) == [0,1]
    assert busca_mayores_2(lista4) == [0,1]
    assert busca_mayores_3(lista4) == [0,1]
    assert lista4 == [10,9,1,2,3,4,5]
    
def test_busca_mayores_iguales():
    assert busca_mayores_1(lista5) == [0,1]
    assert busca_mayores_2(lista5) == [0,1]
    assert busca_mayores_3(lista5) == [0,1]
    assert lista5 == [9,9,1,2,3,4,5]

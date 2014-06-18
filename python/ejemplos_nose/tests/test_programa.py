# -*- coding: utf-8 -*-

'''
Created on 10/02/2012

@author: Alberto
'''

from programa import *

def test_suma():
    assert suma( 0, 0) == 0
    assert suma( 5, 5) == 10
    assert suma( -5, 5) == 0
    
def test_multiplica_positivos():
    assert multiplica( 5, 10) == 50
    
def test_multiplica_negativos():
    assert multiplica( -1, -5) == 5
    
def test_division_positiva():
    assert division( 10, 2) == 5

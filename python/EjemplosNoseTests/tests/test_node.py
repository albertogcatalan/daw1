# -*- coding: utf-8 -*-

'''
Created on 13/02/2012

@author: Alberto

'''
from funciones import *

def test_cuenta_vocales():
    
    assert cuenta_vocales('casa') == 2
    assert cuenta_vocales('CASA') == 2
    assert cuenta_vocales('sdfg') == 0

def test_cuenta_vocales_acento(): 
    
    assert cuenta_vocales('frío') == 2
    assert cuenta_vocales('FRÍO') == 2
    assert cuenta_vocales('murciélago') == 5
    
def test_cuenta_vocales_dieresis():
    
    assert cuenta_vocales('cigüeña') == 4
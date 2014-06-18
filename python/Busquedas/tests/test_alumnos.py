# -*- coding: utf-8 -*-

'''
Created on 15/02/2012

@author: Alberto
'''

from EjerciciosAlumnos import *

lista = []

lista.append(Alumno('Luis'))
lista.append(Alumno('Pepe'))
lista.append(Alumno('Ana'))
lista.append(Alumno('Eva'))

def test_encuentra():
    assert buscar('Luis', lista) == 0
    assert buscar('Jaime', lista) == -1
    assert buscar('Ana', lista) == 2
# -*- coding: utf-8 -*-

'''
Created on 25/11/2011

Trocear/Unir

@author: Alberto González (AbeLabs)
@version: 0.1
'''

from easygui import *
import os

def trocear(ruta, tam):
    
    f = open(ruta, 'rb')
    n = 1
    
    while True:
        trozo = f.read(tam)
        
        if trozo:
            fw = open("%s.%03d" % (ruta, n), 'wb')
            n += 1
            fw.write(trozo)
            fw.close()
        else:
            break
        
def unir(archivo):
    
    
    fw = open('nuevo_' +archivo, 'wb')
    n = 1
    
    while True:
        
        if os.path.exists(archivo):
            fr = open(archivo, 'rb')
            fw.write(fr.read())
            fr.close()
            n += 1
        else:
            break
        
    fw.close()
        



while True:
    ventana = indexbox('Selecciona una opción:','Trocear/Unir', ('Trocear', 'Unir', 'Salir'))
    
    if ventana == 0:
        archivo = fileopenbox('', 'Archivo a trocear')
        print archivo
        if archivo:
            trocear(archivo, 6*1024) #bytes
            msgbox('Archivo troceado con éxito.', 'Trocear/Unir')
        else:
            msgbox('Selecciona un archivo para trocear.', 'Error')
    
    elif ventana == 1:
        archivo = fileopenbox('', 'Archivo a unir')
        
        if archivo:    
            unir(archivo)
            msgbox('Archivo generado con éxito.', 'Trocear/Unir')
            
        else:
            msgbox('Selecciona un archivo para unir.', 'Error')
            
    elif ventana == 2:
        exit()




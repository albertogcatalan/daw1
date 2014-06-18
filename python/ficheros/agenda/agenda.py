# -*- coding: utf-8 -*-
'''
    Agenda Master Pro
    Version 0.2
    By Alberto González (AbeLabs)
'''

from easygui import *
import shelve
import csv


def abre_agenda():#funcion abrir agenda
    return shelve.open('contactos.dat')
    
    
def almacena(f, c):#funcion para guardar los datos
    f[c['nombre']] = c
    f.sync()
        
            
def cierra_agenda(f):#funcion para salir
    f.sync()
    f.close()
    
def exportar_csv(f):#funcion para guardar archivo csv
    f.sync()

    with open('contactos.csv', 'w') as fout:
        datos = open('contactos.dat', 'w')
        escribir = csv.writer(fout)
        escribir.writerow(datos)
        

imagen = 'bg.gif'
f = abre_agenda()

while True:
    ventana = indexbox('Bienvenido a la Agenda','Agenda Master Pro', ('Añadir contacto', 'Buscar contacto', 'Listado', 'Exportar a CSV', 'Salir'), imagen)
    
    if ventana == 0:
        datos = multenterbox('Inserta los campos:', 'Añadir nuevo contacto', ('Nombre y Apellidos', 'Email', 'Teléfono'))
        c = {'nombre': datos[0], 'email': datos[1], 'telefono': datos[2]}
        
        if c == '':
            msgbox('Tienes que insertar un nombre', 'Error')
        
        else:
            almacena(f, c)
    
    
    elif ventana == 1:
        if f.keys() != '':
            buscar = enterbox('Introduce Nombre y Apellido: ', 'Buscar contacto')
            resultado = f.get(buscar, 'No existe contacto')
            msgbox(resultado, 'Buscar contacto')
            
        else:
            msgbox('No existen registros en la agenda.', 'Buscar contacto')
        
        
    elif ventana == 2:
        print f
        if f.keys() != '':
            lista = choicebox('Selecciona un contacto para más información:', 'Listado de contactos', f.keys())
            
            if choicebox <> '':
                resultado = f.get(lista, 'No existe contacto')
                
                msgbox(resultado, 'Contacto')
        
        else:
            msgbox('No existen registros en la agenda.', 'Buscar contacto')

    elif ventana == 3:
        exportar_csv(f)
    elif ventana == 4:
        cierra_agenda(f)
        exit()
        
    














    
    
    

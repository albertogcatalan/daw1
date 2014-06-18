'''
Created on 25/11/2011

@author: Alberto
'''

def crea_fichero():
    fw = open('lista_alumnos.txt', 'w')
    
    while True:
        nombre = raw_input('Introduce nombre alumno > ')
        if nombre:
            fw.write(nombre + '\n')
        else:
            break
    fw.close()
    
    
crea_fichero()
# -*- coding: utf-8 -*-

'''
Created on 22/02/2012

@author: Alberto
'''

import sqlite3 as dbapi
import webbrowser

def crea_tabla(conexion):
    '''Devuelve los resultados en una tabla html.
    empleados.html'''
    cursor = conexion.cursor()
    SELECT = 'select * from empleados'
    cursor.execute(SELECT)
    f = open('empleados.html', 'w')
    f.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>Listado</title></head><body><h1 align="center">Listado</h1><table border="1" bordercolor="#666" cellpadding="10" align="center">')
    f.write('<tr bgcolor="#CC6600"><td>DNI</td><td>Nombre</td><td>Departamento</td></tr>')
    for empleado in cursor.fetchall():
        f.write('<tr><td align="center">'+str(empleado[0])+'</td><td align="center">'+str(empleado[1])+'</td><td align="center">'+str(empleado[2])+'</td></tr>')
           
    f.write('</table></body></html>')
    f.close() 
    cursor.close()

def insertar(conexion):
    micursor = conexion.cursor()
    INSERT = """insert into empleados
                  values (?, ?, ?)"""
    for n in range(100):
        micursor.execute(INSERT, ('12345678' + str(n),
                                  'Empleado_' + str(n),
                                  'Empleados satisfechos'))
    
    conexion.commit()
    micursor.close()
    
def muestra_resultados(conexion):
    cursor = conexion.cursor()
    cursor.execute("select * from empleados")
    for empleado in cursor.fetchall():
        print empleado
    cursor.close()
    
    
if __name__ == '__main__':
    conexion = dbapi.connect('alumnos.bd')
    #insertar(conexion)
    muestra_resultados(conexion)
    crea_tabla(conexion)
    webbrowser.open('empleados.html')
    conexion.close()

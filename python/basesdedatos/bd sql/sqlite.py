# -*- coding: utf-8 -*-

'''
Created on 22/02/2012

@author: Alberto
'''

import sqlite3 as dbapi

conexion = dbapi.connect("alumnos.bd")
cursor = conexion.cursor()
cursor.execute("""create table empleados (dni text,
                  nombre text,
                  departamento text)""")
cursor.execute("""insert into empleados
                  values ('12345678-A', 'Manuel Gil', 'Contabilidad')""")
cursor.execute("""select * from empleados""")
for tupla in cursor.fetchall():
    print tupla
misdatos = cursor.fetchall()
for empleado in misdatos:
    print empleado[2].upper(), empleado[1]
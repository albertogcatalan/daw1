# -*- coding: utf-8 -*-

'''
Created on 22/02/2012

@author: Alberto
'''

import sqlite3 as bd

def crea_inserta(conexion):
    datos = open('ciclismo_BD.sql').read()
    cursor = conexion.cursor()
    for sentencia in datos.split(';'):
        cursor.execute(sentencia)
    conexion.commit()
    cursor.close()
    
def consulta(conexion, sql):
    cursor = conexion.cursor()
    cursor.execute(sql)
    cols = len(cursor.description)
    tam = 80 / cols
    encabezado = [d[0] for d in cursor.description]
    for col in encabezado:
        print "%-*s" % (tam, col),
    print
    print '_'*80
    
    for linea in cursor.fetchall():
        print linea
    

if __name__ == '__main__':
    conexion = bd.connect('ciclistas.dat')
    #crea_inserta(conexion)
    sql1 = 'select * from maillot'
    consulta(conexion, sql1)
    conexion.close()
    
# -*- coding: utf-8 -*-

'''
Created on 27/02/2012

@author: Alberto
'''

import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import sqlite3 as bd
import webbrowser
import os.path
import numpy as na
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import pyplot, mpl
import matplotlib.cbook as cbook
import matplotlib.image as image
from matplotlib.collections import PolyCollection
from matplotlib.colors import colorConverter

def crea_inserta(conexion):
    '''Creamos la BD en base a un archivo SQL que 
    contiene una BD de Ciclistas'''
    
    datos = open('ciclismo_BD.sql').read()
    cursor = conexion.cursor()
    for sentencia in datos.split(';'):
        cursor.execute(sentencia)
    conexion.commit()
    cursor.close()
    
def consulta(conexion, sql):
    '''Función para realizar consultas SQL'''
    
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
        
    print
    print '_'*80

def generar_html(conexion, lista):
    '''Generar el HTML informe.html'''
    
    cursor = conexion.cursor()
    # si existe el informe lo eliminamos
    if os.path.exists('informe.html'):
        os.remove('informe.html')
        
    f = open('informe.html', 'w')
    
    f.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
    f.write('<link rel="stylesheet" href="style.css" /><title>Informe</title></head>')
    f.write('<body><h1>Informes de Ciclistas</h1>')
    
    f.write('<a href="#graf1">Gráfico 1</a>')
    f.write('<br/>')
    f.write('<a href="#graf2">Gráfico 2</a>')
    f.write('<br/>')
    f.write('<a href="#graf3">Gráfico 3</a>')
    f.write('<br/>')
    f.write('<a href="#graf4">Gráfico 4</a>')
    f.write('<br/>')
    f.write('<a href="#graf5">Gráfico 5</a>')
    
    # bucle que genera tabla con gráfico para cada consulta
    for p in lista:
        cursor.execute(p)
        f.write('<br/><table>')
        f.write('<tr>')
        for columna in cursor.description:
            f.write('<th>%s</th>' % columna[0].upper())
        f.write('</tr>')
        
        for atributo in cursor.fetchall():
            f.write('<tr>')
            for col in atributo:
                f.write('<td>'+str(col)+'</td>')
            f.write('</tr>')
    
        f.write('</table>')
        
    f.write('<br/><br/>')
    f.write('<a name="graf1"><h2><b>Gráfico 1</b></h2></a>')
    f.write('<img src="1.png"')
    f.write('<br/><br/>')
    f.write('<a name="graf2"><h2><b>Gráfico 2</b></h2></a>')
    f.write('<img src="2.png"')
    f.write('<br/><br/>')
    f.write('<a name="graf3"><h2><b>Gráfico 3</b></h2></a>')
    f.write('<img src="3.png"')
    f.write('<br/><br/>')
    f.write('<a name="graf4"><h2><b>Gráfico 4</b></h2></a>')
    f.write('<img src="4.png"')
    f.write('<br/><br/>')
    f.write('<a name="graf5"><h2><b>Gráfico 5</b></h2></a>')
    f.write('<img src="5.png"')
    f.write('<br/><br/>')
    
    f.write('</body>')
    f.write('</html>')
    
def generar_grafico_1(conexion, sentencia):
    cursor = conexion.cursor()
    cursor.execute(sentencia)
    
    descriptions = []
    for column in cursor.description:
        descriptions.append(column[0].upper())
    
    list1 = []
    for data in cursor.fetchall():
        list1.append(data[3])
        
        
    labels = descriptions
    plt.ylabel('Datos')
    plt.xlabel('Campos')
    pos = na.array(range(4))+0.5
    
    plt.bar(pos ,[10, 4, 6, 8], 0.5)
    plt.xticks(pos+ 0.5/2, labels)
    plt.savefig('1.png')

def generar_grafico_2(conexion, sentencia):
    cursor = conexion.cursor()
    cursor.execute(sentencia)
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    x = na.linspace(0, 1, 100)
    y = na.sin(x * 2 * na.pi) / 2 + 0.5
    ax.plot(x, y, zs=0, zdir='z', label='zs=0, zdir=z')
   
    colors = ('r', 'g', 'b', 'k')
    for c in colors:
        x = na.random.sample(4)
        y = na.random.sample(4)
        ax.scatter(x, y, 0, zdir='y', c=c)
    
    ax.legend("A")
    ax.set_xlim3d(0, 1)
    ax.set_ylim3d(0, 1)
    ax.set_zlim3d(0, 1)
    plt.savefig('2.png')
    
def generar_grafico_3(conexion, sentencia):
    cursor = conexion.cursor()
    cursor.execute(sentencia)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    ax.plot(na.random.rand(len(cursor.fetchall())), '-o', ms=20, lw=2, alpha=0.7, mfc='orange')
    ax.grid()
    
    plt.savefig('3.png')

def generar_grafico_4(conexion, sentencia):
    cursor = conexion.cursor()
    cursor.execute(sentencia)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    ax.plot(na.random.rand(len(cursor.fetchall())), '-o', ms=20, lw=2, alpha=0.7, mfc='yellow')
    ax.grid()
    
    plt.savefig('4.png')
    
def generar_grafico_5(conexion, sentencia):
    cursor = conexion.cursor()
    cursor.execute(sentencia)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    ax.plot(na.random.rand(len(cursor.fetchall())), '-o', ms=20, lw=2, alpha=0.7, mfc='red')
    ax.grid()
    
    plt.savefig('5.png')
        
if __name__ == '__main__':
    '''Inicio del programa'''
    
    # conectacmos a la BD
    conexion = bd.connect('ciclistas.dat')
    
    #crea_inserta(conexion)
    
    # consultas sql
    sql1 = 'select * from maillot'
    sql2 = 'select nombre, edad from ciclista'
    sql3 = 'select * from equipo'
    sql4 = 'select nompuerto, altura, categoria, pendiente from puerto'
    sql5 = 'select * from maillot where premio = 8000000'
    
    lista = [sql1, sql2, sql3, sql4, sql5]
    
    generar_grafico_1(conexion, sql1)
    generar_grafico_2(conexion, sql2)
    generar_grafico_3(conexion, sql3)
    generar_grafico_4(conexion, sql4)
    generar_grafico_5(conexion, sql5)
    
    generar_html(conexion, lista)
    
    webbrowser.open('informe.html')
    # cerramos la conexion a la BD
    conexion.close()
    
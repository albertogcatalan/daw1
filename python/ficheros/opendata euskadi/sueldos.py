# -*- coding: utf-8 -*-
'''
Created on 02/12/2011

@author: Alberto
'''

import csv
import codecs
from pygooglechart import GroupedVerticalBarChart, Axis

salarios2009 = []
salarios2010 = []
salarios2011 = []
nivel = []

archivo = codecs.open('sueldos_2011.csv', 'r', 'iso-8859-1')
archivo.readline()
lector = csv.DictReader(archivo, delimiter=";", quoting=csv.QUOTE_NONE) #diccionario

def porcentaje(num1, num2):#funcion para hacer la media
    media = ((float(num2) * 100) / float(num1)) - 100
    return int(media)

    
for fila in lector:#bucle de filtrado
    filtrado1 = ''
    filtrado = ''
    
    if fila['Nivel'] != '':
        nivel.append(fila['Nivel'])
    
    if fila['Año 2009 - Anual'] != '':
        filtrado1 = fila['Año 2009 - Anual'].replace('.', '')
        filtrado = filtrado1.replace(',', '.')
        salarios2009.append(filtrado)
        
    if fila['Año 2010 - Anual'] != '':
        filtrado1 = fila['Año 2010 - Anual'].replace('.', '')
        filtrado = filtrado1.replace(',', '.')
        salarios2010.append(filtrado)
        
    if fila['Año 2011 - Anual'] != '':
        filtrado1 = fila['Año 2011 - Anual'].replace('.', '')
        filtrado = filtrado1.replace(',', '.')
        salarios2011.append(filtrado)
    
fw = open('anuales.csv', 'w')
csvwriter = csv.writer(fw, delimiter=' ')
csvwriter.writerow(('Nivel;Salarios2009;Salarios2010;Salarios2011;Porcentaje2010;Porcentaje2011'))

chart = GroupedVerticalBarChart(600, 400, y_range=[0, 100])#iniciamos grafico
chart.set_bar_width(3)
chart.set_colours(['E01B4C', '421BE0', '1BE01B'])
chart.set_axis_labels(Axis.LEFT, ['0%', '50%', '100%'])

i = 0
for x in salarios2009:#generamos csv y chart
    csvwriter.writerow([nivel[i], ';'+salarios2009[i]+';', salarios2010[i]+';', salarios2011[i]+';', str(porcentaje(salarios2009[i], salarios2010[i]))+'%'+';', str(porcentaje(salarios2009[i], salarios2011[i]))+'%'])
    chart.add_data([100])
    chart.add_data([abs(porcentaje(salarios2009[i], salarios2010[i]))])
    chart.add_data([abs(porcentaje(salarios2009[i], salarios2011[i]))])
    i += 1

fw.close()
chart.download('sueldos_euskadi.png')

    
    
    
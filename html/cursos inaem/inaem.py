# -*- coding: utf-8 -*-

'''
Created on 01/12/2011

@author: Alberto
'''

from BeautifulSoup import BeautifulSoup
import urllib2

url = 'http://plan.aragon.es/MapaRec.nsf/fmrListado'  # Listado cursos formación empleo ...
doc = BeautifulSoup(urllib2.urlopen(url))
# mostrar documento indentado
print doc.prettify()  
 
# Analizamos el doc. Los cursos están almacenados:
#    * en tablas (elemento td)
#    * que tienen clase "textoApl1"
 
cursos = doc.findAll('td', attrs={'class': "textoApl1"})
for curso in cursos:
    # Imprimimos nombre y url del curso:
    print curso.a.string, curso.a.get('href')

# -*- coding: utf-8 -*-
'''
Created on 26/01/2012

@author: Alberto

'''

import amara
from amara.lib import U

doc = amara.parse('xpath.xml') #ruta del archivo

# expresiones xpath
xpath1 = u'/ies/nombre'
xpath2 = u'/ies/web'
xpath3 = u'/ies/ciclos/ciclo/nombre'
xpath4 = u'/ies/ciclos/ciclo/@id'
xpath5 = u'/ies/ciclos/ciclo/decretoTitulo/@año'
xpath6 = u'/ies/ciclos/ciclo/*'
xpath7 = u'/ies/ciclos/ciclo[grado="Superior"]/nombre'
xpath8 = u'/ies/ciclos/ciclo[decretoTitulo[@año<2010]]/nombre'
xpath9 = u'/ies/ciclos/ciclo[decretoTitulo[@año=2008]]/nombre|/ies/ciclos/ciclo[decretoTitulo[@año=2010]]/nombre'

'''
Nombre del Instituto (IES Abastos)
'''
resultado1 = doc.xml_select(xpath1)

for nombre in resultado1:
    nombre.xml_write()
    print '\n'+U(nombre)
    
print '---------------------------'

''' 
Página web del Instituto (http://www.iesabastos.org)
'''
resultado2 = doc.xml_select(xpath2)

for web in resultado2:
    web.xml_write()
    print '\n'+U(web)

print '---------------------------'

'''
Nombre de los Ciclos Formativos (Administración de Sistemas Informáticos en Red,
Desarrollo de Aplicaciones Web, Sistemas Microinformáticos y Redes)
'''
resultado3 = doc.xml_select(xpath3)

for nombre_ciclo in resultado3:
    nombre_ciclo.xml_write()
    print '\n'+U(nombre_ciclo)
    
print '---------------------------'

'''
Siglas por las que se conocen los Ciclos Formativos (ASIR, DAW, SMR)
'''
resultado4 = doc.xml_select(xpath4)

for curso in resultado4:
    print U(curso)
    
print '---------------------------'

'''
Años en los que se publicaron los decretos de título de los Ciclos Formativos (2009, 2010, 2008).
'''
resultado5 = doc.xml_select(xpath5)

for decretos in resultado5:
    print U(decretos)
    
print '---------------------------'

'''
Ciclos Formativos de Grado Medio (<ciclo id="SMR"> <nombre>Sistemas Microinformáticos y 
Redes</nombre> <grado>Medio</grado> <decretoTitulo año="2008" /> </ciclo>).
 Se trata de obtener el elemento <ciclo> completo)
'''
resultado6 = doc.xml_select(xpath6)

for curso in resultado6:
    curso.xml_write()
    print U(curso)
    
print '---------------------------'

'''
Nombre de los Ciclos Formativos de Grado Superior
(Administración de Sistemas Informáticos en Red, Desarrollo de Aplicaciones Web)
'''
resultado7 = doc.xml_select(xpath7)

for curso in resultado7:
    print U(curso)
    
print '---------------------------'

'''
Nombre de los Ciclos Formativos anteriores a 2010 
(Administración de Sistemas Informáticos en Red, Sistemas Microinformáticos y Redes)
'''
resultado8 = doc.xml_select(xpath8)

for nombre_curso_ano in resultado8:
    print U(nombre_curso_ano)
    
print '---------------------------'

'''
Nombre de los Ciclos Formativos de 2008 o 2010 
(Desarrollo de Aplicaciones Web, Sistemas Microinformáticos y Redes)
'''
resultado9 = doc.xml_select(xpath9)

for nombre_curso_ano in resultado9:
    print U(nombre_curso_ano)

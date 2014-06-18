# -*- coding: utf-8 -*-
'''
Created on 01/01/2012

@author: Alberto

'''

import amara
from amara.lib import U

doc = amara.parse('movies.xml') #ruta del archivo

# expresiones xpath
xpath1 = u'/movies/movie[@type="comedy"]/title'     
xpath2 = u'/movies/movie[actor="Nicolas Cage"]/actor'                           
xpath3 = u'/movies/movie[actor="Nicolas Cage"]/actor[.!=("Nicolas Cage")]'      
xpath4 = u'/movies/movie[@year=1992]/producer'
xpath5 = u'/movies/movie[count(actor)>=3]/title'
xpath6 = u'/movies/movie[contains(producer,"Wood")]/title'
xpath7 = u'/movies/movie[contains(producer,substring-after(actor," "))]/title'

'''
Título de las Comedias
'''
resultado1 = doc.xml_select(xpath1)

for titulo in resultado1:
    print U(titulo)
    
print '---------------------------'

''' 
Actores que trabajaron con Nicolas Cage en alguna película.
'''
resultado2 = doc.xml_select(xpath2)

for actores in resultado2:
    print U(actores)

print '---------------------------'

'''
Actores que trabajaron con Nicolas Cage en alguna película, sin que salga su nombre en el resultado
'''
resultado3 = doc.xml_select(xpath3)

for actores in resultado3:
    print U(actores)
    
print '---------------------------'

'''
Productores de alguna película en 1992
'''
resultado4 = doc.xml_select(xpath4)

for productores in resultado4:
    print U(productores)
    
print '---------------------------'

'''
Título de las películas que tuvieron al menos tres actores
'''
resultado5 = doc.xml_select(xpath5)

for titulo in resultado5:
    print U(titulo)
    
print '---------------------------'

'''
Título de las películas cuyo productor se apellida Wood.
'''
resultado6 = doc.xml_select(xpath6)

for titulo in resultado6:
    print U(titulo)
    
print '---------------------------'

'''
Titulo de las películas cuyo productor se apellida como al menos uno de los actores.
'''
resultado7 = doc.xml_select(xpath7)

for titulo in resultado7:
    print U(titulo)
    
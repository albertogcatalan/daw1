# -*- coding: utf-8 -*-
'''
Created on 26/01/2012

@author: Alberto

'''

import amara
from amara.lib import U

doc = amara.parse('xpath2.xml') #ruta del archivo

# expresiones xpath
xpath1 = u'/ies/modulos/modulo/nombre'                               
xpath2 = u'/ies/modulos/modulo[ciclo = "ASIR"]/nombre'                 
xpath3 = u'/ies/modulos/modulo[curso = 2]/nombre'                     
xpath4 = u'/ies/modulos/modulo[horasSemanales < 5]/nombre'             
xpath5 = u'/ies/modulos/modulo[curso = 1][ciclo = "ASIR"]/nombre'
xpath6 = u'/ies/modulos/modulo[horasSemanales > 3]/horasSemanales'     

'''
Nombre de los módulos que se imparten en el Instituto (Aplicaciones web,
Gestión de bases de datos, Lenguajes de marcas y sistemas de gestión de información, 
Implantación de aplicaciones web)
'''
resultado1 = doc.xml_select(xpath1)

for nombre in resultado1:
    print U(nombre)
    
print '---------------------------'

''' 
Nombre de los módulos del ciclo ASIR (Gestión de bases de datos, Lenguajes de marcas y
sistemas de gestión de información, Implantación de aplicaciones web).
'''
resultado2 = doc.xml_select(xpath2)

for asir in resultado2:
    print U(asir)

print '---------------------------'

'''
Nombre de los módulos que se imparten en el segundo curso de cualquier ciclo
(Aplicaciones web, Implantación de aplicaciones web).
'''
resultado3 = doc.xml_select(xpath3)

for segundo in resultado3:
    print U(segundo)
    
print '---------------------------'

'''
Nombre de los módulos de menos de 5 horas semanales
(Aplicaciones web, Lenguajes de marcas y sistemas de gestión de información).
'''
resultado4 = doc.xml_select(xpath4)

for mod_horas in resultado4:
    print U(mod_horas)
    
print '---------------------------'

'''
Nombre de los módulos que se imparten en el primer curso de ASIR
(Gestión de bases de datos, Lenguajes de marcas y sistemas de gestión de información).
'''
resultado5 = doc.xml_select(xpath5)

for asir1 in resultado5:
    print U(asir1)
    
print '---------------------------'

'''
Horas semanales de los módulos de más de 3 horas semanales (4, 5, 5).
'''
resultado6 = doc.xml_select(xpath6)

for horas in resultado6:
    print U(horas)
    
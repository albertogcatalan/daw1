# -*- coding: utf-8 -*-
'''
Created on 26/01/2012

@author: Alberto

'''

import amara
from amara.lib import U

doc = amara.parse('xpath3.xml') #ruta del archivo

# expresiones xpath
xpath1 = u'/ies/modulos/modulo[ciclo=/ies/ciclos/ciclo[nombre="Sistemas Microinformáticos y Redes"]/@id]/nombre'
xpath2 = u'/ies/ciclos/ciclo[@id=/ies/modulos/modulo[nombre="Lenguajes de marcas y sistemas de gestión de información"]/ciclo]/nombre'
xpath3 = u'/ies/modulos/modulo[ciclo=/ies/ciclos/ciclo[grado = "Superior"]/@id]/nombre'
xpath4 = u'/ies/modulos/modulo[ciclo=/ies/ciclos/ciclo[decretoTitulo/@año = 2008]/@id]/nombre'
xpath5 = u'/ies/ciclos/ciclo[@id=/ies/modulos/modulo[curso=1]/ciclo]/grado'

'''
Nombre de los módulos del ciclo "Sistemas Microinformáticos y Redes" (Aplicaciones web)
'''
resultado1 = doc.xml_select(xpath1)

for nombre in resultado1:
    print U(nombre)
    
print '---------------------------'

''' 
Nombre de los ciclos que incluyen el módulo "Lenguajes de marcas y sistemas de gestión de información"
(Administración de Sistemas Informáticos en Red, Desarrollo de Aplicaciones Web).
'''
resultado2 = doc.xml_select(xpath2)

for modulo in resultado2:
    print U(modulo)

print '---------------------------'

'''
Nombre de los módulos de ciclos de Grado Superior (Gestión de bases de datos,
Lenguajes de marcas y sistemas de gestión de información, Implantación de aplicaciones web).
'''
resultado3 = doc.xml_select(xpath3)

for nombre_modulos in resultado3:
    print U(nombre_modulos)
    
print '---------------------------'

'''
Nombre de los módulos de ciclos cuyo título se aprobó en 2008 (Aplicaciones web).
'''
resultado4 = doc.xml_select(xpath4)

for nombre2008 in resultado4:
    print U(nombre2008)
    
print '---------------------------'

'''
Grado de los ciclos con módulos de primer curso (Superior, Superior, Superior).
'''
resultado5 = doc.xml_select(xpath5)

for grado in resultado5:
    print U(grado)

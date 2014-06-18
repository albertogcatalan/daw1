# -*- coding: utf-8 -*-
 
mi_nombre = 'Zed A. Shaw'
mi_edad = 45  # ¿es cierto?
mi_altura = 180  # cms.
mi_peso = 80  # kgs
mis_ojos = 'Azules'
mis_dientes = 'Blancos'
mi_pelo = 'Negro'
mi_coche = 'FE150'
mi_pc = 'Intel i7'

print "Vamos a hablar de %s." % mi_nombre
print "%s mide %d cms." % (mi_nombre, mi_altura)
print "%s pesa %d kgs." % (mi_nombre, mi_peso)
print "Ciertamente no pesa demasiado :) "
print "%s tiene los ojos %s y el pelo %s " % (mi_nombre, mis_ojos, mi_pelo)
print "Sus dientes son %s según el café que ha tomado" % mis_dientes

# Piensa lo que hace esta línea
print "Si sumamos %d, %d, y %d obtenemos %d." % (
    mi_edad, mi_altura, mi_peso, mi_edad + mi_altura + mi_peso)
print "Tengo un coche %s y un PC %s." % (mi_coche, mi_pc)

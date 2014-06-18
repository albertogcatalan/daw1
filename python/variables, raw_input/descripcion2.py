# -*- coding: utf-8 -*-
 
#mi_nombre = 'Zed A. Shaw'
#mi_edad = 45  # ¿es cierto?
#mi_altura = 180  # cms.
#mi_peso = 80  # kgs
#mis_ojos = 'Azules'
#mis_dientes = 'Blancos'
#mi_pelo = 'Negro'
#mi_coche = 'FE150'
#mi_pc = 'Intel i7'


mi_nombre = raw_input('Tu nombre: ')
mi_edad = int(raw_input('Tu edad: '))
mi_altura = int(raw_input('Tu altura: '))
mi_peso = int(raw_input('Tu peso: '))
mis_ojos = raw_input('Tus ojos: ')
mis_dientes = raw_input('Tus dientes: ')
mi_pelo = raw_input('Tu pelo: ')
mi_coche = raw_input('Tu coche: ')
mi_pc = raw_input('Tu pc: ')

print "-" * 20
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

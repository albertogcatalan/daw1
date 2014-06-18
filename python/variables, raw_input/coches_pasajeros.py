# -*- coding: utf-8 -*-
# No declaramos variables, ponemos nombres a objetos

coches = 100
capacidad_coche = 4.0
conductores = 30
pasajeros = 90
coches_no_conducidos = coches - conductores
coches_conducidos = conductores
capacidad_real = coches_conducidos * capacidad_coche
media_pasajeros_coche = pasajeros / coches_conducidos
 
print "Hay", coches, "coches disponibles."
print "Tenemos sólo ", conductores, "conductores disponibles."
print "Habrá", coches_no_conducidos, "coches vacíos hoy."
print "Podemos transportar", capacidad_real, "personas hoy."
print "Tenemos", pasajeros, "pasajeros para transportar."
print "Tenemos que poner una media de", media_pasajeros_coche, "por coche hoy."



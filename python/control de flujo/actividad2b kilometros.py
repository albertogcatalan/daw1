# -*- coding: utf-8 -*-

from easygui import *

tamano = float(enterbox('Tamaño del deposito en litros: '))
porcentaje = float(enterbox('Porcentaje lleno: '))
consumo = float(enterbox('Consumo a los 100km: '))
consumo_real = float(consumo / 100)

litros = (tamano * porcentaje) / 100
disponible = consumo_real * 30
if  litros <= disponible:
    msgbox('Tienes que repostar')
else:
    msgbox('Vas bien de combustible')




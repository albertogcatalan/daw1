# -*- coding: utf-8 -*-
from easygui import *
passwd = 0
clavereal = '626rr1472'
i = 0

while passwd == 0:
    clave = enterbox('Introduce la contraseña: ')
    if clave == clavereal:
        passwd = 1
        msgbox('Contraseña correcta.')
    else:
        i += 1
        if i == 5:
            passwd = 1
            msgbox('Contraseña incorrecta.')


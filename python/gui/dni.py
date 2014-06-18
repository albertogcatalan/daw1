'''
Calcular DNI/NIF
'''

import easygui
Cadena = easygui.enterbox('Escribe tu DNI/NIE: ', 'Calcular NIF')

if Cadena[0] == 'X':
    DNI = Cadena[1:8]
elif Cadena[0] == 'Y':
    DNI = '1'+Cadena[1:8]
elif Cadena[0] == 'Z':
    DNI = '2'+Cadena[1:8]

DNI = int(DNI)
NIF ='TRWAGMYFPDXBNJZSQVHLCKE'
easygui.msgbox("El NIF de tu DNI es "+ NIF[DNI%23], 'Calcular NIF')



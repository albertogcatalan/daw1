
from easygui import *

numero = int(enterbox('Introduce un numero'))

if numero == 2:
    msgbox('Es primo')
else:
    for x in range(2, numero):
        if numero % x == 0:
           msgbox('No es primo')
           break
        else:
           msgbox('Es primo')
           break
    



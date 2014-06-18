from easygui import *

numero = int(enterbox('Introduce un numero'))
i = 1

while i <= 10:
    print numero * i
    i += 1

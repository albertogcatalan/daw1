x1 = int(raw_input('Introduce un numero: '))
x2 = int(raw_input('Introduce un numero: '))
x3 = int(raw_input('Introduce un numero: '))

#estrategia 1
'''if x1 >= x2 and x1 >= x3:
    mayor = x1
elif x2 >= x1 and x2 >= x3:
    mayor = x2
elif x3 >= x1 and x3 >= x2:
    mayor = x3'''

#estrategia 2
'''if x1 >= x2:
    if x1 >= x3:
        mayor = x1
    else:
        mayor = x3
else:
    if x2 >= x3:
        mayor = x2
    else:
        mayor = x3'''

#estrategia 3
'''mayor = x1
if x2 > mayor:
    mayor = x2
if x3 > mayor:
    mayor = x3'''

#estrategia 4
mayor = max(x1, x2, x3)

print 'Este es el numero mayor:', mayor

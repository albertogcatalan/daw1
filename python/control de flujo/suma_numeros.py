'''
Escribe un programa que calcula la suma de
los números de 1 a 20 (incluyendo ambos números)
'''



# etiqueta resultado inicializada a 0
resultado = 0


numero = int(raw_input('Introduce el primer numero: '))

numero2 = int(raw_input('Introduce el segundo numero: '))

# for ...range para recorrer del 1 al 21
# incrementando resultado en cada iteración
for num in range(numero, numero2):
    resultado += num
    # resultado = resultado + num == sería lo mismo
    # print ' >   res:', resultado

    # para hacer directamente: sum(range(1,21)):
    
# mostrar resultado
print 'La suma es: ', resultado



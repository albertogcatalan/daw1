frase = raw_input('Introduce frase a convertir: ')
secreto = ''
for letra in frase:
    ascii = int(ord(letra) + 2)
    secreto += chr(ascii)
    
print secreto

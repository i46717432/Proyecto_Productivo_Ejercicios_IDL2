"""Realizar un algoritmo que permita pedir 10 números y determine e 
imprima cuantos son pares, impares, positivos, neutros y negativos."""

# Creamos contadores que comienzan en cero.
pares = 0
impares = 0
positivos = 0
neutros = 0
negativos = 0

# Repetimos el ingreso de datos diez veces.
for i in range(10):

    # Pedimos un número entero.
    numero = int(input(f"Ingrese el número {i + 1}: "))

    # Comprobamos si es par o impar.
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Comprobamos si es positivo, negativo o cero.
    if numero > 0:
        positivos += 1

    elif numero < 0:
        negativos += 1

    else:
        neutros += 1

# Mostramos las cantidades encontradas.
print("Números pares:", pares)
print("Números impares:", impares)
print("Números positivos:", positivos)
print("Números negativos:", negativos)
print("Números neutros:", neutros)
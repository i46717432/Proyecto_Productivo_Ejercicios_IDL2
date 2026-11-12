""" Hacer un programa que permita ingresar un conjunto de N números y un 
numero más X mostrar como resultado: 
• Porcentaje de números menores que X. 
• Porcentaje de números mayores de X. 
• Porcentaje de números iguales de X. 
• Porcentaje de números comprendidos entre 1 y X. 
• Porcentaje de números que no cumple ninguna condición."""
# Pedimos la cantidad de números.
n = int(input("¿Cuántos números ingresará?: "))

if n > 0:

    # Pedimos el número que servirá de referencia.
    x = float(input("Ingrese el valor de X: "))

    # Creamos una lista vacía para guardar los números.
    numeros = []

    # Repetimos el ingreso N veces.
    for i in range(n):
        numero = float(input(f"Ingrese el número {i + 1}: "))
        numeros.append(numero)

    # Creamos contadores para cada condición.
    menores = 0
    mayores = 0
    iguales = 0
    entre_1_y_x = 0
    ninguna = 0

    # Revisamos los números guardados.
    for numero in numeros:

        if numero < x:
            menores += 1

        if numero > x:
            mayores += 1

        if numero == x:
            iguales += 1

        # Comprobamos si está entre 1 y X,
        # incluyendo ambos extremos.
        if 1 <= numero <= x:
            entre_1_y_x += 1

        # Comprobamos si no cumple ninguna condición.
        if not (
            numero < x or
            numero > x or
            numero == x or
            1 <= numero <= x
        ):
            ninguna += 1

    # Convertimos cada cantidad en porcentaje.
    porcentaje_menores = menores * 100 / n
    porcentaje_mayores = mayores * 100 / n
    porcentaje_iguales = iguales * 100 / n
    porcentaje_rango = entre_1_y_x * 100 / n
    porcentaje_ninguna = ninguna * 100 / n

    # Mostramos los resultados.
    print("Menores que X:", porcentaje_menores, "%")
    print("Mayores que X:", porcentaje_mayores, "%")
    print("Iguales a X:", porcentaje_iguales, "%")
    print("Entre 1 y X:", porcentaje_rango, "%")
    print("Ninguna condición:", porcentaje_ninguna, "%")

else:
    print("Error: debe ingresar al menos un número.")
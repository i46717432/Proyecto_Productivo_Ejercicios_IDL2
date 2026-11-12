"""Calcular la suma y promedio de los números pares e impares por 
separado ,de 1 hasta N. """

# Pedimos hasta qué número queremos contar.
n = int(input("Ingrese un número N: "))

# Creamos variables para guardar las sumas.
suma_pares = 0
suma_impares = 0

# Creamos contadores para saber cuántos hay.
cantidad_pares = 0
cantidad_impares = 0

# Comprobamos que N sea mayor que cero.
if n > 0:

    # Recorremos los números desde 1 hasta N.
    for numero in range(1, n + 1):

        # Si el residuo de dividir entre 2 es cero,
        # significa que el número es par.
        if numero % 2 == 0:
            suma_pares += numero
            cantidad_pares += 1

        # De lo contrario, el número es impar.
        else:
            suma_impares += numero
            cantidad_impares += 1

    # Calculamos los promedios.
    # Evitamos dividir entre cero.
    promedio_pares = (
        suma_pares / cantidad_pares
        if cantidad_pares > 0 else 0
    )

    promedio_impares = (
        suma_impares / cantidad_impares
        if cantidad_impares > 0 else 0
    )

    # Mostramos los resultados.
    print("Suma de pares:", suma_pares)
    print("Promedio de pares:", promedio_pares)
    print("Suma de impares:", suma_impares)
    print("Promedio de impares:", promedio_impares)

else:
    print("Error: N debe ser mayor que cero.")

    # CONCLUSION
    """Para principiantes: for sirve para repetir instrucciones, % obtiene el residuo de una división y += permite acumular cantidades."""
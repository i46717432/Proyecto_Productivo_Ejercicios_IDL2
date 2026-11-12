""" Calcular el producto utilizando arrays: 100 x 98 x 96 x 94 x . . . x 1 en 
este orden."""

"""Objetivo: Calcular el producto de la secuencia 100 × 98 × 96 × 94 × ..., utilizando un arreglo o lista.

El enunciado termina en 1, aunque al comenzar en 100 y disminuir de dos en dos se llega a 2. Para conservar el patrón, multiplicaremos los números pares desde 100 hasta 2."""

# Creamos una lista vacía para guardar los números.
numeros = []

# Recorremos los números pares desde 100 hasta 2.
# El -2 indica que disminuimos de dos en dos.
for numero in range(100, 0, -2):

    # Guardamos cada número en la lista.
    numeros.append(numero)

# Creamos una variable para guardar el producto.
producto = 1

# Recorremos todos los números guardados.
for numero in numeros:

    # Multiplicamos cada número por el producto acumulado.
    producto = producto * numero

# Mostramos la lista utilizada.
print("Números del arreglo:")
print(numeros)

# Mostramos la cantidad de números.
print("Cantidad de elementos:", len(numeros))

# Mostramos el producto final.
print("Producto total:", producto)

"""Ejemplo más pequeño: Para comprenderlo, imaginemos la secuencia 10 × 8 × 6 × 4 × 2.
Paso	Número	Producto acumulado
1	10	10
2	8	80
3	6	480
4	4	1,920
5	2	3,840"""

"""En el ejercicio original se multiplican 50 números pares, por lo que el resultado es mucho mayor.

Para principiantes: Una lista permite guardar varios valores en una sola variable. append() agrega elementos y el ciclo for permite recorrerlos para realizar operaciones."""
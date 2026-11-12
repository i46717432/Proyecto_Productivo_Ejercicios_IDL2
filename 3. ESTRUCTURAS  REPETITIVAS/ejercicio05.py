"""Realizar un algoritmo para determinar cuánto ahorrará una persona en 
un año, si al final de cada mes deposita cantidades variables de dinero; 
se quiere saber cuánto lleva ahorrado cada vez que haga un deposito 
en cada mes y luego mostrar el ahorro final de 12 meses. """

# Creamos una variable para acumular los ahorros.
ahorro_total = 0

# Creamos una lista para guardar los depósitos.
depositos = []

# Repetimos el proceso durante 12 meses.
for mes in range(1, 13):

    # Pedimos cuánto dinero se ahorró ese mes.
    deposito = float(input(f"Depósito del mes {mes}: S/ "))

    # No permitimos depósitos negativos.
    while deposito < 0:
        print("El depósito no puede ser negativo.")
        deposito = float(input("Ingrese otro importe: S/ "))

    # Guardamos el depósito en la lista.
    depositos.append(deposito)

    # Sumamos el nuevo depósito al ahorro acumulado.
    ahorro_total += deposito

    # Mostramos cuánto lleva ahorrado.
    print(f"Ahorro acumulado en el mes {mes}: S/ {ahorro_total:.2f}")

# Mostramos el ahorro final del año.
print("AHORRO TOTAL DEL AÑO: S/", round(ahorro_total, 2))

"""Ejemplo: Si una persona deposita S/ 100 todos los meses, al finalizar el año habrá ahorrado S/ 1,200.

Para principiantes: while repite una instrucción mientras se cumpla una condición. append() agrega un elemento a una lista y += suma una cantidad al total acumulado."""
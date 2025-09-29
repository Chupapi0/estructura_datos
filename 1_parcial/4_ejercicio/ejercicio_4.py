rows = int(input("Introduzca el numero de filas: "))
cols = int(input("Introduzca el numero de de columnas: "))
matriz = []
ven = 0
for X in range(rows):
    fila = []
    for Y in range(cols):
        valor = int(input(f"Ingresa el valor para posición [{X}][{Y}]: "))
        fila.append(valor)
        op = valor + ven
        ven = op
    matriz.append(fila)

print(matriz)
print(op)

input("Presione enter para salir.....")

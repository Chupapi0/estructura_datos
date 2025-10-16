# Implementación de una pila
pila = []
cola = []

nombre = input("Introduzca un nombre: ")
# Agregar elementos (push)
for i in nombre:
    pila.append(i)
    cola.append(i)

print(pila)
print(cola)

# Eliminar elementos (pop)
ultimo = pila.pop()
primero = cola.pop(0)
print("\n---PILAS---")
print("Elemento eliminado:", ultimo)
print("Pila después de eliminar un elemento:", pila)

print("\n---COLAS---")
print("Elemento eliminado:", primero)
print("Pila después de eliminar un elemento:", cola)

input("Presione enter para salir.....")
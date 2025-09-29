"""
Diseñe un programa en python que realize lo siguiente 
1. declare y cree un arreglo con edad de un grupo de personas  +
2. calcule e imprima la edad minimna y maxima de ese grupo de personas con el nombre de estas. El promedio de las edades y la mediana del grupo
3. permita al usuario agregar una nueva edad al erreglo y mostrar nuevamente los datos actualizados
"""
import statistics

pe = int(input("Ingrese el numero de personas en su grupo: "))
print(pe)

personas = []
edad = []

for X in range(pe):
    nombres = input(f"Ingresa el nombre de la persona numero [{X + 1}]: ")
    personas.append(nombres)
    valor = int(input(f"Ingresa la edad de {nombres}: "))
    edad.append(valor)

print("Arreglo de personas:", personas)
print("Arreglo de edades:", edad)

edad_min = min(edad)
edad_max = max(edad)
promedio = sum(edad) / len(edad)
mediana = statistics.median(edad)
min_index = edad.index(edad_min)
max_index = edad.index(edad_max)
print(f"\nLa edad minima es {edad_min} de {personas[min_index]}")
print(f"La edad maxima es {edad_max} de {personas[max_index]}")
print(f"El promedio de las edades es: {promedio:.2f}")
print(f"La mediana de las edades es: {mediana}")

num = int(input("Quieres introducir a otra persona (0 = NO, 1 = YES): "))
if num == 0:
   print("Gracias por usar el programa")
else:
    np = int(input("¿Cuantas nuevas personas vas a introducir?"))
    X = len(edad)
    for X in range(np):
        nombres = input(f"Ingresa el nombre de la nueva persona numero [{X + 1}]: ")
        personas = personas + [nombres]
        valor = int(input(f"Ingresa la edad de {nombres}: "))
        edad = edad + [valor]

    print("Arreglo de personas:", personas)
    print("Arreglo de edades:", edad)

    edad_min = min(edad)
    edad_max = max(edad)
    promedio = sum(edad) / len(edad)
    mediana = statistics.median(edad)
    min_index = edad.index(edad_min)
    max_index = edad.index(edad_max)
    print(f"\nLa edad minima es {edad_min} de {personas[min_index]}")
    print(f"La edad maxima es {edad_max} de {personas[max_index]}")
    print(f"El promedio de las edades es: {promedio:.2f}")
    print(f"La mediana de las edades es: {mediana}")

input("Presione enter para salir.....")

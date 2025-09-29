"""
Busqueda de elementos de un arreglo
Desarrolle un programa en python que:
    1. permita declarar y crear un arreglo con calificaciones de un grupo de estudiantes (valores enteros del 0 al 100) +
    2. Calcule el promedio de las calificaciones de cada alumno y de las calificaciones almacenadas en el arreglo +
    3. que permita buscar si una calificaciones especifica (ingresada por el usuario) se encuentra en el arreglo 
    4. que muestre los resultados de forma clara en la pantalla +
"""

#Este sera el largo del arreglo
et = int(input("Ingrese el numero de estudiantes que va a calificar: "))
print(et)
#Este sera el ancho de nuestro arreglo
mt = int(input("Ingrese el numero de materias que usted va a calificar: "))
print(mt)

matriz_n=[]
matriz_c=[]
ven = 0

#Mete los nombres de los estudiantes
for X in range(et):
    nombres = input(f"Ingresa el nombre del estudiente numero [{X + 1}]: ")
    matriz_n.append(nombres)

#Ingrsa la calificacion por materia y estudiante
for X in range(et):
    fila_c=[]
    for Y in range(mt):
        valor = int(input(f"Ingresa la calificacion de {matriz_n[X]} en la materia numero {Y + 1} (del 0 al 100) : "))
        fila_c.append(valor)
    matriz_c.append(fila_c)

print("\n===== CALIFICACIONES Y PROMEDIOS =====\n")

#Imprime el promedio por estudiante y la calificacion por materia
for i in range(et):
    nombre = matriz_n[i]
    calificaciones = matriz_c[i]
    promedio = (sum(calificaciones) *10) / (len(calificaciones)*100)
    promedio_g = (promedio + ven)
    ven = promedio
    print(f"{nombre}: Calificaciones = {calificaciones} | Promedio = {promedio:.2f}")

#Genera el promedio del grupo
promedio_gf = promedio_g / len(matriz_n)
print(f"El promedio general del grupo es de: {promedio_gf}")

#Ingresa la calificacion que desea buscar
valor = int(input("\nIngrese la calificación que desea saber: "))
encontrado = False

#Buca la calificacion en el arreglo 
for i in range(len(matriz_c)):
    for j in range(len(matriz_c[i])):
        if matriz_c[i][j] == valor:
            print(f"El valor {valor} está en el estudiante '{matriz_n[i]}' en la materia número {j + 1}.")
            encontrado = True

#imprime el alumno y donde tuvo esa calificacion
if not encontrado:
    print(f"El valor {valor} no está en la lista.")

input("Presione enter para salir.....")

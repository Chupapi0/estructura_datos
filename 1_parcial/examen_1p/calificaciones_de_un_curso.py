"""
Implemente en python un programa que realize lo siguiente:
1. Cree un arreglo con las calificaciones de 10 estudiantes considerando valores enteros entre 0 y 10. ✓
2. Al inicio se preguntara cuantas materias hay en el curso                                            ✓
3. Muestre en pantalla todos los alumnos y todas sus calificaciones                                    ✓
4. Calcule y mustre el promedio de las calificaciones por alumno y grupal                              ✓
    A) Promedio de las calificaciones por alumno                                                       ✓
    B) Promedio de calificaciones por materia                                                          ✓
    C) Promedio grupal                                                                                 ✓
5. Muestre en pantalla el alumno con la calificacion minina y la calificaciones maxima                 ✓
6. El numero de alumnos que aprobaron mayor a 7 y los que reprobaron menor a 7                         ✓
7. Permita al usuario buscar la calificacion de un alumno en especifica dentro del arreglo e indique si se encuentra o no - ✓
8. Despues de la busqueda ordene el arreglo de mayor a menor y muestre el resultado en pantalla
"""
#Este sera el ancho de nuestro arreglo
mt = int(input("Ingrese el numero de materias que usted va a calificar: "))
print(mt)
#Arreglos de los nombres y las calificaciones
matriz_n=[]
matriz_c=[]
ven = 0
#Variable de los alumnos 
an=10

#Mete los nombres de los estudiantes
for X in range(an):
    nombres = input(f"Ingresa el nombre del estudiente numero [{X + 1}]: ")
    matriz_n.append(nombres)

#Ingrsa la calificacion por materia y estudiante
for X in range(an):
    fila_c=[]
    for Y in range(mt):
        valor = int(input(f"Ingresa la calificacion de {matriz_n[X]} en la materia numero {Y + 1} (0 al 10) : "))
        fila_c.append(valor)
    matriz_c.append(fila_c)

print("\n===== CALIFICACIONES Y PROMEDIOS =====\n")
aa = 0
ar = 0
#Imprime el promedio por estudiante y la calificacion por materia
for i in range(an):
    nombre = matriz_n[i]
    calificaciones = matriz_c[i]
    promedio = (sum(calificaciones) *10) / (len(calificaciones)*10)
    promedio_g = (promedio + ven)
    ven = promedio
    print(f"{nombre}: Calificaciones = {calificaciones} | Promedio = {promedio:.2f}")
    if promedio >= 7:
        aat=aa+1
        aa=aat
    else:
        art=ar+1
        ar=art

#Imprime el promedio por materia
print("\n===== PROMEDIO POR MATERIA =====")
for i in range(mt):
    columna = [fila[i] for fila in matriz_c]
    promedio_materia = (sum(columna) *10) / (len(columna)*10)
    print(f"El promedio de la materia {i + 1} es de: ",promedio_materia)

#Genera el promedio del grupo
print("\n===== PROMEDIO GENERAL =====")
promedio_gf = promedio_g / len(matriz_n)
print(f"El promedio general del grupo es de: {promedio_gf}")

#Imprime la calificacion maxima y minima en cada materia
print("\n===== CALIFICACION MAXIMA Y MINIMA =====")
for i in range(mt):
    columna = [fila[i] for fila in matriz_c]
    calificacion_min = min(columna)
    calificacion_max = max(columna)
    alumno_min = matriz_n[columna.index(calificacion_min)]
    alumno_max = matriz_n[columna.index(calificacion_max)]
    print(f"La materia {i + 1} tiene una nota mínima de {calificacion_min}, obtenida por {alumno_min}")
    print(f"La materia {i + 1} tiene una nota máxima de {calificacion_max}, obtenida por {alumno_max}")

#Imprime el numero de alumnos reprobados y aprobados
print("\n===== NUMERO DE ALUMNOS REPROBADOS Y APROBADOS =====")
print(f"El total de alumnos aprobados fue de = {aa}")
print(f"El total de alumnos reprobados fue de = {ar}")

#Ingresa la calificacion que desea buscar
valor = int(input("\nIngrese la calificación que desea saber: "))
encontrado = False

#Busca la calificacion en el arreglo 
for i in range(len(matriz_c)):
    for j in range(len(matriz_c[i])):
        if matriz_c[i][j] == valor:
            print(f"El valor {valor} está en el estudiante '{matriz_n[i]}' en la materia número {j + 1}.")
            encontrado = True

#imprime el alumno y donde tuvo esa calificacion
if not encontrado:
    print(f"El valor {valor} no está en la lista.")

# Ordena todas las calificaciones de mayor a menor y muestra el resultado
calificaciones_planas = [nota for alumno in matriz_c for nota in alumno]
calificaciones_ordenadas = sorted(calificaciones_planas, reverse=True)

print("\n===== CALIFICACIONES ORDENADAS DE MAYOR A MENOR =====")
print(calificaciones_ordenadas)

input("Presione enter para salir.....")

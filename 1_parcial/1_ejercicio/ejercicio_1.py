# Solicitar un valor al usuario
n = int(input("Introduzca el numero que le realizaremos un factorial: "))

if n > 1:
    factorial = 1
    contador = 1
    f = n
    while contador <= n:
        Op = factorial * f
        factorial = Op
        f = f - 1
        contador = contador + 1
    print("El factorial de", n, "es:", factorial)
elif n == 0 or n == 1:
    print("El valor del factorial de 0 y 1 da como resultado 1")    
else:
    print("No hay factorial de numeros negativos")

input("Presione enter para salir.....")

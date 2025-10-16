"""
Verificar utilizando pilas si una palabra es un parindromo o no lo es
1- Debe de solicitar al usuario la palabra
2- Utilizar la pila para invertir la palabra
3- Comparar palabra original vs invertida
	Si es igual = ES UN PALINDROMO
	Si no es igual = NO ES UN PALINDROMO
""" 
pila = []
palabra_o = input("Ingrese una palabra: ")
#convertimos la cadena a minusculas
palabra = palabra_o.lower()
#Si no introdujo una palabra te saca
if len(palabra) == 0:
    print("No ingresaste ni una palabra")
    exit()
#pasa la cadena de texto a una pila
for X in palabra:
    pila.append(X)
#Invertimos la pila con este comando
pila_inv=pila[::-1]
#pasamos a una cadena de texto la pila ya invertida
palabra_invertida = ''.join(pila_inv)
#Comparamos las dos cadenas
if palabra == palabra_invertida:
    print("ES UN PALÍNDROMO")
else:
    print("NO ES UN PALÍNDROMO")

input("Presione enter para salir.....")

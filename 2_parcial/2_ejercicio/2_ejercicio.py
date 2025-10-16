"""
Cree un programa en python que determine si una expresion tiene los parentesis correctamente balanceados.
Para ello utilice una pila que almacene los parentesis de apertura y los retire cuando encuentre un parentesis de cierre.
Una expresion esta balanceada si :
- Cada parentesis de apertura tiene su correspondiente parentesis de cierre.
- No hay cierrres antes de que alla un parentesis de apertura. 
"""
pila = []
expresion = input("Ingrese una expresion: ")

if len(expresion) == 0:
    print("La expresion esta vacia")
    exit()

for X in expresion:
    if X == "(":
        pila.append(X)

    elif X == ")":
        if len(pila) == 0:
            print("La expresion no esta balanceada")
            exit()
        pila.pop()

if len(pila) == 0:
    print("La expresion esta balanceada")
else:
    print("La expresion no esta balanceada")

input("Presione enter para salir.....")

"""
Cree un programa en python que determine si una expresion tiene los parentesis correctamente balanceados.
Para ello utilice una pila que almacene los parentesis de apertura y los retire cuando encuentre un parentesis de cierre.
Una expresion esta balanceada si :
- Cada parentesis de apertura tiene su correspondiente parentesis de cierre.
- No hay cierrres antes de que alla un parentesis de apertura.
"""

pila = []
expresion = input("Ingrese una expresion con parentesis: ")

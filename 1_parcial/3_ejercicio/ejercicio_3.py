def invertir_cadena(cadena):
    # Caso base: cadena vacía o de un solo carácter
    if len(cadena) <= 1:
        return cadena
    else:
        # Llamada recursiva: invierte el resto y agrega el primer carácter al final
        return invertir_cadena(cadena[1:]) + cadena[0]

# Solicitar entrada al usuario
texto = input("Introduzca una cadena de texto: ")
resultado = invertir_cadena(texto)
print("Cadena invertida:", resultado)

input("Presione enter para salir.....")

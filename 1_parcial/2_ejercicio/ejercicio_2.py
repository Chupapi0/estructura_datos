# Solicitar un valor al usuario
f = int(input("Introduzca hasta que numero de la cadena de fibonacci desea obvervar: "))
fi = 0
ff = 1
cont = 1

if f > 1:
    print("... SERIE DE FIBONACCI ...")
    print("           ",fi)
    print("           ",ff)
    while cont < (f-1):
        fn = fi + ff 
        print(fi," + ",ff," = ", fn)
        fi = ff
        ff = fn
        cont+= 1
elif f == 1:
    print("           ",fi) 
elif f == 0:
    print("No puedo mostrarle nada")    
else:
    print("ERROR con los numeros negativos")

# Mostrar el valor ingresado
lista = []
while True:
    try:
        numero = int(input("Ingrese un numero para añadir a la lista (-1 para salir): "))
        if numero == -1:
            break
        else:
            lista.append(numero)

    except ValueError:
        print("Error, solo se pueden añadir numeros enteros a la lista.")


fallos = 0
while True:
    if fallos == 3:
        break
    try:
        numero = int(input("Ingrese un numero para buscar en la lista: "))
        print(f"Posicion de la primera aparicion: {lista.index(numero)+1}")

    except ValueError:
        fallos += 1
        print(f"Error, valor incorrecto (errores restantes {3 - fallos})\n")

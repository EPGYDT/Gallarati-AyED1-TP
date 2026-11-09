numero = 1
while True:
    try:
        for i in range(numero, 100_001):
            numero += 1
            print(i)

        print("\nTermino!")
        break
    except KeyboardInterrupt:
        confirmacion = input("Desea detener el programa (si | no): ")
        if confirmacion.strip().lower() == "si":
            print("Deteniendo el programa...\n")
            print("Termino!")
            break
def tabla_multiplicar(n):
    diccionario = {i: n*i for i in range(1, 12)}
    for c, v in diccionario.items():
        print(f"{c:<2}  |  {v:<2}")


numero = int(input("Ingrese un numero para ver su tabla: "))
tabla_multiplicar(numero)
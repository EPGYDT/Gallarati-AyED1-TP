def tabla_multiplicar(n):
    """
    Contrato:
        - Imprime la tabla de multiplicar de un numero.
    Pre:
        - Recibe un numero entero.
    Post:
        - Imprime los productos del numero por los enteros del 1 al 11.
    """
    diccionario = {i: n*i for i in range(1, 12)}
    for c, v in diccionario.items():
        print(f"{c:<2}  |  {v:<2}")


numero = int(input("Ingrese un numero para ver su tabla: "))
tabla_multiplicar(numero)
def calcular_oblongo(numero: int) -> bool:
    """
    Verifica si el numero ingresado es oblongo.
    Pre: Recibe un numero entero positivo.
    Post: devuelve un booleano que informa si el numero es o no es oblongo.
    """
    assert isinstance(numero, int) and numero > 0, "El numero debe ser un entero positivo."

    oblongo = False
    for i in range(numero):
        if i * (i+1) == numero:
            oblongo = True
            break
        elif i * (i+1) > numero:
            break

    return oblongo

numero = int(input("Ingrese un numero para verificar si es oblongo: "))
print(calcular_oblongo(numero))



def calcular_triangular(numero: int) -> bool:
    """
    Verifica si el numero ingresado es triangular.
    Pre: Recibe un numero entero positivo.
    Post: Devuelve un booleano que informa si el numero es triangular o no.
    """
    assert isinstance(numero, int) and numero > 0, "El numero debe ser un entero positivo."
    triangular = False
    acumulador = 0
    for i in range(numero):
        acumulador += i
        if acumulador == numero:
            triangular = True
            break
        elif acumulador > numero:
            break

    return triangular

numero = int(input("Ingrese un numero para verificar si es triangular: "))

print(calcular_triangular(numero))


numero = int(input("Ingrese un numero para verificar si es oblongo: "))

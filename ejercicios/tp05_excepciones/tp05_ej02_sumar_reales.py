import re


def sumar_reales(cadena1: str, cadena2: str):
    """
    Contrato:
        -

    Pre:
        -

    Post:
        -
    """
    try:
        num1 = float(cadena1)

    except ValueError:
        print("El primer valor no es un numero.")
        return -1

    try:
        num2 = float(cadena2)

    except ValueError:
        print("El segundo valor no es un numero.")
        return -1

    else:
        return num1 + num2


cadena = input("Ingrese un numero: ")

cad = input("Ingrese un segundo numero: ")
print(sumar_reales(cadena, cad))
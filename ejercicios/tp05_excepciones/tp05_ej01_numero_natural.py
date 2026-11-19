class NumeroNegativoError(Exception):
    pass


def ingresar_numero():
    """
    Contrato:
        - Solicita al usuario un numero entero positivo.
    Pre:
        - No requiere datos previos.
    Post:
        - Devuelve el numero ingresado si es positivo.
        - Solicita nuevamente el dato cuando el numero no es valido.
    """
    try:
        numero = int(input("Ingrese un numero: "))
        if numero <= 0:
            raise NumeroNegativoError

    except NumeroNegativoError:
        print("El numero no es positivo.")

    except AssertionError:
        print("Se debe ingresar un numero entero.")

    else:
        return numero


ingresar_numero()

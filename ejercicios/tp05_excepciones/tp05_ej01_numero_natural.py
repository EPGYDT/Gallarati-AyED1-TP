class NumeroNegativoError(Exception):
    pass


def ingresar_numero():
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

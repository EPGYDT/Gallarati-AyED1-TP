#EJ 2

def verif_dia(dia: int, mes: int, ano: int) -> bool:
    """
    Verifica si la fecha ingresada es una fecha real.
    Pre: necesita un dia, mes y año que sean numeros enteros.
    Post: Devuelve un booleano en vase a si la fecha es real o no.
    """
    assert isinstance(dia, int) and isinstance(mes, int) and isinstance(ano, int), "Los numeros de la fecha deben ser enteros."
    assert dia > 0 and mes > 0 and ano > 0, "Los numeros de la fecha deben ser positivos."

    biciesto = verif_biciesto(ano)
    if mes > 0 and dia > 0 and ano > 0:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia <= 31 and dia > 0:
                return True
            else:
                return False

        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:

            if dia <= 30 and dia > 0:
                return True
            else:
                return False

        elif mes == 2:
            if biciesto == True:
                if dia > 0 and dia <= 29:
                    return True
                else:
                    return False
            else:
                if dia > 0 and dia <= 28:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False


def verif_biciesto(ano: int) -> bool:
    """
    Verifica si el año es o no biciesto.
    Pre: El numero debe ser un entero positivo
    Post: devuelve un booleano en base a si el ano es biciesto o no.
    """
    assert isinstance(ano, int) and ano > 0, "El año debe ser un numero entero positivo"

    if ano % 400 == 0:
        return True

    elif ano % 4 == 0 and ano % 100 != 0:
        return True

    else:
        return False

print(verif_dia(1, 1, 2001))
print(verif_dia(18, 2, 2008))
print(verif_dia(29, 2, 2008))
print(verif_dia(29, 2, 2009))
print(verif_dia(31, 6, 2040))
def diasiguiente(dia: int, mes: int, ano: int) -> tuple:
    """
    Calcula la fecha siguiente al dia ingresado.
    Pre: Recibe tres enteros positivos equivalentes a una fecha.
    Post: Retorna la fecha del dia siguiente al ingresado en forma de tupla.
    """
    assert 32 > dia > 0 and 13 > mes > 0 and ano > 0, "Los dias deben ser de 1 a 31, los meses de 1 a 12, y el año mayor a 0."
    assert verif_dia(dia, mes, ano) == True, "La fecha es erronea."

    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10:
        if dia < 31:
            dia += 1
        else:
            dia = 1
            mes += 1

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia < 30:
            dia += 1
        else:
            dia = 1
            mes += 1

    elif mes == 2:
        
        biciesto = verif_biciesto(ano)
        if biciesto == True:
            if dia < 29:
                dia += 1
            else:
                dia = 1
                mes = 3
        else:
            if dia < 28:
                dia += 1
            else:
                dia = 1
                mes = 3
    else:
        if dia < 31:
            dia += 1
        else:
            dia = 1
            mes = 1
            ano += 1

    return dia, mes, ano

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



dia = int(input("Ingrese un dia: "))
mes = int(input("Ingrese un mes: "))
ano = int(input("Ingrese un año: "))
print()
#Añadir X cantidad de dias:
print(f"la fecha siguiente es: {diasiguiente(dia, mes, ano)}")
print(f"\n\n")
cantidad_de_vueltas = int(input("Ingrese la cantidad de dias que quiere añadir a la fecha original: "))

for i in range(cantidad_de_vueltas):
    dia, mes, ano = diasiguiente(dia, mes, ano)

print(dia, mes, ano)


#Ver la diferencia de dias entre dos fechas:
print(f"\n---Ingrese dos fechas para ver cuantos dias tienen de diferecia---\n\n")
dia1 = int(input("Ingrese un dia: "))
mes1 = int(input("Ingrese un mes: "))
ano1 = int(input("Ingrese un año: "))
print()
dia2 = int(input("Ingrese un segundo dia: "))
mes2 = int(input("Ingrese un segundo mes: "))
ano2 = int(input("Ingrese un segundo año: "))

dias = 0

if (dia1, mes1, ano1) > (dia2, mes2, ano2):
    while (dia1, mes1, ano1) != (dia2, mes2, ano2):
        dia2, mes2, ano2 = diasiguiente(dia2, mes2, ano2)
        dias += 1
    print(f"Hay {dias} dias de diferencia entre ambas fechas.")

elif (dia1, mes1, ano1) < (dia2, mes2, ano2):
    while (dia1, mes1, ano1) != (dia2, mes2, ano2):
        dia1, mes1, ano1 = diasiguiente(dia1, mes1, ano1)
        dias += 1
    print(f"Hay {dias} dias de diferencia entre ambas fechas.")

else:
    print("Ambas fechas son iguales.")


"""
Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios,
y luego escribir un programa que las vincule:

a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha válida.

b. Sumar N días a una fecha.

c. Ingresar un horario desde teclado, verificando que sea correcto.

d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
segundo se considerará que el primero corresponde al día anterior.
En ningún caso la diferencia en horas puede superar las 24 horas.
"""

def verificar_fecha(dia: int, mes: int, ano: int) -> bool:
    biciesto = verif_biciesto(ano)
    treinta_y_uno = (1, 3, 5, 7, 8, 10, 12)
    treinta = (4, 6, 9, 11)
    
    if mes > 0 and dia > 0 and ano > 0:
        if mes in treinta_y_uno:
            if dia <= 31 and dia > 0:
                return True
            else:
                return False

        elif mes in treinta:

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
    if ano % 400 == 0:
        return True

    elif ano % 4 == 0 and ano % 100 != 0:
        return True

    else:
        return False


def sumar_dias(n: int, dia: int, mes: int, ano: int) -> tuple[int, int, int] | None:
    if verificar_fecha(dia, mes, ano) == True:
        biciesto = verif_biciesto(ano)
        treinta_y_uno = (1, 3, 5, 7, 8, 10, 12)
        treinta = (4, 6, 9, 11)
        for i in range(n):

            if mes == 12:
                if dia == 31:
                    dia = 1
                    mes = 1
                    ano += 1
                else:
                    dia += 1

            elif mes in treinta_y_uno:
                if dia == 31:
                    dia = 1
                    mes += 1

                else:
                    dia += 1

            elif mes in treinta:
                if dia == 30:
                    dia = 1
                    mes += 1

                else:
                    dia += 1

            else:
                if dia == 29:
                    dia = 1
                    mes += 1

                elif dia == 28:
                    if biciesto:
                        dia += 1
                    else:
                        dia = 1
                        mes += 1 

                else:
                    dia += 1

        return dia, mes, ano

    else:
        print("La fecha es incorrecta, no se le pueden añadir dias.")


def verificar_horario(horas: int, minutos: int) -> bool:
    if horas > 23 or horas < 0 or minutos > 59 or minutos < 0:
        print("Error, horario, invalido.")
        return False

    else:
        print("horario correcto")
        return True


def calcular_diferencia_horarios(horas: int, minutos: int, horas2: int, minutos2: int):
    if horas > horas2:
        dif_horas = horas - horas2
        dif_minutos = minutos - minutos2
        if dif_minutos < 0:
            dif_minutos += 60
            dif_horas -= 1

    elif horas < horas2:
        dif_horas = horas2 - horas
        dif_minutos = minutos2 - minutos
        if dif_minutos < 0:
            dif_minutos += 60
            dif_horas -= 1

    else:
        dif_horas = 0
        if minutos > minutos2:
            dif_minutos = minutos - minutos2

        elif minutos < minutos2:
            dif_minutos = minutos2 - minutos

        else:
            dif_minutos = 0
            print("Ambos horarios son iguales")

    return dif_minutos, dif_horas



fecha = input("Ingrese una fecha (Ejemplo: 7/5/2010): ").strip().split("/")
dia, mes, ano = int(fecha[0]), int(fecha[1]), int(fecha[2])
if verificar_fecha(dia, mes, ano) == True:
    print("La fecha es valida")

else:
    print("La fecha es invalida.")


n = int(input(f"Ingrese la cantidad de dias que le quiere añadir a la fecha {fecha[0]}/{fecha[1]}/{fecha[2]} : "))

dia, mes, ano = sumar_dias(n, dia, mes, ano)

print(f"Fecha con {n} dias agregados: {dia}/{mes}/{ano}")


horario = input("Ingrese un horario (Ejemplo: 20:40): ").strip().split(":")
horas, minutos = int(horario[0]), int(horario[1])

horario_valido = verificar_horario(horas, minutos)

if horario_valido:
    horario2 = input("Ingrese un segundo horario para comparar con el primero(Ejemplo: 20:40): ").strip().split(":")
    horas2, minutos2 = int(horario2[0]), int(horario2[1])

    if verificar_horario(horas2, minutos2):
        dif_min, dif_hor = calcular_diferencia_horarios(horas, minutos, horas2, minutos2)
        print(f"La diferencia entre ambos horarios es de: \nHoras: {dif_hor}     Minutos: {dif_min}")
    else:
        print("El horario ingresado no es valido")

else:
    print("El horario ingresado no es valido")
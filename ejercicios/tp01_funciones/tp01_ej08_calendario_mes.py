# Variables globales

dias_semana = ("Dom", "Lun", "Mar", "Mie", "Jue", "Vie", "Sab")
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
treinta_y_uno = (1, 3, 5, 7, 8, 10, 12)
treinta = (4, 6, 9, 11)


# Funciones

def diadelasemana(dia: int,mes: int,ano: int) -> int:
    if mes < 3:
        mes = mes + 10
        ano = ano - 1
    else:
        mes = mes - 2
    siglo = ano // 100
    año2 = ano % 100
    diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem


def generar_mes(dia: int, dias: int) -> list[int]:
    """
    Contrato:
        - Genera una lista con todos los dias del mes indcado por la fecha que ingreso el usuario

    Pre:
        - Recibe dos enteros positivos. El primero indica el dia con el que empieza el mes,
        y el segundo cuantos dias tiene el mes.

    Post:
        - Retorna una lista con todos los dias del mes ingresado y la
    """
    mes = [0 for d in range(dia)]

    mes.extend(range(1, dias+1))

    return mes



def imprimir_mes(mes: int, ano: int, lista: list[int])-> None:
    """
    Contrato:
        # -Imprime el mes de manera que simule un calendario.
        
    Pre:
        -Recibe dos enteros positivos (el mes y el año), y una lista con todos los dias del mes.
        
    Post:
        -No retorna nada, solo realiza prints.
    """

    print(f"{meses[mes-1]} de {ano}")
    print()
    for d in dias_semana:
        print(f"{d}", end="  ")

    print()
    contador = 0
    for d in lista:
        if d:
            print(f'{str(d):>3}', end="  ")
        else:
            print(f"   ", end="  ")
        contador += 1

        if contador == 7:
            print()
            contador = 0




def main():
    """
    Contrato:
        - Ejecuta el código principal.
    
    Pre:
        - No recibe nada.
    
    Post:
        - No retorna nada, solo ejecuta el código principal.
    """
    while True:
        mes = int(input("Ingrese un mes: "))
        ano = int(input("Ingrese un año: "))

        if mes > 12 or mes <= 0:
            print("Mes inválido, intente nuevamente.")
            continue

        elif mes in treinta_y_uno:
            dias = 31
            break

        elif mes in treinta:
            dias = 30
            break

        else:
            if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
                dias = 29

            else:
                dias = 28

            break


    dia = diadelasemana(1, mes, ano)

    lista = generar_mes(dia, dias)
    print()
    imprimir_mes(mes, ano, lista)


# Código principal.

main()
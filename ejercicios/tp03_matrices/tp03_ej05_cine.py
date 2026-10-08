import random as rn

def generar_matriz(filas, butacas):
    return [[rn.choice(["X", "-"]) for butaca in range(1, butacas+1)] for fila in range(filas)]



def mostrar_butacas(matriz: list[list]):
    """
    Contrato:
        - Muestra todas las butacas, ordenadas en filas y columnas.
    Pre:
        - Recibe la matriz con todos los datos de las butacas.
    Post:
        - No retorna nada, realiza varios prints para mostar la matriz.
    """
    largo = len(matriz)
    alto = len(matriz[0])
    print("Columnas: ", end="")
    for i in range(alto):
            print(f"{i+1:>2}", end="")

    print()

    for lista in range(largo):
        print(f"Fila {lista+1:>2}:  ", end="|")
        for e in matriz[lista]:
            print(f"{e}", end="|")

        print()



def reservar(matriz: list[list]):
    """
    Contrato:
       - Reserva una de las butacas que no este ocupada. La butaca es indicada por el usuario.
    Pre:
       - Recibe la matriz con todos los datos de las butacas.
    Post:
       - No retorna nada, actualiza la matriz o realiza un print que informa que no se pudo reservar la butaca (ya estaba ocupada).
    """
    while True:
        try:
            fila = int(input("Ingrese el numero de fila de la butaca que quiere reservar: "))
        except ValueError:
            print("Error, ingrese un entero positivo")
        else:
            if fila > 9 or fila < 1:
                print("Error, la fila debe estar entre 1 y 9")

            else:
                break
    
    while True:
        try:
            columna = int(input("Ingrese el numero de columna de la butaca que quiere reservar: "))
        except ValueError:
            print("Error, ingrese un entero positivo")
        else:
            if columna > 9 or columna < 1:
                print("Error, la columna debe estar entre 1 y 9")

            else:
                break

    if matriz[fila-1][columna-1] == "X":
        print("Esa butaca ya esta ocupada")
        return
    else:
        matriz[fila-1][columna-1] = "X"
        return



def butacas_libres(matriz: list[list[str]]):
    """
    Contrato:
        - Muestra la cantidad total de butacas libres.
    Pre:
        - Recibe la matriz como parametro con todos los datos de a las butacas.
    Post:
        - Retorna un entero positivo que indica cuantas butacas libres hay.
    """
    libres = 0
    for e in matriz:
        libres += e.count("-")

    print(f"Cantidad de butacas libres: {libres}")



def butacas_contiguas(matriz: list[list[str]]):
    """
    Contrato:
        - Busca la mayor cantidad de butacas libres contiguas.
    Pre:
        - Recibe la matriz con todas las filas y colunas con los datos de las butacas.
    Post:
        - No retorna nada, solo imprime la mayor cantidad de butacas contiguas en la sala.
    """
    cant_contiguas = 0
    posicion = 0
    for i, lista in enumerate(matriz):
        actual = 0
        for e in lista:
            if e == "-":
                actual += 1
                if actual > cant_contiguas:
                    cant_contiguas = actual
                    posicion = i + 1

            else:
                actual = 0

    if cant_contiguas > 0:
        print(f"Hay {cant_contiguas} en la fila {posicion}")
    else:
        print("No hay butacas libres.")




def imprimir_opciones():
    """
    Contrato:
        - Imprime todas las opciones del menu principal.
    Pre:
        - No recibe nada.
    Post:
        - No retorna nada, solo imprime las opciones.
    """
    print("1. Reservar butaca.")
    print("2. Cant. butacas libres.")
    print("3. Mostrar butacas contiguas.")
    print("0. Salir.")



def main():
    """
    Contrato:
        - Ejecuta el codigo principal.
    Pre:
        - No recibe nada.
    Post:
        - No retorna nada, solo llama a las funciones.
    """

    filas = 9
    butacas = 9
    matriz = generar_matriz(filas, butacas)

    while True:
        print("--- Menu de butacas --- \n")
        imprimir_opciones()
        print()
        mostrar_butacas(matriz)
        print()
        opcion = input("Ingrese una opcion: ")

        match opcion:
            case "1":
                reservar(matriz)

            case "2":
                butacas_libres(matriz)

            case "3":
                butacas_contiguas(matriz)

            case 0:
                break

            case _:
                print("Error, ingrese una opcion valida.")

""" NO LLEGUE PROFE, no puedo 🙏 """
main()
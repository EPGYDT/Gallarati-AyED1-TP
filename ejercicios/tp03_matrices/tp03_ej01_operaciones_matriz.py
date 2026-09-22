def generar_matriz(n: int) -> list[list[int]]:
    """
    Permite cargar números enteros en una matriz de N x N, ingresando los datos desde
    teclado
    Pre: Recibe un entero positivo que define el tamaño de la matriz
    Post:    
    """
    matriz = []

    for i in range(n):
        fila = []
        for j in range(n):
            num = int(input(f"Ingrese el elemento numero {j+1} de la fila numero {i+1}: "))
            fila.append(num)
        matriz.append(fila)

    return matriz



def ordenar_matriz(matriz: list[list[int]])-> None:
    """
    Ordena en forma ascendente cada una de las filas de la matriz.
    Pre: Recibe la matriz que va a ordenar.
    Post: No retorna nada, solo modifica la matriz original.
    """

    for fila in matriz:
        fila.sort()



def intercambiar_filas(matriz: list[list[int]], fila1: int, fila2: int) -> None:
    """
    Intercambia dos filas de la matriz.
    Pre: Recibe la matriz y el numero de las 2 filas.
    Post: No retorna nada, solo intercambia la posicion de las filas en la matriz.
    """
    matriz[fila1-1], matriz[fila2-1] = matriz[fila2-1], matriz[fila1-1]



def intercambiar_columnas(matriz: list[list[int]], col1: int, col2: int) -> None:
    """
    Intercambia columnas de la matriz.
    Pre: Recibe la matriz y el numero de las 2 columnas.
    Post: no retorna nada, solo actualiza la matriz con la posicion de las columnas intercambiada.
    """

    for i in range(len(matriz)):
        matriz[i][col1 - 1], matriz[i][col2 - 1] = matriz[i][col2 - 1], matriz[i][col1 - 1]




def trasponer(matriz: list[list[int]]) -> None:
    """
    Traspone la matriz sobre si misma, (intercambia cada elemento Aij por Aji).
    Pre: Recibe la matriz con todos los datos.
    Post: No retorna nada, solo actualiza la matriz original.
    """
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz)):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]



def promedio_fila(matriz: list[list[int]], fila: int) -> float:
    """
    Calcula el promedio de los elementos de una fila
    Pre: Recibe la matriz con todos los datos y el numero de fila sobre la cual va a calcular el promedio de sus elementos.
    Post: Retorna un flotante positivo que equivale al promedio de todos los elementos de una fila de la matriz
    """

    promedio = sum(matriz[fila-1]) / len(matriz[fila-1])
    return promedio



def porcentaje_impares(matriz: list[list[int]], col: int) -> float:
    """
    Calcula el porcentaje de impares de una columna.
    Pre: Recibe la matriz con todos los datos y un entero positivo que representa la columna.
    Post: Retorna un flotante que representa el porcentaje de impares en la columna ingresada.
    """
    impares = 0
    largo = len(matriz)
    for i in range(largo):
        if matriz[i][col-1] % 2 == 1:
            impares += 1

    return  100 * impares / largo



def determinar_simetria(matriz: list[list[int]]):
    """
    Determina si una matriz es simetrica en base a su diagonal principal.
    Pre: Recibe la matriz con todas las filas y columnas.
    Post: Retorna un booleano en base a si la matriz es simetrica segun su diagonal principal.
    """

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return False

    return True



def simetria_secundaria(matriz: list[list[int]]):
    """
    Determina si una matriz es simetrica en base a su diagonal secundaria.
    Pre: Recibe la matriz con todas las filas y columnas.
    Post: Retorna un booleano en base a si la matriz es simetrica segun su diagonal secundaria.
    """
    largo = len(matriz)
    for i in range(largo):
        for j in range(largo):
            if matriz[i][j] != matriz[largo -1 -j][largo - 1 -i]:
                return False

    return True



def palindromos(matriz: list[list[int]]) -> list[int]:
    """
    Determina qué columnas de la matriz son palíndromos (capicúas).
    Pre: Recibe la matriz con todas las filas y columnas
    Post: Retorna una lista con todos los numeros de las columnas que son palíndromos
    """
    columnas = []
    largo = len(matriz)
    for i in range(largo):
        columna = []
        for j in range(largo):
            columna.append(matriz[j][i])

        if columna == columna[::-1]:
            columnas.append(i+1)

    return columnas



def main():
    """
    Ejecuta el codigo principal.
    Pre: No recibe nada
    Post: No retorna nada, solo ejecuta el codigo.
    """

    #Generar matriz
    while True:
        n = int(input("Ingrese el valor de tamaño de la matriz (n x n): "))
        if n <= 0:
            print("Error, ingrese un entero positivo.")
        else:
            break

    matriz = generar_matriz(n)
    print(matriz)


    #Simetria diagonal principal
    verificador = determinar_simetria(matriz)

    if verificador:
        print("La matriz es simetrica en base a su diagonal principal.")
    else:
        print("La matriz no es simetrica en base a su diagonal principal.")


    #Simetria diagonal secundaria
    verificador = simetria_secundaria(matriz)

    if verificador:
        print("La matriz es simetrica en base a su diagonal secundaria.")
    else:
        print("La matriz no es simetrica en base a su diagonal secundaria.")

    #Palidromos
    print(f"Lista con las columnas palindromos: {palindromos(matriz)}")


    #Ordenar matriz
    ordenar_matriz(matriz)

    print(f"Elementos de matriz en orden ascendente: {matriz}")


    #Intercambiar filas
    while True:
        fila1 = int(input("Ingrese la primera fila para cambiar de lugar: "))
        
        if fila1 <= 0 or fila1 > n:
            print("Error, ingrese una fila valida.")
        else:
            break

    while True:
        fila2 = int(input("Ingrese la segunda fila para cambiar de lugar: "))
        
        if fila2 <= 0 or fila2 > n:
            print("Error, ingrese una fila valida.")
        else:
            break

    intercambiar_filas(matriz, fila1, fila2)
    print(f"Matriz con filas intercambiadas: {matriz}")


    #Intercambiar columnas
    while True:
        columna1 = int(input("Ingrese la primera columna para cambiar de lugar: "))
        
        if columna1 <= 0 or columna1 > n:
            print("Error, ingrese un entero positivo.")
        else:
            break

    while True:
        columna2 = int(input("Ingrese la segunda columna para cambiar de lugar: "))
        
        if columna2 <= 0 or columna2 > n:
            print("Error, ingrese un entero positivo.")
        else:
            break

    intercambiar_columnas(matriz, columna1, columna2)
    print(f"Matriz con columnas intercambiadas: {matriz}")


    #Trasponer matriz
    trasponer(matriz)
    print(f"Matriz traspuesta sobre si misma: {matriz}")


    #Promedio de elementos en una fila
    fila = 0
    while fila <= 0 or fila > n:
         fila = int(input("Ingrese un numero de fila para ver el promedio de sus elementos: "))

    print(f"El promedio de los elementos de la fila {fila} es de {promedio_fila(matriz, fila)}")


    #Porcentaje impares
    columna = 0
    while columna <= 0 or columna > n:
        columna = int(input("Ingrese un numero de columna para ver el porcentaje de impares en sus elementos: "))

    print(f"El porcentaje de impares en la columna {columna} es de: {porcentaje_impares(matriz, columna):.2f}%")



main()
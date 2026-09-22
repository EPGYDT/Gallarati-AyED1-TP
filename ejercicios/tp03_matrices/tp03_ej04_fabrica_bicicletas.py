from random import randint


def generar_matriz(n) -> list[list]:
    """
    Genera una matriz con la cantidad de listas definida por el usuario.
    Pre: Recibe un entero positivo que determina el tamaño de la matriz.
    Post: Retorna una matriz de longitud 'n'. 
    """
    return [[] for i in range(n)]



def cargar_matriz(matriz: list[list]):
    """
    
    
    
    """
    for i in range(len(matriz)):
        for j in range(6):
            matriz[i].append(randint(0, 150))



def cant_total(matriz: list[list[int]])-> None:
    for i in range(len(matriz)):
        print(f"Cantidad de bicicletas de la fabrica {i+1}: {sum(matriz[i])}\n")


def mayor_fabrica(matriz: list[list[int]]) -> None:
    dias =["lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]
    dia_mayor = 0
    prod_mayor = 0
    fabrica_mayor = 0
    for j in range(len(matriz)):
        for i, e in enumerate(matriz[j]):
            if e > prod_mayor:
                prod_mayor = e
                dia_mayor = dias[i]
                fabrica_mayor = j+1

    print(f"El dia de mayor produccion fue el {dia_mayor} con {prod_mayor} bicicletas en la fabrica {fabrica_mayor}.")



def dia_mas_prod(matriz: list[list[int]])-> None:
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]
    producciones = [0, 0, 0, 0, 0, 0]
    for j in range(len(matriz)):
        for i, e in enumerate(matriz[j]):
            producciones[i] += e

    mayor_prod = max(producciones)

    for i in range(len(producciones)):
        if mayor_prod == producciones[i]:
            mayor_dia = dias[i]


    print(f"El dia de mayor produccion fue el {mayor_dia} con {mayor_prod} bicicletas entre todas las fabricas.")



def menor_cant(matriz: list[list[int]])-> None:
    cant_fabrica = [min(matriz[lista]) for lista in matriz]
    fabrica = 1
    for e in cant_fabrica:
        print(f"Menor cantidad fabricada de la fabrica {fabrica}: {e}")
        fabrica += 1



def imprimir_matriz(matriz: list[list]):
    for e in matriz:
        print(e)



n = int(input("Ingrese una cantidad de fabricas: "))
matriz = generar_matriz(n)
cargar_matriz(matriz)
print()
imprimir_matriz(matriz)
print()
cant_total(matriz)
print()
mayor_fabrica(matriz)
print()
dia_mas_prod(matriz)
print()
menor_cant(matriz)
from random import randint

def generar_m_aleatoria(n):
    matriz = [[] for i in range(n)]
    largo = n**2
    for i in range(n):
        for j in range(n):
            while True:
                numero = randint(1, largo)
                if not any(numero in lista for lista in matriz):
                    matriz[i].append(numero)
                    break

    return matriz


def imprimir_matriz(matriz):
    """
    Se encarga de imprimir una matriz lista por lista
    Pre: Recibe la matriz que va a imprimir.
    Post: No retorna nada, solo imprime la matriz
    """
    largo = len(matriz)
    for i in range(largo):
        print(matriz[i])

n = int(input("Ingrese el numero de largo y ancho de la matriz"))
imprimir_matriz(generar_m_aleatoria(n))
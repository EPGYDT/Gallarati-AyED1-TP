def generar_matriz(n)-> list[list[int]]:
    """
    Genera una matriz de n x n donde  
    
    
    """
    return [[0 for i in range(n)] for i in range(n)]

def imprimir_matriz(matriz):
    largo = len(matriz)
    for i in range(largo):
        print(matriz[i])

def a(n: int)-> list[list[int]]:
    matriz = generar_matriz(n)
    num = 1
    for i in range(n):
        matriz[i][i] = num
        num += 2

    return matriz



def b(n: int)-> list[list[int]]:
    matriz = generar_matriz(n)
    num = 1
    largo = n
    for i in range(n):
        matriz[largo - 1 -i][i] = num
        num *= 3

    return matriz



def c(n: int)-> list[list[int]]:
    matriz = generar_matriz(n)
    largo = len(matriz)

    for i in range(n):
        for j in range(i+1):
            matriz[i][j] = n-i
    return matriz


def d(n: int)-> list[list[int]]:
    matriz = generar_matriz(n)
    largo = len(matriz)
    num = n*2
    for i in range(n):
        for j in range(n):
            matriz[i][j] = num
        num //= 2

    return matriz


def e(n: int)-> list[list[int]]:
    matriz = generar_matriz(n)
    largo = n
    contador = 1
    fila = 1
    for i in range(n):
        for j in range(n):
            if j % 2 == 1 and fila % 2 == 1:
                matriz[i][j] = contador
                contador += 1
                continue
                
            
    return matriz


"""HASTA ACA ABARCA MI TIEMPO 🥀"""

def f(n: int)-> list[list[int]]:
    matriz = generar_matriz(n)
    largo = n
    numeros = 1
    for i in range(largo):
        for j in range(1,largo+1):
            if j <= i+1:
                matriz[i][-j] = numeros
                numeros += 1

    return matriz

        


def g(n: int)-> list[list[int]]:
    matriz = generar_matriz(n)
    numeros = [num for num in range(1, n*n+1)]
    largo = n
    for i in range(largo):
        matriz[i][i:-i] = numeros[:largo]
        numeros.remove(matriz[i][i:-i])
        for j in range(largo):
            matriz[i]


def h(n: int)-> list[list[int]]:
    pass


def i(n: int)-> list[list[int]]:
    pass


n = int(input("Ingrese el largo y ancho de la matriz: "))

print("\nFuncion a:")
imprimir_matriz(a(n))
print("\nFuncion b:")
imprimir_matriz(b(n))
print("\nFuncion c:")
imprimir_matriz(c(n))
print("\nFuncion d:")
imprimir_matriz(d(n))
print("\nFuncion e:")
imprimir_matriz(e(n))
print("\nFuncion f:")
imprimir_matriz(f(n))
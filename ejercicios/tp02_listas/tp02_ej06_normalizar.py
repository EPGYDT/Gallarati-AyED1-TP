def normalizar(lista: list) -> float:
    """
    Normaliza todos los elementos de una lista (hace que la suma de todos ellos de 1).
    Pre: Recibe una lista con numeros enteros positivos.
    Post: retorna la misma lista con todos sus elementos normalizados.
    """

    valor = 0
    for elemento in lista:
        valor += elemento
        
    valor = 1 / valor

    for i in range(len(lista)):
        lista[i] *= valor

    return lista


lista = [1, 1, 2]
print(normalizar(lista))
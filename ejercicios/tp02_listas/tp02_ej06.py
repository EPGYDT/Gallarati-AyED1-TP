def normalizar(lista: list) -> float:

    valor = 0
    for elemento in lista:
        valor += elemento
        
    valor = 1 / valor

    for i in range(len(lista)):
        lista[i] *= valor

    return lista


lista = [1, 1, 2]
print(normalizar(lista))
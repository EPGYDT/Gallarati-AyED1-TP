def intercalar_elementos(lista1: list[int], lista2: list[int]) -> list[int]:
    """
    Intercala dos listas en una la primera de ellas.
    Pre: Recibe dos listas con enteros positivos.
    Post: Devuelve la primera lista intercalada con las segunda.
    """
    for i, e in enumerate(lista2):
        lista1[(i+i+1):(i+i+1)] = [e]
    return lista1


lista1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

lista2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(intercalar_elementos(lista1, lista2))
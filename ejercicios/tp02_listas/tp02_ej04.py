def eliminar_elementos(lista: list[int], lista_elim: list[int]):
    """
    Elimina de una lista los elementos de otra lista.
    Pre: Recibe dos listas con enteros.
    Post: Retorna la primera lista sin los elementos de la segunda lista.
    """
    print(f"Lista original: {lista}")
    for e in lista:
        if e in lista_elim:
            lista.remove(e)
    print(f"Lista elementos a eliminar: {lista_elim}")
    print(f"Lista con elementos eliminados: {lista}")


lista = [n for n in range(1, 50, 2)]
lista_eliminados = lista[7: 15]

eliminar_elementos(lista, lista_eliminados)
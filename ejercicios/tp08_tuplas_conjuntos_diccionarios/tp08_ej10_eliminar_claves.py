def eliminarclaves(diccionario: dict, lista: list):
    """
    Contrato:
        - Elimina del diccionario las claves incluidas en una lista.
    Pre:
        - Recibe un diccionario y una lista de claves.
    Post:
        - Modifica el diccionario eliminando las claves existentes.
        - Imprime el diccionario resultante y la cantidad eliminada.
    """
    eliminados = 0
    for e in lista:
        try:
            del diccionario[e]

        except KeyError:
            continue
        else:
            eliminados += 1

    print(f"Diccionario sin las claves de la lista: ")
    print(diccionario)
    print(f"Cantidad de claves eliminadas: {eliminados}")



diccionario = {
    "Carnes": "pollo",
    "Lacteos": "leche",
    "Pescados": "salmon"
    }

print(f"Diccionario: {diccionario}")


lista = [
    "Carnes",
    "Leche",
    "Pescados"
]

print(f"Lista: {lista}\n")

eliminarclaves(diccionario, lista)
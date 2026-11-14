def eliminarclaves(diccionario: dict, lista: list):
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
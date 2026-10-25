def filtrar_palabras_1(cadena: str, n: int) -> str:
    """
    Contrato:
        -
    Pre:
        -
    Post:
        -
    """
    lista = cadena.split()
    nueva_cadena = []
    for palabra in lista:
        if len(palabra) > n:
            nueva_cadena.append(palabra)

    return " ".join(nueva_cadena)


def filtrar_palabras_2(cadena: str, n: int) -> str:
    """
    Contrato:
        -
    Pre:
        -
    Post:
        -
    """
    lista = cadena.split()
    nueva_cadena = [palabra for palabra in lista if len(palabra) > n]
    return " ".join(nueva_cadena)


def filtrar_palabras_3(cadena: str, n: int) -> str:
    """
    Contrato:
        -
    Pre:
        -
    Post:
        -
    """
    lista = cadena.split()
    nueva_cadena = list(filter(lambda palabra: len(palabra) > n, lista))
    return " ".join(nueva_cadena)

cadena = "ella sapo pollo queso el fiambre pass pepito pe"
n = 4

print("Metodo uno (ciclo normal):")
print(f"{filtrar_palabras_1(cadena, n)}\n")
print("Metodo dos (lista por comprension):")
print(f"{filtrar_palabras_2(cadena, n)}\n")
print("Metodo tres (funcion filter):")
print(f"{filtrar_palabras_3(cadena, n)}\n")
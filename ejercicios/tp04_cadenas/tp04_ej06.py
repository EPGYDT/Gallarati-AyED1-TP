def extraer_subcadena_slices(cadena: str, posicion: int, n: int) -> None:
    """
    Contrato:
        -
    Pre:
        -
    Post:
        -
    """
    subcadena = cadena[posicion: posicion + n + 1]
    return subcadena

def extraer_subcadena(cadena: str, posicion: int, n: int) -> None:
    """
    Contrato:
        -
    Pre:
        -
    Post:
        -
    """
    subcadena = ""
    for i in range(n):
        subcadena += cadena[posicion + i]
    return subcadena

cadena = "El número de teléfono es 4356-7890"
print(f"Cadena: {cadena}")
posicion = 25
print(f"Posicion: {posicion}")
caracteres = 9
print(f"Caracteres: {caracteres}\n")

print("Con slices:")
print(f"{extraer_subcadena_slices(cadena, posicion, caracteres)}\n")
print("Sin slices:")
print(f"{extraer_subcadena(cadena, posicion, caracteres)}")
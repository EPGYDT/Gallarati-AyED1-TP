def eliminar_subcadena(cadena: str, subcadena: str) -> str:
    """
    Contrato:
        -
    Pre:
        -
    Post:
        -
    """
    if subcadena in cadena:
        texto = "".join(cadena.split(subcadena))
        return texto

    else:
        return "La subcadena no se encontraba en la cadena."


def eliminar_subcadena_slices(cadena: str, subcadena: str) -> str:
    """
    Contrato:
        -
    Pre:
        -
    Post: 
        -
    """
    if subcadena in cadena:
        posicion = cadena.find(subcadena)
        texto = cadena[:posicion] + cadena[posicion+len(subcadena):]
        return texto

    else:
        return "La subcadena no se encontraba en la cadena."

cadena = "el hombre que tenia cabeza de caballo es muy fuerte"
print(f"Cadena: {cadena}")
subcadena = "que tenia cabeza de caballo"
print(f"Subcadena: {subcadena}\n")

print("Sin slices:")
print(eliminar_subcadena(cadena, subcadena))
print("Con slices:")
print(eliminar_subcadena_slices(cadena, subcadena))
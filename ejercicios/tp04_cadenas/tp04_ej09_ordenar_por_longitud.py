def ordenar_cadena(cadena: str) -> str:
    """
    Contrato:
        -

    Pre:
        -

    Post:
        -
    """

    lista = [palabra.strip() for palabra in cadena.split()]
    lista = sorted(lista, key=len)
    return " ".join(lista)

cadena = "  pescado        ballena   megalodon      delfin   beluga pato   narval     tortuga   "
print(f"Cadena de caracteres: \n {cadena}")

print(f"\nCadena ordenada: \n {ordenar_cadena(cadena)}")
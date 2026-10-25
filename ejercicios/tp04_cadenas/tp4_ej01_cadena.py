def verificar_capicua(texto: str)-> bool:
    """
    Contrato:
        - Indica si una cadena de texto es un palindromo (capicua).
    Pre:
        - Recibe un string.
    Post:
        - Retorna un booleano que indica si la cadena ingresada es o no un palindromo.
    """
    
    return texto == "".join(reversed(texto))


cadena = "neuquen"
print(verificar_capicua(cadena))

cadena = "santa fe"
print(verificar_capicua(cadena))

cadena = "capicua aucipac"
print(verificar_capicua(cadena))


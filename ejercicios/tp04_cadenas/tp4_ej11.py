def hallar_subcadena(cadena: str, subcadena: str):
    """
    Contrato:
        - Indica cuantas veces aparece una subcadena dentro de otra.
    Pre:
        - Recibe dos cadenas de caracteres.
    Post:
        - Retorna un entero que indica la cantidad de veces que aparece la segunda cadena en la primera cadena.
    """
    posicion = 0
    sub_letra = subcadena[posicion]
    cant_apariciones = 0

    for letra in cadena:
        if letra.lower() == sub_letra.lower():
            if sub_letra == subcadena[-1:]:
                posicion = 0
                sub_letra = subcadena[posicion]
                cant_apariciones += 1

            else:
                posicion += 1
                sub_letra = subcadena[posicion]

    return cant_apariciones


cadena = input("Ingrese la cadena: ")
sub_cadena = input("Ingrese la subcadena: ")


print(hallar_subcadena(cadena, sub_cadena))
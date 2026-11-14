def validar_domino(ficha1: tuple[int, int], ficha2: tuple[int, int]) -> bool:
    """
    Contrato:
        - Indica si dos fichas de domino encajan entre si o no.
    Pre:
        - Recibe dos tuplas con dos enteros cada una.
    Post:
        - Retorna un booleano en base a si las fichas encajan o si no.
    """
    return bool(set(ficha1) & set(ficha2))
"Utilice el operador '&' que permite realizar una interseccion entre conjuntos, es decir, '&' retorna los  elementos que tienen en comun"


ficha1 = tuple(input("Ingrese una ficha de domino (ejemplo: 4/3): ").split("/"))
ficha2 = tuple(input("Ingrese una segunda ficha de domino (ejemplo: 5/0): ").split("/"))
print(validar_domino(ficha1, ficha2))
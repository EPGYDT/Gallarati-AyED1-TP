def verificar_ortogonales(vector1: tuple[int, int], vector2: tuple[int, int]) -> bool:
    """
    Contrato:
        - Indica si dos vectores son ortogonales.
    Pre:
        - Recibe dos tuplas con dos enteros cada una que representan dos vectores.
    Post:
        - Retorna un booleano en base a si los vectores son ortogonales o no.
    """
    return (int(vector1[0]) * int(vector2[0])) + (int(vector1[1]) * int(vector2[1])) == 0

vector1 = tuple(input("Ingrese un vector (ejemplo: 4,3): ").split(","))
vector2 = tuple(input("Ingrese un segundo vector (ejemplo: 5,2): ").split(","))

print(verificar_ortogonales(vector1, vector2))
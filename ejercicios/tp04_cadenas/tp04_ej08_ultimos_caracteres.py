def delvolver_ultimos(cadena: str, n: int)-> str:
    """
    Contrato:
        - devolver_ultimos(cadena, n) -> str
        - Devuelve los últimos n caracteres de una cadena.

    Pre:
        - cadena es una cadena de caracteres.
        - n es un entero positivo.

    Post:
        - Retorna una cadena con los últimos n caracteres de cadena.
        - Si n es mayor que la longitud de cadena, retorna la cadena completa.
        - La cadena original no se modifica.
    """
    caracteres = cadena[-n:]
    return caracteres


texto = input("Ingrese un texto: ")
print(f"Texto: {texto}\n")
while True:
    try:
        n = int(input("Ingrese el numero de caracteres finales que quiere ver: "))
        if n > 0:
            break
        else:
            print("El numero debe ser positivo.")

    except ValueError:
        print("Error, ingrese un numero entero")


print(f"Cant. caracteres: {n}")
print(delvolver_ultimos(texto, n))
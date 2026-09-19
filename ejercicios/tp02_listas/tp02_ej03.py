def cuadrados(n: int) -> list[int]:
    """
    Genera una lista con todos los cuadrados de los enteros del 1 a n.
    Pre: Recibe un entero positivo que simboliza el indice y entero final.
    Post: Devuelve una lista con los cuadrados de todos los enteros de 1 a n.
    """
    lista = [num ** 2 for num in range(1, n+1)]
    return lista

while True:
    n = int(input("Ingrese un numero para el largo de la lista: "))
    if n <= 1:
        print("Error, ingrese un entero positivo mayor a 1.")
    else:
        break


lista = cuadrados(n)
print(f"\nLista con los cuadrados desde el 1 hasta el {n}: {lista} \n")
print(f"Ultimos diez valores de la lista (si los hay): {lista[-10: ]}")

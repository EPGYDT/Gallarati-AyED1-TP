from random import randint

def generar_lista(n: int) -> list:
    """
    Genera una lista de un largo predefinido, con numeros aleatorios del 1 al 100
    Pre: recibe un entero positivo que indica cuantos indices tendra la lista
    Post: Retorna una lista con numeros aleatorios entre el 0 y el 100
    """
    assert n > 0, "El numero debe ser un entero positivo."
    lista = []
    for i in range(n):
        lista.append(randint(1, 100))

    return lista

def verif_repetido(lista: list[int]) -> str:
    """
    Verifica si una lista tiene algun elemento repetido.
    Pre: Recibe una lista con al menos un entero
    Post: Devuelve una lista con los elementos repetidos, sin alterar la lista original
    """

    verificador = False
    repetidos = []
    for elemento in lista:
        if lista.count(elemento) > 1:
            verificador = True
            if repetidos.count(elemento) == 0:
                repetidos.append(elemento)
    if verificador:
        return f"Numeros repetidos: {repetidos}"
    else:
        return "No hubo ningun numero repetido."

def elementos_unicos(lista: list) -> list:
    """
    Recibe una lista y devuelve otra con los elementos unicos.
    Pre: Recibe una lista con al menos 1 entero
    Post: devuelve otra lista sin los valores repetidos
    """
    lista2 = []
    for e in lista:
        if lista.count(e) == 1:
            lista2.append(e)
    return lista2

n = int(input("ingrese un numero para definir cuanto va a medir la lista: "))
lista = generar_lista(n)
lista.sort()
print(f"lista generada: {lista}\n")
print(verif_repetido(lista))
print(f"La nueva lista con elementos unicos: {elementos_unicos(lista)}")
def verificar_orden(lista: list) -> bool:
    """Verifica si los elementos de una lista estan ordenados en orden ascendente.
    pre: Recibe una lista.
    Post: devuelve un booleano en base a si la lista estaba ordenada antes de la funcion."""
    return lista == sorted(lista) 


lista = []
while True:
    dato = input("ingrese un elemento para añadir a la lista (0 para salir): ")
    if dato != "0":
        lista.append(dato)
    else:
        break
print(lista)
print(verificar_orden(lista))
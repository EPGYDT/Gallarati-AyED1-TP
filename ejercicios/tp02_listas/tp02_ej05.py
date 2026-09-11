def verificar_orden(lista: list[int]) -> bool:
    return lista == sorted(lista)


lista = []
while True:
    numero = int(input("ingrese un numero para añadir a la lista (0 para salir): "))
    if numero != 0:
        lista.append(numero)
    else:
        break
print(lista)
print(verificar_orden(lista))

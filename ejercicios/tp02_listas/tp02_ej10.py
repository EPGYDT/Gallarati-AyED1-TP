from random import randint

lista = [randint(1, 100) for i in range(20)]
print(lista)

lista_filtrada = list(filter(lambda n: n%2 != 0, lista))
print(lista_filtrada)
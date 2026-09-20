lista = [n for  n in range(101, 200, 2)]
print(lista)

#Segundo metodo (mas ineficiente y mas dificil):
lista = [n for n in range(100, 200) if n % 2 != 0]
print(lista)
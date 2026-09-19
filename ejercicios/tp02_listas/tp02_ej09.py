a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))


lista = [n for n in range(a, b+1) if n % 7 == 0 and n % 5 != 0]
print(lista)
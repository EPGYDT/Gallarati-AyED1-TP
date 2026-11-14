conjunto = {4, 6, 7 ,9}
print(f"conjunto: {conjunto}")
while True:
    numero = int(input("ingrese un numero para eliminar del conjunto: "))
    if numero == -1:
        break
    try:
        conjunto.remove(numero)
    except KeyError:
        print("el numero no esta en el conjunto.")

print(conjunto)
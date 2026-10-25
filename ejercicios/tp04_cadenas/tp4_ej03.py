clave_maestra = input("Ingrese la clave maestra: ")

clave1 = str([n for i, n in enumerate(clave_maestra) if i % 2 == 0])
clave2 = [n for i, n in enumerate(clave_maestra) if i % 2 != 0]

print(clave1)
print(clave2)
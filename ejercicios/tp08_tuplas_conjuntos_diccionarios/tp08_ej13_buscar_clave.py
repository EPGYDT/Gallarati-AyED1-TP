def buscarclave(diccionario: dict, valor: int):
    """
    Contrato:
        - Busca las claves asociadas a un valor.
    Pre:
        - Recibe un diccionario y un valor entero.
    Post:
        - Devuelve una lista con las claves cuyo valor coincide.
    """
    claves = []
    for c, v in diccionario.items():
        if v == valor:
            claves.append(c)

    return claves

precios = {
    "Cuaderno": 4500,
    "Lapicera": 1000,
    "Lápiz": 500,
    "Goma de borrar": 500,
    "Regla": 1000,
    "Mochila": 18000,
    "Cartuchera": 6500,
    "Resaltador": 1800,
    "Carpeta": 3200,
    "Hojas A4": 6500,
    "Tijera": 2500,
    "Calculadora": 18000,
    "Cuaderno universitario": 6500,
    "Marcadores": 4200,
    "Corrector": 1500
}
largo = 0
for c in precios:
    if len(c) > largo:
        largo = len(c)

for c, v in precios.items():
    print(f"Clave: {c:<{largo}}    Valor: {v}")

valor = int(input("\nIngrese el valor que quiere mapear: "))
print()

lista = buscarclave(precios, valor)

print("Lista de claves que apuntan a ese valor:")
for e in lista:
    print(e)
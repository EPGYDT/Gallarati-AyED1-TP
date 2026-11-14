"""
Una librería almacena su lista de precios en un diccionario. 
Diseñar un programa para crearlo, incrementar los precios de los cuadernos en un 15%,
imprimir un listado con todos los elementos de la lista de precios e indicar cuál es 
el ítem más costoso que venden en el comercio.
"""

def imprimir_lista(diccionario):
    largo = ""
    for c in diccionario:
        if len(c) > len(largo):
            largo = c
    
    print(f"{'Productos:':<{len(largo)}}  |  Precios:\n")

    for c, v in diccionario.items():
        print(f"{c:<{len(largo)}}  |  {v}")



def main():
    productos = {}
    while True:
        nombre = input("Ingrese el nombre del producto que quiere añadir (-1 para frenar): ")
        if nombre == "-1":
            break
        elif nombre not in productos:
            precio = float(input("Ingrese el precio del producto: "))
            productos[nombre] = precio
        else:
            print("Ese producto ya existe, intente con otro: ")

    
    imprimir_lista(productos)


    input("Presione Enter para aumentar el precio de los cuadernos en un 15%: ")

    for clave in productos:
        if clave.strip().lower().startswith("cuaderno"):
            productos[clave] *= 1.15


    imprimir_lista(productos)
    mas_caro = ["", 0]
    for c, v in productos.items():
        if v > mas_caro[1]:
            mas_caro = [c, v]

    print(f"El producto mas caro fue: {mas_caro[0]}  con un valor de ${mas_caro[1]}")

main()
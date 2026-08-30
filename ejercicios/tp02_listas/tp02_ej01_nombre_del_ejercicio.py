"""
1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita
verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:

a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos
 también será un número al azar de dos dígitos.

b. Calcular y devolver el producto de todos los elementos de la lista anterior.

c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar
se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar
listas auxiliares.

d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50]
"""

from random import randint

#Funcion a
def cargar_lista_random(lista: list) -> list:
    """
    Carga una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos.
    Pre: Recibe una lista.
    Post: Devuelve una lista con elementos aleatorios añadidos.
    """

    for i in range(randint(10, 99)):
        lista.append(randint(1000, 9999))

    return lista

#Funcion b
def calcular_productos(lista: list) -> int:
    """
    Calcula el producto de todos los elementos de una lista
    Pre: Recibe una lista con al menos un entero.
    Post: Retorna un entero que 
    """
    producto = 1
    for elemento in lista:
        producto *= elemento
    return producto

#Funcion c

def eliminar_valor(valor: int, lista: list) -> list:
    """
    Elimina todas las apariciones de un valor en una lista.
    Pre: Recibe un valor para eliminar, que debe ser un entero, y una lista.
    Post: Devuelve la lista sin el valor.
    """
    for elemento in lista:
        if elemento == valor:
            lista.remove(elemento)

    return lista

#Funcion d
def capicua(lista: list) -> bool:
    """
    Verifica si la lista es capicua.
    Pre: Recibe una lista con enteros.
    Post: Devuelve un booleano que informa si la lista es capicua.
    """
    if lista == reversed(lista):
        return True
    else:
        return False

#Programa principal

lista = []

print(cargar_lista_random(lista))
print(f"/n/n")
print(calcular_productos(lista))
print(f"/n/n")
valor = int(input("Ingrese un valor para eliminarlo de la lista: "))
print(f"el producto de todos los elementos de la lista es: {eliminar_valor(valor, lista)}")
print(f"/n/n")
print(capicua(lista))
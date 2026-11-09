from math import sqrt

try:
    numero = float(input("Ingrese un numero para calcular su raiz cuadrada: "))
    if numero < 0:
        raise ValueError

except ValueError:
    print("Error, se debe ingresar un numero positivo.")

else:
    print(sqrt(numero))
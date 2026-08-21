#EJ 1
def comparador(num1, num2, num3):
    "Compara los numeros y devuelve el mayor"
    if num1 > num2:

        if num1 > num3:
            return num1

        elif num1 < num3:
            return num3

        else:
            return -1

    elif num1 < num2:

        if num2 > num3:
            return num2

        elif num2 < num3:
            return num3

        else:
            return -1

    else:

        if num1 < num3:
            return num3

        else:
            return -1

a = 0
b = 0
c = 0



while a < 1:
    a = int(input("ingrese el primer numero: "))

while b < 1:
    b = int(input("ingrese el segundo numero: "))

while c < 1:
    c = int(input("ingrese el tercer numero: "))


mayor = comparador(a, b, c)

if mayor == -1:
    print("nu hubo un solo numero mayor")

else:
    print(f"el numero mayor fue: {mayor}") 



#TP 1

#EJ 1
def comparador(num1, num2, num3):
    """
    Compara los numeros y devuelve el mayor.
    Pre: Recibe tres enteros positivos.
    Post: Devuelve el mayor unico, o un -1 en caso de no haber uno.
    """
    assert isinstance(num1, int) and isinstance(num2, int) and isinstance(num3, int), "Los numeros deben ser enteros."
    assert num1 > 0 and num2 > 0 and num3 > 0, "Los numeros deben ser positivos"
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
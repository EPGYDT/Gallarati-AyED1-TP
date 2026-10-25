def romanizar_numeros(numero: int)-> str:

    lista = []

    if numero // 1000 > 0:
        lista.append("M" * (numero // 1000))
        numero %= 1000

    if numero // 900 > 0:
        lista.append("CM")
        numero %= 900

    if numero // 500 > 0:
        lista.append("D")
        numero %= 500

    if numero // 400 > 0:
        lista.append("CD")
        numero %= 400

    if numero // 100 > 0:
        lista.append("C" * (numero // 100))
        numero %= 100

    if numero // 90 > 0:
        lista.append("XC")
        numero %= 90

    if numero // 50 > 0:
        lista.append("L")
        numero %= 50

    if numero // 40 > 0:
        lista.append("XL")
        numero %= 40

    if numero // 10 > 0:
        lista.append("X" * (numero // 10))
        numero %= 10

    if numero // 9 > 0:
        lista.append("IX")
        numero %= 9

    if numero // 5 > 0:
        lista.append("V")
        numero %= 5

    if numero // 4 > 0:
        lista.append("IV")
        numero %= 4

    if numero // 1 > 0:
        lista.append("I" * (numero // 1))

    numero_romano = "".join(lista)
    print(numero_romano)

numero = 0
while numero > 3999 or numero < 1:
    numero = int(input("Ingrese un numero para convertir en romano (max. 3999): "))
    if numero > 3999 or numero < 1:
        print("Error, numero invalido, intente nuevamente.")

5
romanizar_numeros(numero)



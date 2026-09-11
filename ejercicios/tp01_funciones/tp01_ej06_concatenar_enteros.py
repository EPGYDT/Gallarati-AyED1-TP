def concatenar(num1: int, num2: int) -> int:
    """
    Añade los digitos del segundo numero al final del primero (los concatena)
    Pre: Recibe dos numeros enteros positivos.
    Post: Devuelve el numero entero concatenado.
    """
    assert isinstance(num1, int) and isinstance(num2, int), "Ambos numeros deben ser enteros."
    assert num1 > 0 and num2 > 0, "Ambos numeros deben ser positivos."

    cant_digitos = 0
    aux = num2
    while aux != 0:
        aux //= 10
        cant_digitos += 1

    concatenado = num1 * (10 ** cant_digitos)
    return concatenado + num2

numero1 = int(input("Ingrese el primer numero para concatenar: "))
numero2 = int(input("Ingrese el numero que sera concatenado: "))

print(concatenar(numero1, numero2))
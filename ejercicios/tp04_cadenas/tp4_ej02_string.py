texto = input("Ingrese un texto para centrar: ")

cant_espacios = (80 - len(texto)) // 2
texto = " " * cant_espacios + texto

print(texto)
import re
frase = input("Ingrese una frase: ")
sin_repetidos = list(set(re.split(r"[ ./:;,]", frase)))
sin_repetidos.sort(key=len)
print(" ".join(sin_repetidos))
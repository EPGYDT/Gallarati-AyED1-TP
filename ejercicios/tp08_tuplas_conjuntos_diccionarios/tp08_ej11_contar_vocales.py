def contarvocales(cadena: str):
    diccionario = dict()
    for letra in cadena.lower():
        if letra in "aeiou":
            if letra in diccionario:
                diccionario[letra.lower()] += 1

            else:
                diccionario[letra.lower()] = 1


    for c, v in sorted(diccionario.items()):
        print(f"Vocal: {c}     Cant. apariciones: {v}")
    if len(diccionario) < 5:
        print("El resto de vocales no aparecen")

cadena = input("Ingrese un texto para verificar cuantas vocales tiene: ")
contarvocales(cadena)
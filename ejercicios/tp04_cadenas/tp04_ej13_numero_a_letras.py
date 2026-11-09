"""
Muchas aplicaciones financieras requieren que los números sean expresados también en letras.
Por ejemplo, el número 2153 puede escribirse como "dos mil ciento cincuenta y tres".
Escribir un programa que utilice una función para convertir un
número entero entre 0 y 1 billón (1.000.000.000.000) a letras. ¿En qué cambiaría
la función si también aceptara números negativos? ¿Y números con decimales?
"""




def calcular_numero(numero):
    tres_cifras = 0
    dos_cifras = 0
    una_cifra = 0
    if numero // 100 > 0:
        tres_cifras = numero // 100
        numero %= 100

    if numero // 10 > 0:
        dos_cifras = numero // 10
        numero %= 10

    if numero // 1 > 0:
        una_cifra = numero // 1
        numero %= 1

    return tres_cifras, dos_cifras, una_cifra

def numero_a_letras(numero):
    mono = ("uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve")
    dieces = (
        "once",
        "doce",
        "trece",
        "catorce",
        "quince",
        "dieciseis",
        "diecisiete",
        "dieciocho",
        "diecinueve",
    )
    decenas = (
        "diez",
        "veinte",
        "treinta",
        "cuarenta",
        "cincuenta",
        "sesenta",
        "setenta",
        "ochenta",
        "noventa",
    )
    centenas = (
        "cien",
        "doscientos",
        "trescientos",
        "cuatrocientos",
        "quinientos",
        "seiscientos",
        "setecientos",
        "ochocientos",
        "novecientos",
    )
    miles = "mil"
    millones = ("millon", "millones")
    billones = "billon"


    texto = ""
    resto = numero
    if resto // 1_000_000_000_000 > 0:
        resto %= 1_000_000_000_000
        texto += "Un " +  billones + " "

    if resto // 1_000_000_000 > 0:
        saltar_unidad = False
        cant = resto // 1_000_000_000
        resto %= 1_000_000_000

        if cant == 1:
            tres_cifras, dos_cifras, una_cifra= 0, 0, 0
            texto += miles + " "

        else:
            tres_cifras, dos_cifras, una_cifra = calcular_numero(cant)

        if tres_cifras != 0:
            if tres_cifras == 1 and (dos_cifras > 0 or una_cifra > 0):
                texto += "ciento" + " "
            else: 
                texto += centenas[tres_cifras - 1] + " "

        if dos_cifras != 0:
            if dos_cifras == 2 and una_cifra != 0:
                texto += "".join(["veinti", mono[una_cifra - 1], " "])
                saltar_unidad = True

            elif dos_cifras == 1 and una_cifra != 0:
                texto += dieces[una_cifra-1] + " "
                saltar_unidad = True

            else:
                
                texto += decenas[dos_cifras - 1] + " "

        if una_cifra != 0 and saltar_unidad == False:
            if dos_cifras > 0:
                texto += "y" + " "
            texto += mono[una_cifra - 1] + " "

        texto += miles + " " + millones[1] + " "


    if resto // 1_000_000 > 0:
        saltar_unidad = False
        saltar_millones = False
        cant = resto // 1_000_000
        resto %= 1_000_000

        if cant == 1:
            tres_cifras, dos_cifras, una_cifra = 0, 0, 0
            saltar_unidad = True
            saltar_millones = True
            texto += " ".join(["un", millones[0], " "])

        else:
            tres_cifras, dos_cifras, una_cifra = calcular_numero(cant)

        if tres_cifras != 0:
            if tres_cifras == 1 and (dos_cifras > 0 or una_cifra > 0):
                texto += "ciento" + " "
            else: 
                texto += centenas[tres_cifras - 1] + " "

        if dos_cifras != 0:
            if dos_cifras == 2 and una_cifra != 0:
                texto += "".join(["veinti", mono[una_cifra - 1], " "])
                saltar_unidad = True

            elif dos_cifras == 1 and una_cifra != 0:
                texto += dieces[una_cifra-1] + " "
                saltar_unidad = True

            else:
                texto += decenas[dos_cifras - 1] + " "

        if una_cifra != 0 and saltar_unidad == False:
            if dos_cifras > 0:
                texto += "y" + " "
            texto += mono[una_cifra - 1] + " "

        if saltar_millones == False:
            texto += millones[1] + " "


    if resto // 1_000 > 0:
        saltar_unidad = False
        cant = resto // 1_000
        resto %= 1_000

        if cant == 1:
            tres_cifras, dos_cifras, una_cifra = 0, 0, 0
            saltar_unidad = True
            texto += miles + " "

        else:
            tres_cifras, dos_cifras, una_cifra = calcular_numero(cant)

        if tres_cifras != 0:
            if tres_cifras == 1 and (dos_cifras > 0 or una_cifra > 0):
                texto += "ciento" + " "
            else:
                texto += centenas[tres_cifras - 1] + " "

        if dos_cifras != 0:
            if dos_cifras == 2 and una_cifra != 0:
                texto += "".join(["veinti", mono[una_cifra - 1], " "])
                saltar_unidad = True

            elif dos_cifras == 1 and una_cifra != 0:
                texto += dieces[una_cifra-1] + " "
                saltar_unidad = True

            else:
                texto += decenas[dos_cifras - 1] + " "

        if una_cifra != 0 and saltar_unidad == False:
            if dos_cifras > 0:
                texto += "y" + " "
            texto += mono[una_cifra - 1] + " "

        if cant != 1:
            texto += miles + " "


    if resto // 1 > 0:
        saltar_unidad = False
        cant = resto // 1
        resto %= 1

        if cant == 1:
            tres_cifras, dos_cifras, una_cifra = 0, 0, 1

        else:
            tres_cifras, dos_cifras, una_cifra = calcular_numero(cant)

        if tres_cifras != 0:
            if tres_cifras == 1 and (dos_cifras > 0 or una_cifra > 0):
                texto += "ciento" + " "
            else: 
                texto += centenas[tres_cifras - 1] + " "


        if dos_cifras != 0:
            if dos_cifras == 2 and una_cifra != 0:
                texto += "".join(["veinti", mono[una_cifra - 1], " "])
                saltar_unidad = True

            elif dos_cifras == 1 and una_cifra != 0:
                texto += dieces[una_cifra-1] + " "
                saltar_unidad = True

            else:
                texto += decenas[dos_cifras - 1] + " "

        if una_cifra != 0 and saltar_unidad == False:
            if dos_cifras > 0:
                texto += "y "
            texto += mono[una_cifra - 1] + " "

    return texto


numero = int(input("Ingrese un numero: "))
print(numero_a_letras(numero))
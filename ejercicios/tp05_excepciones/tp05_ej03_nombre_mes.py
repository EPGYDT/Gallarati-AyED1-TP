def encontrar_mes(numero):
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Spetiembre", "Octubre", "Noviembre", "Diciembre")
    try:
        if numero > 12 or numero < 1:
            raise IndexError
        return meses[numero-1]
    
    except IndexError:
        return ""

while True:
    try:
        mes = int(input("Ingrese el numero del mes: "))

    except:
        print("Ingrese un numero entero.\n")

    else:
        print(encontrar_mes(mes))
        break
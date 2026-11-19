def encontrar_mes(numero):
    """
    Contrato:
        - Obtiene el nombre de un mes a partir de su numero.
    Pre:
        - Recibe un numero entero.
    Post:
        - Devuelve el nombre correspondiente si esta entre 1 y 12.
        - Devuelve una cadena vacia si el numero no corresponde a un mes.
    """
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
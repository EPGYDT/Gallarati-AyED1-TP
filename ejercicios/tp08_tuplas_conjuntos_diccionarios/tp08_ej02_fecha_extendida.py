def convertir_fecha_extendida(fecha: tuple[int, int, int]) -> str:
    """
    Contrato:
        - Convierte una fecha numerica en una de texto.
    Pre:
        - Recibe una tupla con 3 enteros que representan la fecha que se quiere convertir.
    Post:
        - Retorna una cadena que indica la fecha en texto.
        - Si el año ingresado es de 2 digitos o menor, se le suman años en base a un año de corte.
    """
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

    ano_corte = 26
    if fecha[2] < 100:
        if fecha[2] > ano_corte:
            fecha[2] += 1900
        else:
            fecha[2] += 2000

    return f"{fecha[0]} de {meses[fecha[1]-1]} de {fecha[2]}"
    



print("El año de corte es 26 (1927-2026)\n")
dia = int(input("Ingrese el numero de dia: "))
mes = int(input("Ingrese el numero de mes: "))
ano = int(input("Ingrese el numero de año: "))

fecha = (dia, mes, ano)

print(convertir_fecha_extendida(fecha))
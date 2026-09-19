def informar_cantidad(socios: list[int]) -> None:
    """
    Muestra cuantas veces ingreso cada socio al club.
    Pre: Recibe la lista con todos los ingresos de los socios.
    Post: No retorna nada, hace un print por cada socio indicando su numero de ingresos.
    """
    repetidos = []
    for e in socios:
        if e not in repetidos:
            repetidos.append(e)
            print(f"Nro Socio: {e}      Cant ingresos: {socios.count(e)}")



def eliminar_socios(socios: list[int], eliminado: int) -> None:
    """
    Da de baja a un socio de el sistema.
    Pre: Recibe la lista con todos los numeros de socios y el numero de socio que se dara de baja.
    Post: No retorna nada, solo actualiza la lista y hcae un print.
    """
    eliminados = socios.count(eliminado)
    socios[:] = [socio for socio in socios if socio != eliminado]
    print(f"Se eliminaron {eliminados} ingresos del socio {eliminado}.")



socios = []
while True:
    num_socio = int(input("Ingrese el numero de el socio (-1 para salir): "))
    if 99_999 >= num_socio >= 10_000:
        socios.append(num_socio)

    elif num_socio == -1:
        break

    else:
        print("Error, numero de socio invalido, intente nuevamente.")

informar_cantidad(socios)

while True:
    numero = int(input("Ingrese el numero de socio que se quiere dar de baja: "))
    if numero in socios:
        break
    else:
        print("Error, no hay ningun socio con ese numero.")
eliminar_socios(socios, numero)

informar_cantidad(socios)
def calc_vuelto(costo, pago):
    """
    Calcula el vuelto que debe devolver el cajero en la menor cantidad de billetes
    Pre: Recibe dos enteros positivos (costo de compra y cantidad de pago).
    Post: Retorna La cantidad de billetes mas optima de vuelto, o imprime un mensaje en caso de pagar menos o con lo justo.
    """
    assert isinstance(costo, int) and isinstance(pago, int), "El costo y el pago deben ser numeros enteros."
    assert costo > 0 and pago > 0, "El costo y el pago deben ser positivos."

    if pago > costo:
        vuelto = pago - costo
        if vuelto // 5000 > 0:
            cinco_mil = vuelto // 5000
            vuelto %= 5000
            print(f"Billetes de 5000: {cinco_mil}")

        if vuelto // 1000 > 0:
            mil = vuelto // 1000
            vuelto %= 1000
            print(f"Billetes de 1000: {mil}")

        if vuelto // 500 > 0:
            quinientos = vuelto // 500
            vuelto %= 500
            print(f"Billetes de 500: {quinientos}")

        if vuelto // 200 > 0:
            doscientos = vuelto // 200
            vuelto %= 200
            print(f"Billetes de 200: {doscientos}")

        if vuelto // 100 > 0:
            cien = vuelto // 100
            vuelto %= 100
            print(f"Billetes de 100: {cien}")

        if vuelto // 50 > 0:
            cincuenta = vuelto // 50
            vuelto %= 50
            print(f"Billetes de 50: {cincuenta}")

        if vuelto // 10 > 0:
            diez = vuelto // 10
            vuelto %= 10
            print(f"Billetes de 10: {diez}")

        if vuelto > 0:
            print(f"sobran {vuelto}$ pesos que se dan en caramelos ;)")

    elif pago == costo:
        print("no se debe dar vuelto ya que el cliente pago con lo justo")

    else:
        print("El dinero no es suficiente para cubrir el gasto de la compra :(")

costo = 0
pago = 0


while costo < 10:
    costo = int(input("Ingrese el costo de la compra: "))

while pago <= 0:
    pago = int(input("Ingrese el monto que pago el cliente: "))

calc_vuelto(costo, pago)

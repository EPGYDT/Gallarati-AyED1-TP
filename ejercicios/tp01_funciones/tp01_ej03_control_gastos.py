#EJ 3


def controlar_gastos(viajes: int, costo: int):
    """
    Realiza un control de gastos de viajes.
    Pre: Recibe dos numeros enteros positivos, la cantidad de viajes, y el costo base de un viaje.
    Post: devuelve el total de los gastos aplicando los descuentos.
    """
    assert isinstance(viajes, int) and isinstance(costo, int), "Ambos numeros deben ser enteros." 
    assert viajes > 0 and costo > 0, "Ambos numeros deben ser positivos."

    total_gastado = 0

    if viajes > 0 and costo > 0:
        if viajes <= 20:
            for i in range (viajes):
                total_gastado += costo

            return total_gastado

        elif viajes <= 30:
            for i in range (viajes):
                if i < 20:
                    total_gastado += costo

                else:
                    total_gastado += costo / 100 * 80

            return total_gastado

        elif viajes <= 40:
            for i in range (viajes):
                if i < 20:
                    total_gastado += costo

                elif i < 30:
                    total_gastado += costo / 100 * 80

                else:
                    total_gastado += costo / 100 * 70

            return total_gastado

        else:
            for i in range (viajes):
                if i < 20:
                    total_gastado += costo

                elif i < 30:
                    total_gastado += costo / 100 * 80

                elif i < 40:
                    total_gastado += costo / 100 * 70

                else:
                    total_gastado += costo / 100 * 60

            return total_gastado

    else:
        return False


print(controlar_gastos(90, 1000))
print(controlar_gastos(20, 1000))
print(controlar_gastos(45, 1000))
print(controlar_gastos(2, 1000))
print(controlar_gastos(5, 1000))
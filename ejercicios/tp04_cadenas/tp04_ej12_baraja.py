palos = ("oros", "bastos", "espadas", "copas")
comodines = ("comodin-1", "comodin-2")
cartas = [carta for carta in range(1, 13)]
mazo = [f"{palo} {carta}" for palo in palos for carta in cartas]

for i,carta in enumerate(mazo):
    if carta.startswith(mazo[i-1][:3]):
        print(f"{carta} ", end="")
    else:
        print(f"\n{carta} ", end="")
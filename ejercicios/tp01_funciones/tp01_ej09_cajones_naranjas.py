from random import randint


def contar_naranjas(cant_naranjas: int):
    """
    Genera el peso de las naranjas y cuenta los diferentes tipos.
    Pre: Recibe la cantidad de naranjas cosechadas como un numero entero positivo.
    Post: Devuelbe una tupla con numeros enteros positivos.
    """
    nar_act = 0
    nar_sueltas = 0
    nar_jugo = 0
    peso_total = 0
    for i in range(cant_naranjas):
        nar_act = randint(150, 350)
        
        if 300 >= nar_act >= 200:
            nar_sueltas += 1
            peso_total += nar_act
            
            
        else:
            nar_jugo += 1
    

            
    
    
    return nar_sueltas, nar_jugo, peso_total

def contar_camiones(peso: int) -> int:
    """
    Cuenta la cantidad de camiones de para llevar los cajones.
    Pre: Recibe el peso de las naranjas como un entero positivo.
    Post: Devuelve un entero positivo que representa la cantidad de camiones.
    """
    camiones = peso // 500_000
    peso_restante = peso % 500_000
    
    if peso_restante >= 400_000:
        camiones += 1

    return camiones



def contar_cajones(naranjas_sueltas):
    cajones = naranjas_sueltas // 100
    naranjas_sueltas = naranjas_sueltas % 100
    
    return naranjas_sueltas, cajones



def main():
    naranjas = 0
    while naranjas <= 0:
        naranjas = int(input("Ingrese la cantidad de naranjas cosechadas: "))
    
    naranjas_sueltas, naranjas_jugo, peso = contar_naranjas(naranjas)
    naranjas_sueltas, cajones = contar_cajones(naranjas_sueltas)
    
    cant_camiones = contar_camiones(peso)

    if cant_camiones > 0:
        print(f"Cant. camiones: {cant_camiones}")
        print(f"Cant. cajones: {cajones}")

        if naranjas_sueltas > 0:
            print(f"Cant. naranjas que no forman parte de un cajon completo: {naranjas_sueltas}")
        else:
            print("No hubieron naranjas sueltas.")


    else:
        print("No se pudo cubrir lo minimo necesario para que un camion transporte las naranjas.")

    if naranjas_jugo > 0:
        print(f"Cant. naranjas para jugo: {naranjas_jugo}")

    else:
        print("No hubieron naranjas que para jugo.")



main()
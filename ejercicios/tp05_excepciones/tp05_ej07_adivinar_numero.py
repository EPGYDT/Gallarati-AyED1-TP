from random import randint

numero_aleatorio = randint(1, 500)



print("Adivina el numero del 1 al 500!!!")

intentos = 0
while True:
    try:
        numero = int(input("Ingrese un numero para intentar adivinar: "))
        if numero > 500 or numero < 1:
            raise ValueError

    except ValueError:
        print("Error, valor incorrecto, se debe ingresar un numero entero entre 1 y 500.")

    else:
        if numero != numero_aleatorio:

            if numero > numero_aleatorio:
                print("El numero que ingresaste es mayor a mi numero.")

            else:
                print("El numero que ingresaste es menor a mi numero.")

        else:
            print(f"Acertaste!!! mi numero era el {numero_aleatorio}")
            break
    finally:
        intentos += 1

print(f"Cantidad de intentos que te tomo adivinar: {intentos}")
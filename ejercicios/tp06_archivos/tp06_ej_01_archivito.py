import json

try:
    with open("personas.csv", "rt", encoding="utf-8-sig") as personas:
        for nombres in personas:
            try:
                apellido, nombre = nombres.split(",", 1)
                apellido = apellido.strip()
                nombre = nombre.strip()
            except ValueError:
                continue

            if apellido.endswith("ian"):

                try:
                    with open("ARMENIA.txt", "at", encoding="utf-8") as armenia:
                        armenia.write(f"Apellido: {apellido}     Nombre: {nombre}\n")

                except:
                    print("Error akhper")

            elif apellido.endswith("ini"):

                try:
                    with open("ITALIA.txt", "at", encoding="utf-8") as italia:
                        italia.write(f"Apellido: {apellido}     Nombre: {nombre}\n")

                except:
                    print("Error squalo")

            elif apellido.endswith("ez"):

                try:
                    with open("ESPAÑA.txt", "at", encoding="utf-8") as espania:
                        espania.write(f"Apellido: {apellido}     Nombre: {nombre}\n")

                except:
                    print("Error brochacho")


except OSError:
    print("Hubo un error con el archivo")

finally:
    print("bye, bye")




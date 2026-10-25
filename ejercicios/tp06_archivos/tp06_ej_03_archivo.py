"""
3. Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los
próximos Juegos Panamericanos. Para eso encargó la realización de un programa
que incluya las siguientes funciones:
"""


def grabar_rango_alturas():
    """
    Graba en un archivo las alturas de los atletas de distintas
    disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una
    línea distinta.
    """
    deportes = {}
    while True:
        deporte = input("Ingrese el nombre del deporte (presione ENTER para salir): ")
        if not deporte:
            break
        else:
            deporte = deporte.strip().capitalize()
        if deporte not in deportes:
            deportes[deporte] = []

        while True:
            try:
                altura = float(
                    input(
                        f"Ingrese la altura del deportista de {deporte} (ENTER para salir): "
                    )
                )

            except ValueError:
                break

            else:
                if altura > 0:
                    deportes[deporte].append(altura)
                else:
                    print("\n La altura debe se un numero positivo.\n")

    try:
        with open("deportes.txt", "wt", encoding="utf-8") as archivo:
            for c, v in deportes.items():
                archivo.write(f"Deporte: {c}\n")
                for estatura in v:
                    print(estatura)
                    archivo.write(f"{estatura}\n")
                archivo.write("\n")

    except OSError:
        print("Hubo un error al escribir el archivo.")


def grabar_promedio():
    """
    Graba en un archivo los promedios de las alturas de los atletas,
    leyendo los datos del archivo generado en el paso anterior. La disciplina y el
    promedio deben grabarse en líneas diferentes.

    """
    try:
        with open("deportes.txt", "rt", encoding="utf-8") as archivo, open(
            "promedios.txt", "wt", encoding="utf-8"
        ) as destino:
            acumulador = 0
            cant = 0

            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue

                if linea.startswith("Deporte"):
                    if cant > 0:
                        destino.write(f"{acumulador / cant:.2f}\n")
                    acumulador = 0
                    cant = 0
                    destino.write(linea.replace("Deporte: ", "").strip() + "\n")

                else:
                    acumulador += float(linea)
                    cant += 1

            if cant > 0:
                destino.write(f"{acumulador / cant:.2f}\n")

    except OSError:
        print("Hubo un error al escribir el archivo.")

    finally:
        print("Finalizo el trabajo de promedios.")


def promedio_global():
    try:
        with open("deportes.txt", "rt", encoding="utf-8") as archivo:
            acumulador = 0
            cant = 0
            for linea in archivo:
                linea = linea.strip()

                if not linea:
                    continue

                try:
                    altura = float(linea)
                    acumulador += altura
                    cant += 1
                except ValueError:
                    continue

            if cant > 0:
                return acumulador / cant

            else:
                return 0

    except OSError:
        print("Hubo un problema con el promedio global")


def mostrar_mas_altos():
    promedio = promedio_global()

    if promedio == 0:
        print("No hay alturas para calcular el promedio.")
        return

    print(f"Promedio global: {promedio:.2f}")

    try:
        with open("deportes.txt", "rt", encoding="utf-8") as archivo:

            for linea in archivo:
                linea = linea.strip()

                if not linea:
                    continue

                elif linea.startswith("Deporte:"):
                    print(f"\n{linea}")

                else:
                    altura = float(linea)
                    if altura > promedio:
                        print(linea)

    except OSError:
        print()


grabar_rango_alturas()
grabar_promedio()
mostrar_mas_altos()

def mostrar_listado(pacientes: tuple[list[int], list[str]]) -> None:
    """
    Muestra un listado de todos los pacientes que fueron atendidos por turno
    y otro con todos los atendidos por urgencia
    Pre: Recibe la tupla con los datos de los pacientes.
    Post: no retorna nada, solo realiza prints.
    """
    print("Pacientes por turno: \n")
    for i, paciente in enumerate(pacientes[0]):
        if pacientes[1][i] == "1":
            print(f"Paciente de turno: {paciente}")

    print("\n\nPacientes por urgencia:\n")

    for i, paciente in enumerate(pacientes[0]):
        if pacientes[1][i] == "0":
            print(f"Paciente por urgencia: {paciente}")



def informar_afiliado(pacientes: tuple[list[int], list[str]], paciente: int) -> None:
    """
    Informa cuantas veces un paciente solicitado fue atendido por turno
    y cuantas veces por urgencia.
    Pre: Recibe la tupla con los datos de los pacientes y el numero del
    paciente del que se quiere el informe.
    Post: No retorna nada, solo realiza prints.
    """
    turnos = 0
    urgencia = 0
    for i, e in enumerate(pacientes[0]):
        if e == paciente:
            if pacientes[1][i] == "0":
                urgencia += 1

            else:
                turnos += 1

    print(f"Veces atendido por turno: {turnos}")
    print(f"Veces atendido por urgencia: {urgencia}")
            


pacientes = ([], [])

while True:
    numero = int(input("Ingrese un numero de afiliado (-1 para salir): "))
    if numero >= 1000 and numero <= 9999:
        pacientes[0].append(numero)
        while True:
            estado = input("Ingrese el estado del paciente (0. Urgencia | 1. Turno): ")
            match estado:
                case "0":
                    pacientes[1].append(estado)
                    print("El paciente se registro exitosamente por urgencia.")
                    break

                case "1":
                    pacientes[1].append(estado)
                    print("El paciente se registro exitosamente por turno.")
                    break

                case _:
                    print("Error, ingrese una opcion valida.")

    elif numero == -1:
        print("Adios!")
        break

    else:
        print("Error, ingrese un numero valido.")


mostrar_listado(pacientes)

while True:
    paciente = int(input("Ingrese el numero de paciente para recibir el informe de  "))
    if paciente in pacientes[0]:
        informar_afiliado(pacientes, paciente)

    elif paciente == -1:
        print("Adios!")
        break
    else:
        print("Error, ingrese un numero de paciente valido.\n")
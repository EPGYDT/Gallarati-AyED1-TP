def separar_email(email: str) -> tuple:
    """
    Contrato:
        - Separa un email en nombre de usuario y dominios.
    Pre:
        - Recibe una cadena con formato email.
    Post:
        - Devuelve una tupla con las partes separadas por @ y puntos.
    """
    nombre, resto = email.split("@")
    resto = resto.split(".")
    if len(resto) == 3:
        return (nombre, resto[0], resto[1], resto[2])
        

    return (nombre, resto[0], resto[1])


email = "pablo@gmail.com.ar"
tupla = separar_email(email)
for e in tupla:
    print(e)
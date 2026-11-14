def separar_email(email: str) -> tuple:
    nombre, resto = email.split("@")
    resto = resto.split(".")
    if len(resto) == 3:
        return (nombre, resto[0], resto[1], resto[2])
        

    return (nombre, resto[0], resto[1])


email = "pablo@gmail.com.ar"
tupla = separar_email(email)
for e in tupla:
    print(e)
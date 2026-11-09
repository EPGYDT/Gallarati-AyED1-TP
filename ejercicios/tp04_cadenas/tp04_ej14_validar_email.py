import re


def validar_correo(texto):
    patron = r"[A-Za-z0-9]+@[A-Za-z0-9._+-]{1,}\.(com|com\.ar)"
    return bool(re.fullmatch(patron, texto))
    
while True:
    email = input("Ingrese su direccion de correo electronico: ")
    validacion = validar_correo(email)
    if validacion:
        break

print(email)
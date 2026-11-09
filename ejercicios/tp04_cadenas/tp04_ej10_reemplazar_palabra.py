def reemplazar_palabra(cadena: str, palabra: str, reemplazo: str) -> None:
    """
    Contrato:
        - 
    
    Pre:
        - 
    
    Post:
        -
    """
    contador = 0
    while True:
        if palabra in cadena:
            cadena = cadena.replace(palabra, reemplazo, 1)
            contador += 1

        else:
            break
    
    if contador != 0:
        print(f"\nTexto con la palabra {palabra} reemplazada por la palabra {reemplazo}:")
        print(cadena)
        print(f"Cantidad de veces reemplazada: {contador}")
    else:
        print(f"La palabra {palabra}, no  aparece nunca en el texto.")


texto = "Python es facil. Python es bueno. Python es divertido"
palabra = "Python"
reemplazo = "Undertale"
print(f"texto: {texto}")
print(f"Palabra a reemplazar: {palabra}")
print(f"Palabra que va a reemplazarla: {reemplazo}")
reemplazar_palabra(texto, palabra, reemplazo)
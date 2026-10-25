import json

def convertir_a_json(nombre_archivo: str):
    salida = ""
    try:
        with open(nombre_archivo, "rt", encoding="utf-8") as archivo:
            nacionalidades = []
            apellidos = {"ini": "italia", "ian": "armenia", "ez": "españa"}
            
            for nombres in archivo:
                try:
                    apellido, nombre = nombres.split(",", 1)
                    apellido = apellido.strip()
                    nombre = nombre.strip()
                except ValueError:
                    continue

                for c, v in apellidos.items():
                    if apellido.endswith(c):
                        nacionalidades.append({f"{v}.txt": f"{apellido}, {nombre}"})

    except Exception as e:
        print(e)

    else:
        

        try:
            with open("son.json", 'wt', encoding='utf-8') as jason:
                salida = json.dump(nacionalidades, jason, indent=4, ensure_ascii=False)

        except OSError:
            print("Hubo un error con el jason")


archivo = "C:/Users/agustin gallarati/Documents/Gallarati-AyED1-TP/ejercicios/tp06_archivos/personas.csv"
convertir_a_json(archivo)

def verif_biciesto(ano: int) -> bool:
    """
    Verifica si el año es o no biciesto.
    Pre: El numero debe ser un entero positivo
    Post: devuelve un booleano en base a si el ano es biciesto o no.
    """
    assert isinstance(ano, int) and ano > 0, "El año debe ser un numero entero positivo"
    
    if ano % 400 == 0:
        return True

    elif ano % 4 == 0 and ano % 100 != 0:
        return True

    else:
        return False


def diadelasemana(dia,mes,ano):
    if mes < 3:
        mes = mes + 10
        ano = ano - 1
    else:
        mes = mes - 2
    siglo = ano // 100
    año2 = ano % 100
    diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

dia = 1
mes = 3
ano = 2008

match mes:
    case 1:
        print(f"Enero {ano}")
        dias = 31
        
    case 2:
        print(f"febrero {ano}")
        if verif_biciesto(ano):
            dias = 29
        else:
            dias = 28
        
    case 3:
        print(f"Marzo {ano}")
        dias = 31
        
    case 4:
        print(f"Abril {ano}")
        dias = 30
        
    case 5:
        print(f"Mayo {ano}")
        dias = 31
        
    case 6:
        print(f"Junio {ano}")
        dias = 30
        
    case 7:
        print(f"Julio {ano}")
        dias = 31
        
    case 8:
        print(f"Agosto {ano}")
        dias = 31
        
    case 9:
        print(f"Septiembre {ano}")
        dias = 30
        
    case 10:
        print(f"Octubre {ano}")
        dias = 31
        
    case 11:
        print(f"Noviembre {ano}")
        dias = 30
        
    case 12:
        print(f"Diciembre {ano}")
        dias = 31
        
        
print("Dom  Lun  Mar  Mie  Jue  Vie  Sab")
a = 1
        
dia_actual = diadelasemana(dia, mes, ano)

dias_meses = list(range(1, 31))
print(dias_meses)

for i in range(dia_actual , dias):
    if a + 7 <= dias:
        print(f"{a}    {a+1}    {a+2}    {a+3}    {a+4}    {a+5}    {a+6}")
        a += 7
        
    elif a < dias:
        print(a)
        a += 1
    else:
        break
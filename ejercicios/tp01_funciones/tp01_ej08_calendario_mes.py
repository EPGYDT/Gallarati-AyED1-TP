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

if mes in (1, 3, 5, 7, 8, 10, 12):
    dias = 31

elif mes in (4, 6, 9, 11):
    dias = 30

else:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        dias = 29
    else:
        dias = 28
    
print("Dom  Lun  Mar  Mie  Jue  Vie  Sab")

        
dia_actual = diadelasemana(dia, mes, ano)

match dia_actual:
    case 0:
        print("001  002  003  004  005  006  007")
        n = 8
    case 1:
        print("     001  002  003  004  005  006")
        n = 7

    case 2:
        print("          001  002  003  004  005")
        n = 6

    case 3:
        print("               001  002  003  004")
        n = 5
    
    case 4:
        print("                    001  002  003")
        n = 4

    case 5:
        print("                         001  002")
        n = 3

    case _:
        print("                              001")
        n = 2
    
    




for i in range(4):

    print(f"{n}    {n+1}    {n+2}    {n+3}    {n+4}    {n+5}    {n+6}")
    n += 7
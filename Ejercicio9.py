num = int(input("Escribe un numero:"))


def esPrimo(num):
    if num < 1:
       return False
    elif num == 2:
       return True
    for n in range(2,num):
        if num % n == 0:
           return False
        else:
           return True
def validacion():
    resultado = esPrimo(num)
    if resultado is True:
        print("Es primo")
    else:
        print("No es primo")          


validacion()
    
        


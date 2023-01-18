num1 = int(input("Introduce un numero:"))
num2 = int(input("Introduce otro numero:"))

opcion = input("""Selecciona una de las opciones: 
                        0: Salir
                        1: Suma
                        2: Resta
                        """)
def suma():
    resultado = num1 + num2
    print(resultado)


def resta():
    resultado = num1 - num2
    print(resultado)

while opcion != 0:
   match opcion:
        case "1":
            suma()
            continue
        case "2":
            resta()
            break

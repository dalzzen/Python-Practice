#Suma de los numeros anteriores a un numero dado por el usario
numero = int(input("Escriba un numero:"))
suma: int = 0
for x in range(1,numero):
    suma = x + suma
    x+1
print(suma)
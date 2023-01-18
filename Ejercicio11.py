#Escribí un programa que, dado un número entero por el usuario (guardado como int), muestre la suma de todos sus dígitos. 
#Recordá que vas a necesitar obtener cada uno de los dígitos por separado para poder sumarlos entre sí.
numero = int(input("Escribe un numero:"))
suma: int = 0
lista_numero = [int(x) for x in str(numero)]
for x in lista_numero:
    suma = suma + x
    x+1
print(lista_numero)
print(suma)
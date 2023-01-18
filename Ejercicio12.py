#Escribí una función llamada esPar que reciba como parámetro un número y retorne True si el número es par ó False 
#si es impar. Utilizar esta función en un programa que solicite al usuario el ingreso de 10 números y que luego muestre, 
#por separado, la suma de todos los pares y la suma de todos los impares.

#Definiendo funcion esPar
def esPar(num):
    if num % 2 == 0:
        return True
    else:
        return False
#Definiendo funcion suma de lista que suma los valores que hay dentro de la lista
def sumaLista(lista):
    resultado_suma:int = 0
    for x in lista:
        resultado_suma = x + resultado_suma
    return resultado_suma
#Creacion de lista de numeros y llenado de lista 
lista_numeros = []
while len(lista_numeros) < 10:     
    numero = input("Escriba un numero:")
    lista_numeros.append(int(numero))
#Creacion de listas que se usaran para numeros pares e impares
numeros_pares = []
numeros_impares = []
#Llenado de listas dependiendo de si el valor es par o impar
for x in lista_numeros:
    if esPar(x) is True:
        numeros_pares.append(int(x))
    else:
        numeros_impares.append(int(x))

print("La suma de numeros impares es:",sumaLista(numeros_impares))
print("La suma de numeros pares es:",sumaLista(numeros_pares))

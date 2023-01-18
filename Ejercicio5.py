#Escribí un programa que, dada una cadena de texto por el usuario, 
#imprima True si la cantidad de caracteres en la cadena es un número par, o False si no lo es.
texto = str(input("Escriba una cadena de texto:"))
cantidad_caracteres = len(texto)
if cantidad_caracteres % 2 == 0:
    print(True)
else:
    print(False)

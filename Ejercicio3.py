#Escribí un programa que solicite al usuario dos números y los almacene en dos variables. 
#En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla.
#A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable. 
#Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.
n1 = float(input("Ingrese el valor del primer numero: "))
n2 = float(input("Ingrese el valor del segundo numero: "))
suma = n1 + n2
print(suma)
n3 = float(input("Ingrese el valor del tercer numero: "))
multi = n3 * suma
print(multi)
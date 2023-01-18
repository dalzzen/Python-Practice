#Escribí un programa para pedir al usuario su nombre y luego el nombre de otra persona, 
#almacenando cada nombre en una variable. Luego mostrar en pantalla un valor de verdad que indique si: 
#los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra.
nombre1 = str(input("Escriba su nombre:"))
nombre2 = str(input("Escriba el nombre de otra persona:"))
if nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]:
 print(True)
else:
    print(False)

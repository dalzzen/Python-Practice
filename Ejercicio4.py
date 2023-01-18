#Escribí un programa que solicite al usuario el ingreso de una temperatura en escala Fahrenheit (debe permitir decimales) 
#y le muestre el equivalente en grados Celsius. La fórmula de conversión que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)_
temp_fahren = float(input("Ingrese la temperatura en grados Fahrenheit:"))
temp_celsius = (temp_fahren - 32) * 0.5556
print("La temperatura en grados Celsius es:", temp_celsius)
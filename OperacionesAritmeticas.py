import os
os.system('cls' if os.name == 'nt' else 'clear')

#OperacionesAritmeticas 
#suma
print("Ingrese el primer valor :")
a=int(input())
print("Ingrese el segundo valor :")
b=int(input())
print("La suma es: ",a+b)
#resta
print("La resta es: ",a-b)
#multiplicacion
print("La multiplicacion es: ",a*b)
#division
print("La division es: ",a/b)
#modulo
print("El modulo es: ",a%b) 
#potencia
print("La potencia es: ",a**b)
#division entera
print("La division entera es: ",a//b)
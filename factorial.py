import os
os.system('cls' if os.name == 'nt' else 'clear')

#Mostrar el factorial de un numero

n=int(input("Ingresa el numero que deseas que se muestre: "))

factorial=1
for i in range(1,n+1):
    factorial=factorial*i

print(factorial)


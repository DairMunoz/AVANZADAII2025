import os
os.system('cls' if os.name == 'nt' else 'clear')

#Mostrar tabla de multiplicar
print("TABLA DE MULTIPLICAR")
print()
n=int(input("Ingresa el numero que deseas que se muestre: "))

for i in range(1,11):
    print(n,"x",i,"=",n*i)
    
   
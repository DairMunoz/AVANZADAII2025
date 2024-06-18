import os 
os.system('cls' if os.name == 'nt' else 'clear')

mensaje="Ingrese un Texto:"
print(mensaje)
texto=input()


mensaje2="Ingrese tres letras a su eleccion:"
print(mensaje2)
letra1=input()
letra2=input()
letra3=input()

print(texto.replace(letra1,letra2).replace(letra2,letra3).replace(letra3,letra1))




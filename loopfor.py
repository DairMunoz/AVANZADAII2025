import os
os.system('cls' if os.name == 'nt' else 'clear')


for i in range(10):
    print(i)

 #range(inicio,fin,incremento)

for i in range(0,10,2):
    print(i)

    #ciclo for con una lista
    lista=["uno","dos","tres","cuatro","cinco"]

for item in lista:
    print(item)

       #invertir el orden de la lista
for item in reversed(lista):
    print(item)

    #ciclo for con una tupla
    tupla=("uno","dos","tres","cuatro","cinco")

 


for item in tupla:
    print(item)

    #ciclo for con un diccionario
    diccionario={"curso":"Python TOTAL",
                 "clase":"ciclos",
                 "temas":"for",
                 "duracion":"1 trimestre",
                 "profesor":"Dair"}

print(diccionario)
for llave in diccionario:
    print(llave,":",diccionario[llave])

    #invertir el orden del diccionario
for llave in reversed(diccionario):
    print(llave,":",diccionario[llave])

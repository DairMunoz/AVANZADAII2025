import os
os.system('cls' if os.name == 'nt' else 'clear')

lista_1 = ["C", "C++", "Python", "Java"]
lista_2 = ["PHP", "SQL", "Visual Basic"]
lista3=lista_1+lista_2
lista_4=["d", "a", "c", "b", "e"]
lista_5 = [5, 4, 7, 1, 9]
lista_6=lista_1+lista_5
lista_7=[True, False,]
#agregar elementos
lista_7.append(True)
#remover elementos
lista_7.pop(2)
#Ordenarlos de menor a mayor
lista_7.sort()
#Ordenarlos de mayor a menor
lista_7.reverse()



#print(lista_1[0], lista_2[0],)
#print(lista3)
#print(lista_6)
print(lista_7)


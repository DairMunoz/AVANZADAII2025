import os
os.system('cls' if os.name == 'nt' else 'clear')

mi_tupla=(1,"dos",[3.33,"cuatro","equis"],(5.0,6))

print(mi_tupla)
print(mi_tupla[0])
print(mi_tupla[3][1])
print(mi_tupla[2][2])

lista1=list(mi_tupla)
print(lista1)

#umpacking de tuplas (desempaquetamiento de tuplas)
a,b,c,d=mi_tupla
print(a)
print(b)
print(c)
print(d)

#tupla de pi,e,gravedad
pi, e, g = 3.14, 2.71, 9.81
print(pi)
print(e)
print(g)
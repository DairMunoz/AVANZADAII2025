import os
os.system('cls' if os.name == 'nt' else 'clear')

Nombres= [
{"id": 1, "name": "Derick Dair Muñoz Iraheta","Edad": 20},
{"id": 2, "name": "Jorge Arturo Vallecillo Espinoza","Edad": 18}, 
{"id": 3, "name": "Lucas Rodrido Bautista Juarez","Edad": 18},
{"id": 4, "name": "Jose David Mejia Mendoza ","Edad": 31},
{"id": 5, "name": "Kennet Andersson Martinez Varela","Edad": 21} ,    
{"id": 6, "name": "Tommy Jose Montufar Zuniga","Edad": 19},
{"id": 7, "name": "Angel Antonio Perez Rodriguez","Edad": 18},
{"id": 8, "name": "Jose Eduardo Sabillon Hurtado","Edad": 19},
{"id": 9, "name": "Diany Lisbeth Enamorado Fernandez","Edad": 19},
{"id": 10, "name": "Anderson jair Garcia Menjivar ","Edad": 19},
{"id": 11, "name": "Iliana Liceth Zuniga Enamorado","Edad": 18},
{"id": 12, "name": "Norman Bu","Edad": 25},
{"id": 13, "name": "Arnold Stanly Ford","Edad": 18},
{"id": 14, "name": "Walter Eduardo Rapalo Smith","Edad": 20},
{"id": 15, "name": "Edson Jhair Rios Coto","Edad": 26},

]

for valores in Nombres:
    print(valores["id"],"-",valores["name"],"=",valores["Edad"])
'''
Dadas las siguientes listas:
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
y considerando que la posición en la lista corresponde a la misma persona,
mostar el nombre de la persona más joven

'''

lista_edad = [25,36,18,23,45]
lista_nombre = ["Juan","Ana","Sol","Mario","Sonia"]
edad_minima = lista_edad[0]
#nombre_minimo = lista_nombre[0]

for i in range(len(lista_edad)):
    edad = lista_edad[i]
    nombre = lista_nombre[i]
    if edad < edad_minima :
        edad_minima = edad
        
        #print(f"La persona menor es: {nombre_minimo, edad}")
        print(f"NOMBRE: {nombre} - EDAD: {edad}")

    
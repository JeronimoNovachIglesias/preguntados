'''
Ejercicio 2:
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
adolescente (entre 13 y 17 años) o niño (menor a 13 años).

'''
edad = int(input("Ingrese su edad: "))

while edad:
    if edad >= 18:
        print("ES MAYOR DE EDAD")
        break
    elif edad >= 13 and edad <= 17:
        print("ES ADOLESCENTE")
        break
    else:
        print("ES UN NENE")
        break
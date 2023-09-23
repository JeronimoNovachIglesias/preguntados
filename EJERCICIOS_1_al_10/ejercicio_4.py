'''
Ejercicio 4:
Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
ser soltero.'

'''


lista_civil = ["Soltero, Casado, Divorciado"]


for i in range(len(lista_civil)):
    
    edad = int(input("Ingrese una edad:"))
    lista_civil = input("Ingrese su estado civil:")
    
    if edad < 18 and lista_civil != "Soltero":
        lista_civil = print("Es muy pequeño para NO ser soltero.")
    else:
        break
'''
Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
sueldo para esa persona.
'''
while True:
    nombre = input("Ingrese su nombre: ")
    sueldo = float(input("Ingrese su sueldo: "))

    aumento = sueldo * 1.10
    print (f"su aumento es de 10% y le queda un total de: {aumento:0.2f}")


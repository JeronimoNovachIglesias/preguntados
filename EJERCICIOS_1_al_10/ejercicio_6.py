'''
Ejercicio 6:
Utilizar For
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
mostrar el mayor.

'''
lista = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
maximo = [0]
for i in range(len(lista)):
    if lista[i] > maximo:
        maximo = lista[i]
        print(f"el numero mayor es: {maximo}")
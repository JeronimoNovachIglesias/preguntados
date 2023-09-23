'''
Ejercicio 3:
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos.

'''

mensaje = ""
numero = 0
lista_numeros = []
lista_pares = []
lista_impares = []
bandera_menor = False
bandera_mayor = False
numero_menor = 0
numero_mayor = 0
acumulador_positivo = 0
acumulador_negativo = 1



for i in range (5):
    numero = int(input("INGRESE UN NUMERO DISTINTO A 0: "))
    while numero == 0:
        numero = int(input("REINGRESE UN NUMERO DISTINTO A 0"))
    lista_numeros.append(numero)
    
for numero in lista_numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

contador_impares = len(lista_impares)
contador_pares = len(lista_pares)

mensaje += f"Se ingresaron {contador_pares} numeros pares\n"
mensaje += f"Se ingresaron {contador_impares} numeros impares\n"

for numero in lista_numeros:
    if bandera_menor == False or numero < numero_menor:
        numero_menor = numero
        bandera_menor = True

mensaje += f"El menor número ingresado es: {numero_menor}\n"

for numero in lista_pares:
    if bandera_mayor == False or numero > numero_mayor:
        numero_mayor = numero
        bandera_mayor = True
mensaje += f"El mayor numero par ingresado es: {numero_mayor}\n"


for numero in lista_numeros:
    if numero > 0:
        acumulador_positivo += numero
    else:
        acumulador_negativo *= numero

mensaje += f"La suma de los positivos es: {acumulador_positivo}\n"
mensaje += f"Producto de los negativos es: {acumulador_negativo}"


print(mensaje)





'''
contador_pares = 0
contador_impares = 0
numero = 0
bandera_menor = True
bandera_mayor = True
numero_menor = None
numero_mayor = 0
acumulador_positivo = 0
producto_negativos = 0
acumulador_negativo = 1
for i in range (5):
    numero = int(input("Ingrese 5 numeros enteros distintos de 0: "))

    while numero == 0:
        numero = int(input("Reingrese un numero distinto a 0"))

    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1

    if bandera_menor == True or numero < numero_menor :
        numero_menor = numero
        bandera_menor = False

    if numero % 2 == 0:
        if bandera_mayor == True or numero > numero_mayor:
            numero_mayor = numero
            bandera_mayor = False

    if numero > 0:
        acumulador_positivo += numero

    if numero < 0:
        acumulador_negativo *= numero

print(f"CANTIDAD DE IMPARES: {contador_impares}")
print(f"CANTIDAD DE PARES: {contador_pares}")
print(f"NUMERO MAYOR DE PARES: {numero_mayor}")       
print(f"NUMERO MENOR: {numero_menor}")
print(f"SUMA DE POSTIVOS: {acumulador_positivo}")
print(f"PRODUCTO DE LOS NEGATIVOS: {acumulador_negativo}")
'''
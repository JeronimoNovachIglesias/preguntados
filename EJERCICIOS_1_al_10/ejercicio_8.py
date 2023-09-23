'''
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
mostrar el número repetido

'''

lista = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]

numero_repetido = []

for i in range(len(lista)):
    for j in range(len(lista)):
        if i != j:
            if lista[i] == lista[j]:
                numero_repetido.append(lista[i])
        
print(numero_repetido)    
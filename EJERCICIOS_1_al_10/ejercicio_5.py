'''
Ejercicio 5:
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
por cada estadía como base, se pide el ingreso de una estación del
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
Plata/Córdoba) para vacacionar para poder calcular el precio final:
-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
descuento del 10% Mar del Plata tiene un descuento del 20%
-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
un aumento del 10% Mar del Plata tiene un aumento del 20%
-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
precio sin descuento.
Validar el ingreso de datos

'''
# Ejercicio 5:
# Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
# por cada estadía como base, se pide el ingreso de una estación del
# año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
# Plata/Córdoba) para vacacionar para poder calcular el precio final:
# -en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
# descuento del 10% Mar del Plata tiene un descuento del 20%
# -en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
# un aumento del 10% Mar del Plata tiene un aumento del 20%
# -en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
# aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
# precio sin descuento.
# Validar el ingreso de datos

mensaje = ""
estadia_base = 15000
estacion = input("Ingrese una estacion del año (Invierno, Verano, Otoño, Primavera):")
while estacion != "Invierno" and estacion != "Verano" and estacion != "Otoño" and estacion != "Primavera":
    estacion = input("Ingrese una estacion del año (Invierno, Verano, Otoño, Primavera):")

localidad = input("Ingrese una localidad (Bariloche, Cataratas, Mar del plata, Córdoba): ")
while localidad != "Bariloche" and localidad != "Cataratas" and localidad != "Mar del plata" and localidad != "Córdoba":
    localidad = input("Ingrese una localidad (Bariloche, Cataratas, Mar del plata, Córdoba): ")

aumento = 0
descuento = 0

if estacion == "Invierno":
    if localidad == "Bariloche":
        aumento = 1.2
    if localidad == "Córdoba":
        descuento = 0.9
    if localidad == "Mar del plata":
        descuento = 0.8

if estacion == "Verano":
    if localidad == "Bariloche":
        descuento = 0.8
    if localidad == "Mar del plata":
        aumento = 1.2
    else:
        aumento = 1.1

if estacion == "Otoño" or estacion == "Primavera":
    if localidad != "Córdoba":
        aumento = 1.1

if aumento != 0:
    precio_final = estadia_base * aumento
else:
    if descuento != 0:
        precio_final = estadia_base * descuento
    else:
        precio_final = estadia_base
        

print(f"El precio final a pagar es de: {precio_final}")
        
        
        
    
    


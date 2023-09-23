'''
La división de higiene está trabajando en un control de stock para productos sanitarios.  Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe  obtener los siguientes datos: 
1. El tipo (validar "barbijo", "jabón" o "alcohol") 
2. El precio: (validar entre 100 y 300) 
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000  unidades) 
4. La marca y el Fabricante. 
  
Se debe informar lo siguiente: 
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante. B. Del ítem con más unidades, el fabricante. 
C. Cuántas unidades de jabones hay en total. 




'''

#CARGA DE DATOS

lista = []
precio_mas_alto = 0
cantidad_unidades = ""
cantidad_fabricantes = ""
mensaje = ""
mensaje_2 = ""
mensaje_3 = ""
unidad_maxima = 0
fabricante_mayor = ""


for i in range (2):

    tipo = input("Ingrese un tipo de producto: barbijo / jabon / alcohol: ")
    while tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol":
        tipo = input("ERROR, Reingrese un producto valido: ")
    
    precio = input("Ingrese un precio. Entre $100 y $300: $")
    precio = int(precio)
    while precio < 100 or precio > 300:
        precio = input("ERROR. Reingrese un precio valido: $")
    
    unidades = input("Ingrese una unidad. MAXIMO 1000: ")
    unidades = int(unidades)
    while unidades <= 0 or unidades > 1000:
        unidades = input("ERROR. INGRESE UNA UNIDAD VALIDA: ")
    
    fabricante = input("Ingrese un fabricante: ")

    marca = input("Ingrese una marca: ")
    
    lista.append({"tipo" : tipo, "precio" : precio, "unidades" : unidades, "fabricante" : fabricante, "marca" : marca})

#A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.

for i in range(len(lista)):

    if lista[i]["tipo"] == "barbijo":
        if lista[i]["precio"] > precio_mas_alto:
            precio_mas_alto = lista[i]["precio"]
    else:
        print("No se ingresaron barbijos")   

for i in range(len(lista)):
    if lista[i]["tipo"] == "barbijo" and precio_mas_alto == lista[i]["precio"]:
        cantidad_unidades += f"{lista[i]['unidades']}"
        cantidad_fabricantes += f"{lista[i]['fabricante']}"

mensaje += f"El barbijo mas caro, tiene: {cantidad_unidades} unidades, y el fabricante es: {cantidad_fabricantes}"

print(mensaje)

#B. Del ítem con más unidades, el fabricante. 

for i in range(len(lista)):

    if lista[i]["unidades"] > unidad_maxima:
        unidad_maxima = lista[i]["unidades"]
    else:
        print("No se ingresaron unidades")    

for i in range(len(lista)):

    if lista[i]["unidades"] == unidad_maxima:
        fabricante_mayor = lista[i]['fabricante']

mensaje_2 += f"Fabricante del item con mas unidades: {fabricante_mayor}"
print(mensaje_2)


#C. Cuántas unidades de jabones hay en total. 
cantidad_jabones = 0

for i in range(len(lista)):
    if lista[i]["tipo"] == "jabon":
        cantidad_jabones += lista[i]["unidades"]

    else:
        print("No se ingresaron jabones")   

mensaje_3 += f"Hay un total de {cantidad_jabones} jabones"
print(mensaje_3)
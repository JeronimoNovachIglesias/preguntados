'''
Luego de analizar el set de datos correspondiente resolver el Desafío #01:

A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
fuerza (MÁXIMO)
C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
(MÍNIMO)
D. Recorrer la lista y determinar el peso promedio de los superhéroes
masculinos (PROMEDIO)
E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino

NOTA: Se debe construir un menú en el que se sea posible acceder a cada una de
las opciones (A-E)

'''
from data_stark import lista_personajes



#A
def buscar_personajes():
    mensaje = "-" * 40
    for heroe in range(len(lista_personajes)):
        nombre = lista_personajes[heroe]['nombre']
        identidad = lista_personajes[heroe]['identidad']
        empresa = lista_personajes[heroe]['empresa']
        altura = lista_personajes[heroe]['altura']
        peso = lista_personajes[heroe]['peso']
        genero = lista_personajes[heroe]['genero']
        color_ojos = lista_personajes[heroe]['color_ojos']
        color_pelo = lista_personajes[heroe]['color_pelo']
        fuerza = lista_personajes[heroe]['fuerza']
        inteligencia = lista_personajes[heroe]['inteligencia']
        mensaje += (f"""{heroe}     -Nombre: {nombre}-
        Identidad: {identidad}
        Empresa: {empresa}
        Altura: {altura}
        Peso: {peso}
        Genero: {genero}
        Color de ojos: {color_ojos}
        Color de pelo: {color_pelo}
        Fuerza: {fuerza}
        Inteligencia: {inteligencia}\n{mensaje}""")
        return mensaje

#--------------------------------------------------------

#B
def calcular_maximo_fuerza():

    mayor_fuerza = None
    identidad = ""
    peso = ""

    for heroe in lista_personajes :
        fuerza = int(heroe['fuerza'])
        if mayor_fuerza == None or fuerza > mayor_fuerza:
            mayor_fuerza = fuerza

    for heroe in range(len(lista_personajes)):
        fuerza = int(lista_personajes[heroe]['fuerza'])
        if fuerza == mayor_fuerza:
            identidad += f"{lista_personajes[heroe]['identidad']}"
            peso += f"{lista_personajes[heroe]['peso']}"
    mensaje = f"El superheroe con mayor fuerza es: {identidad} y pesa: {peso}"
    return mensaje

#---------------------------------------------------------

#C
def calcular_altura_minima():
    altura_minima = None
    identidad = ""
    nombre = ""
    mensaje = ""
    for heroe in lista_personajes:
        altura = float(heroe['altura'])
        if altura_minima == None or altura < altura_minima:
            altura_minima = altura

    for heroe in range(len(lista_personajes)):
        altura = float(lista_personajes[heroe]['altura'])
        if altura_minima == altura:
            identidad += f"{lista_personajes[heroe]['identidad']}"
            nombre += f"{lista_personajes[heroe]['nombre']}"
    mensaje += f"El nombre del superheroe mas bajo es: {nombre}\nSu identidad es: {identidad}"
    return mensaje

#-----------------------------------------------------------

#D
def calcular_promedio_masculinos():
        
    acumulador_peso = 0
    contador_masculinos = 0
    mensaje = ""

    for heroe in lista_personajes:
        genero = heroe['genero']
        peso = float(heroe['peso'])
        if genero == "M":
            acumulador_peso += peso
            contador_masculinos += 1

    if contador_masculinos != 0:
        promedio_masculino = acumulador_peso / contador_masculinos

    mensaje += f"El promedio es: {promedio_masculino:.2f}"
    return mensaje


#------------------------------------------------------------

#E
def mostrar_nombre_peso_cuando_fuerza_sea_mayor_promedio_femenino():
    acumulador_fuerza = 0
    contador_femenino = 0
    mensaje = ""
    nombre = ""
    peso = ""

    for heroe in lista_personajes:
        fuerza = int(heroe['fuerza'])
        genero = heroe['genero']
        if genero == "F":
            acumulador_fuerza += fuerza
            contador_femenino += 1

    if contador_femenino != 0:
        promedio_fuerza_femenino = acumulador_fuerza / contador_femenino
    mensaje += f"El promedio de fuerza femenina es: {promedio_fuerza_femenino}\n"

    for heroe in range(len(lista_personajes)):

        if fuerza > promedio_fuerza_femenino:
            peso += f"{lista_personajes[heroe]['peso']}"
            nombre += f"{lista_personajes[heroe]['nombre']}"
    mensaje += f" Superheroes que superan el promedio de fuerza femenino:\nPeso: {peso}\nSu nombre: {nombre}"
    return mensaje


#MENU

while True:

    pedido = input("ingrese una opcion para desplegar un menu:\nA)Muestra todos los datos de los superheroes:\nB)Identidad y peso de los superheroes con mayor fuerza:\nC)Nombre e identidad del superhéroe más bajo:\nD)Peso promedio de los superhéroes masculinos:\nE)Nombre y peso de los superhéroes, los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino:\nPresione N para salir: ")

    match pedido:
        case "A":
            print(buscar_personajes())
        case "B":
            print(calcular_maximo_fuerza())
        case "C":
            print(calcular_altura_minima())
        case "D":
            print(calcular_promedio_masculinos())
        case "E":
            print(mostrar_nombre_peso_cuando_fuerza_sea_mayor_promedio_femenino())
        case "N":
            break
    
from data_stark import lista_personajes



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
        print(f"""{heroe}     -Nombre: {nombre}-
        Identidad: {identidad}
        Empresa: {empresa}
        Altura: {altura}
        Peso: {peso}
        Genero: {genero}
        Color de ojos: {color_ojos}
        Color de pelo: {color_pelo}
        Fuerza: {fuerza}
        Inteligencia: {inteligencia}\n{mensaje}""")

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

print(calcular_maximo_fuerza())

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

print(calcular_altura_minima())

#D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)


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

print(calcular_promedio_masculinos())

#E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) 
# los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino
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
    
print (mostrar_nombre_peso_cuando_fuerza_sea_mayor_promedio_femenino())
    



def buscar_nombre_personajes():
    for heroe in range(len(lista_personajes)):
        nombre = heroe['nombre']

def nombres_no_binarios():
    for heroe in lista_personajes:
        genero = heroe['genero']
        buscar_nombre_personajes()
        if genero == "NB":
            mensaje += f"Nombres de los NO BINARIOS: {buscar_nombre_personajes()}"
        


def promedio_nb():
    for heroe in lista_personajes:
        contador_nb = 0
        acumulador_nb = 0
        genero = heroe['genero']
        mensaje = ""
        if genero == "NB":
            contador_nb += 1
            acumulador_nb += genero
    if contador_nb != 0:
        promedio_nb = acumulador_nb / contador_nb
        mensaje += f"Promedio de genero NO BINARIO: {promedio_nb}" 
        return mensaje

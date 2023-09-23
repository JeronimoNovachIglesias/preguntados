from data_stark_2 import lista_personajes



def calcular_altura_maxima(pregunta):
    altura_max = None
    mensaje_femenina = ""
    mensaje_masculina = ""

    for i in lista_personajes:
        nombre = i['nombre']
        genero = i['genero']
        altura = float(i['altura'])

        if genero == "F":
            if altura_max == None or altura > altura_max:
                altura_max = altura
        elif genero == "M":
             if altura_max == None or altura > altura_max:
                altura_max = altura

        for i in lista_personajes:
                if altura_max == altura and genero == "F":
                    mensaje_femenina = f"Femenina mas alta es: {nombre}"
                elif altura_max == altura and genero == "M" :
                    mensaje_masculina = f"Masculino mas alto es: {nombre}"

    if pregunta == "B": 
        return mensaje_femenina
    elif pregunta == "C":
        return mensaje_masculina

def calcular_mas_debil(pregunta):
    mensaje_masculino = ""
    mensaje_nb = ""
    fuerza_minima = None

    for i in lista_personajes:
        nombre = i['nombre']
        genero = i['genero']
        fuerza = int(i['fuerza'])

        if genero == "M":
            if  fuerza_minima == None or fuerza < fuerza_minima:
                fuerza_minima = fuerza
        elif genero == "NB":
            if fuerza_minima == None or fuerza < fuerza_minima:
                fuerza_minima = fuerza

        for i in lista_personajes:
            if  fuerza_minima == fuerza and genero == "M" :
                mensaje_masculino = f"Masculino mas debil es: {nombre}"
            elif fuerza_minima == fuerza and genero == "NB" :
                mensaje_nb = f"No binario mas debil es: {nombre}"
                
    if pregunta == "D":
        return mensaje_masculino
    elif pregunta == "E":
        return mensaje_nb
    


#F. Fuerza promedio de los superhéroes de género NB 
def buscar_promedio_fuerza_nb():
    contador_nb = 0
    acumulador_nb = 0
    mensaje = ""
    for i in lista_personajes:
        genero = i['genero']
        fuerza = int(i['fuerza'])
        if genero == "NB":
            contador_nb += 1
            acumulador_nb += fuerza
        if genero == "NB" and contador_nb != 0:
            promedio_nb = contador_nb / acumulador_nb
        mensaje += f"Fuerza promedio de los NO BINARIOS: {promedio_nb}"

        return mensaje
    
    print(buscar_promedio_fuerza_nb())


def buscar_dato_personajes(indice:int, key:str):
        
    dato = lista_personajes[indice][key]
        
    return dato

print(buscar_dato_personajes(0, 'nombre'))


def nombres_no_binarios():
    no_binario = "Los nombres NO BINARIOS SON:" + '\n'
    for i in range(len(lista_personajes)):           
        if buscar_dato_personajes(i, 'genero')  == "NB":
            no_binario += f"{buscar_dato_personajes(i, 'nombre')}" + "\n"
    return no_binario

print(nombres_no_binarios())

#B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F

def datos_parseados():
    for i in range(len(lista_personajes)):
        lista_personajes[i]['altura'] = float(lista_personajes[i]['altura'])
        lista_personajes[i]['fuerza'] = int(lista_personajes[i]['fuerza'])
        lista_personajes[i]['peso'] = float(lista_personajes[i]['peso'])


def buscar_maximo_minimo(lista:list, clave:str, max_o_min:str) -> dict:
    datos_parseados()
    maximo_minimo = lista [0][clave]
    
    for heroe in lista:
        if max_o_min == "maximo":
            if heroe[clave] > maximo_minimo:
                maximo_minimo = heroe[clave]
        if max_o_min == "minimo":
            if heroe[clave] < maximo_minimo:
                maximo_minimo = heroe[clave]
          
    return maximo_minimo



def buscar_maximo_minimo_generos(lista:list, clave:str, max_o_min:str, genero:str) :
    lista = lista
    maximo_generos = None
    for heroe in lista:
        if heroe['genero'] == genero:
            maximo_generos = buscar_maximo_minimo(lista, clave, max_o_min)

    return maximo_generos

#print(buscar_maximo_minimo_generos(lista_personajes, 'fuerza', 'maximo', 'M'))



def crear_lista_genero(lista:list, genero:str):
    lista_generos = []
    for heroe in lista:
        if heroe['genero'] == genero:
            lista_generos.append(heroe)

    return lista_generos

def buscar_promedio(lista:list, clave:str, genero:str):
    acumulador_promedio = 0
    contador_promedio = 0
  
    for heroe in lista:
        datos_parseados()
        crear_lista_genero(lista, genero)
        nombre = "Promedio de:"

        if heroe['genero'] == genero:
            contador_promedio += 1
            acumulador_promedio += heroe[clave]
        if contador_promedio != 0 and heroe['genero'] == genero:
            promedio = acumulador_promedio / contador_promedio
    
    return promedio

print(buscar_promedio(lista_personajes, 'fuerza', 'NB'))

def crear_diccionario(lista:list, clave:str,):
    diccionario = {}
    for heroe in lista:
        if heroe[clave] != "" and heroe[clave] != "No Hair":
            diccionario [heroe [clave]] = 0

    return diccionario
print(crear_diccionario(lista_personajes, 'color_ojos'))

def buscar_rasgos(lista:list, clave:str):
    datos_parseados()
    diccionario = crear_diccionario(lista, clave)
    

    for heroe in lista_personajes:
        if heroe[clave] != "" and heroe[clave] != "No Hair":
            diccionario [heroe [clave]] += 1
            

    return diccionario

print(buscar_rasgos(lista_personajes, 'color_ojos'))



#print (buscar_maximo_minimo(lista_personajes, 'fuerza', 'maximo'))

def buscar_comparacion(lista:list, clave:str, genero:str, max_o_min:str):
    datos_parseados()
    
    lista_generos = crear_lista_genero(lista, genero)
    nombre = 'Hombres mas debiles:\n'

    minimo_masculino = buscar_maximo_minimo_generos(lista_generos, clave, max_o_min, genero)

    for heroe in lista_personajes:
        if minimo_masculino == heroe[clave] and heroe['genero'] == genero:
            nombre += f"{heroe['nombre']}\n"

    return nombre

print(buscar_comparacion(lista_personajes, 'peso', "NB", "maximo"))



def crear_diccionario_str(lista:list, clave:str):
    dicc = {}
    for heroe in lista:
        if heroe[clave] != "":
            dicc[heroe[clave]] = ""

    return dicc

def agrupar_por_elementos(lista:list, clave:str):
    diccionario_color = crear_diccionario_str(lista, clave)
    for heroe in lista_personajes:
        for color in diccionario_color:
            if color == heroe [clave] and heroe[clave] != "" :
                diccionario_color[color] += heroe['nombre']

    return diccionario_color

print(agrupar_por_elementos(lista_personajes, 'inteligencia'))  
'''
Desafío #02:
Usando como base lo realizado en el anterior desafío realizar los siguientes
informes en un menú
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género NB
B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
género NB
G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
I. Listar todos los superhéroes agrupados por color de ojos.
J. Listar todos los superhéroes agrupados por tipo de inteligencia
NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú

'''

from data_stark_2 import lista_personajes
from funciones_2 import *

#MENU
opcion = input("""Ingrese una opcion:
A. Nombre de cada superhéroe de género NB.
B. Heroina/s más alta/s. 
C. Heroe/s más alto/s. 
D. Heroe más débil de género M. 
E. Heroe más débil de género NB. 
F. Fuerza promedio de los superhéroes de género NB 
G. Tipos de color de ojos y su cantidad. 
H. Tipos de cabello y su cantidad. 
I. Superhéroes agrupados por color de ojos. 
J. Superhéroes agrupados por tipo de inteligencia 
K. Salir.\n""") 
pregunta = opcion.upper()

while True:

    
    match pregunta:
        case "A":
            print(buscar_personaje_nb())
        case "B":
            print("---- Altura maxima Femenina ----")
            print(buscar_maximo_minimo_generos(lista_personajes, 'altura', 'maximo', 'F'))
        case "C":
            print("---- Altura maxima Masculina ----")
            print(buscar_maximo_minimo_generos(lista_personajes, 'altura', 'maximo', 'M'))                  
        case "D":
            print("---- Fuerza minima Masculina ----")
            print(buscar_maximo_minimo_generos(lista_personajes, 'fuerza', 'minimo', 'M'))                
        case "E":
            print("---- Fuerza maxima No Binario ----")
            print(buscar_maximo_minimo_generos(lista_personajes, 'fuerza', 'maximo', 'NB'))                
        case "F":
            print("---- Promedio de fuerza No Binario ----")
            print(buscar_promedio(lista_personajes, 'fuerza', 'NB'))
        case "G":
            print("---- Cantidad y color de ojos ----")
            print(buscar_rasgos(lista_personajes, 'color_ojos'))    
        case "H":
            print("---- Cantidad y color de pelo ----")
            print(buscar_rasgos(lista_personajes, 'color_pelo'))
        case "I":
            print("---- Tipos de ojos ----")
            print(agrupar_por_elementos(lista_personajes, 'color_ojos'))
        case "J":
            print("---- Tipos de inteligencia ----")
            print(agrupar_por_elementos(lista_personajes, 'inteligencia'))                
        
    opcion = input("Ingrese una letra de la A-K: ")
    pregunta = opcion.upper()
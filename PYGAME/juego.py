'''
Desafío:
A. Analizar detenidamente el set de datos.
B. Recorrer la lista guardando en sub-listas: la pregunta, cada opción y la respuesta
correcta.
C. Crear 2 botones (rectángulos) uno con la etiqueta “Pregunta”, otro con la etiqueta
“Reiniciar”
D. Imprimir el Score: 999 donde se va a ir acumulando el puntaje de las respuestas
correctas. Cada respuesta correcta suma 10 puntos.
E. Al hacer clic en el botón (rectángulo) “Pregunta” debe mostrar las preguntas
comenzando por la primera y las tres opciones, cada clic en este botón pasa a la
siguiente pregunta.
F. Al hacer clic en una de las tres palabras que representa una de las tres opciones, si es
correcta, debe sumar el score y dejar de mostrar las opciones.
G. Solo tiene 2 opciones para acertar la respuesta correcta y sumar puntos, si agotó ambas
opciones, deja de mostrar las opciones y no suma score
H. Al hacer clic en el botón (rectángulo) “Reiniciar” debe mostrar las preguntas
comenzando por la primera y las tres opciones, cada clic pasa a la siguiente pregunta.
También debe reiniciar el Score.

'''

import pygame
from datos_preguntados import *
from constantes import *

pygame.init()



#B. Recorrer la lista guardando en sub-listas: la pregunta, cada opción y la respuesta correcta.
def crear_sublistas(lista:list, clave:str):
    sublista = []
    for pregunta in lista:
        sublista.append(pregunta[clave])
    return sublista

sublista_preguntas = crear_sublistas(lista, 'pregunta')
sublista_opcion_a = crear_sublistas(lista, 'a')
sublista_opcion_b = crear_sublistas(lista, 'b')
sublista_opcion_c = crear_sublistas(lista, 'c')
sublista_opcion_correcta = crear_sublistas(lista, 'correcta')

print(sublista_opcion_correcta)

#defino pantalla    
pantalla = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA]) #-> Inicio la pantalla y sus dimensiones
pygame.display.set_caption("PREGUNTADOS")
#-----------------------------

#Deifno Imagen y la posiciono
imagen = pygame.image.load("preguntados.jpg")
imagen = pygame.transform.scale(imagen,(180, 130))
posicion_imagen = (300, 25)
#-----------------------------

#Inicializo contadores
posicion = 0
oportunidades = 0
score = 0
#-----------------------------

#Defino los textos
pregunta = ""
opcion_a = ""
opcion_b = ""
opcion_c = ""
correcta = ""
incorrecta = ""
fuente = pygame.font.SysFont("Arial", 30)
siguiente = "Siguiente"
reiniciar = "Reiniciar"
#-----------------------------

#Renderizo los textos
texto_pregunta = fuente.render(str(pregunta), True, COLOR_BLANCO)
texto_reiniciar = fuente.render(str(reiniciar), True, COLOR_ROJO)
texto_siguiente = fuente.render(str(siguiente), True, COLOR_ROJO) #--> El booleano es para el diseño
texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_ROJO)
texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_ROJO)
texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_ROJO)
puntuacion = fuente.render(str(score), True, COLOR_ROJO)
texto_correcto = fuente.render(str(correcta), True, COLOR_ROJO)
texto_incorrecto = fuente.render(str(incorrecta), True, COLOR_ROJO)
#-----------------------------


running = True
click_bandera = False
bandera_click = True

# while running:
#     lista_eventos = pygame.event.get()
#     for evento in lista_eventos:
#         if evento.type == pygame.QUIT:
#             running = False #--> Si el usuario cierra el programa, se termina de ejecutar el bucle

#     if click_bandera == False:
#         if evento.type == pygame.MOUSEBUTTONDOWN:
#             posicion_click = list(evento.pos)


bandera_abrio_juego = True

while bandera_abrio_juego:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera_abrio_juego = False
            
            
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            print(posicion_click)

            if(posicion_click[0] > 80 and posicion_click[0] < 230) and (posicion_click[1] > 400 and posicion_click[1] < 500):
                click_bandera = False
                if lista[posicion - 1]['correcta'] == "a":
                    score += 10
                    texto_correcto = fuente.render(str(correcta), True, COLOR_ROJO)
                    if (posicion_click[0] > 320 and posicion_click[0] < 470) and (posicion_click[1] > 400 and posicion_click[1] < 500):
                        oportunidades += 1
                    if (posicion_click[0] > 560 and posicion_click[0] < 710) and (posicion_click[1] > 400 and posicion_click[1] < 500):
                        oportunidades += 1
                        click_bandera = True
                        if oportunidades == 2:
                            break
                    print(score)
                    click_bandera = True
                    oportunidades = 0
                    
                    #texto_incorrecto = fuente.render(str(incorrecta), True, COLOR_ROJO)

            if(posicion_click[0] > 320 and posicion_click[0] < 470) and (posicion_click[1] > 400 and posicion_click[1] < 500):
                if lista[posicion - 1]['correcta'] == "b": 
                    score += 10
                    print(score)
                    oportunidades = 0
                elif lista[posicion - 1]['correcta'] == "c":
                    oportunidades += 1
                elif lista[posicion - 1]['correcta'] == "a":
                    oportunidades += 1
            if oportunidades == 2:
                break

            if(posicion_click[0] > 560 and posicion_click[0] < 710) and (posicion_click[1] > 400 and posicion_click[1] < 500):
                if lista[posicion - 1]['correcta'] == "c":
                    score += 10
                    print(score)
                    oportunidades = 0
                elif lista[posicion - 1]['correcta'] == "a":
                    oportunidades += 1
                elif lista[posicion - 1]['correcta'] == "b":
                    oportunidades += 1
            if oportunidades == 2:
                break


            if (posicion_click[0] > 520 and posicion_click[0] < 720) and (posicion_click[1] > 40 and posicion_click[1] < 140):
                if posicion < len(sublista_opcion_correcta):
                    pregunta = sublista_preguntas[posicion]
                    texto_pregunta = fuente.render(str(pregunta), True, COLOR_BLANCO)
                    opcion_a = sublista_opcion_a[posicion]
                    opcion_b = sublista_opcion_b[posicion]
                    opcion_c = sublista_opcion_c[posicion]
                    sublista_opcion_correcta[posicion]
                    puntuacion = (fuente.render(str(score), True, COLOR_ROJO))

                    texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_ROJO)
                    texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_ROJO)
                    texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_ROJO)

                if posicion <= len(sublista_preguntas):
                    posicion += 1

                    click_bandera = True

            if (posicion_click[0] > 60 and posicion_click[0] < 260) and (posicion_click[1] > 40 and posicion_click[1] < 140):
                if posicion < len(sublista_opcion_correcta):
                    posicion = 0
                    pregunta = sublista_preguntas[posicion]
                    texto_pregunta = fuente.render(str(pregunta), True, COLOR_BLANCO)
                    opcion_a = sublista_opcion_a[posicion]
                    opcion_b = sublista_opcion_b[posicion]
                    opcion_c = sublista_opcion_c[posicion]
                    sublista_opcion_correcta[posicion]
                    texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_ROJO)
                    texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_ROJO)
                    texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_ROJO)
                    puntuacion = (fuente.render(str(score), True, COLOR_ROJO))            
                    
            
            

    


    pantalla.fill(COLOR_CELESTE)
    #Pego todo a mi pantalla mediante el .blit()
    rectangulo_1 = pygame.draw.rect(pantalla, COLOR_BLANCO, (60,40,200,100))
    rectangulo_2 = pygame.draw.rect(pantalla, COLOR_BLANCO, (520,40,200,100))
    rectangulo_opcion_a = pygame.draw.rect(pantalla, COLOR_BLANCO, (10,400,250,100))
    rectangulo_opcion_b = pygame.draw.rect(pantalla, COLOR_BLANCO, (275,400,250,100))
    rectangulo_opcion_c = pygame.draw.rect(pantalla, COLOR_BLANCO, (540,400,250,100))

    pantalla.blit(imagen, (posicion_imagen),)
    pantalla.blit(texto_pregunta,(100, 170))
    pantalla.blit(texto_siguiente,(570,70))
    pantalla.blit(texto_reiniciar,(115,70))
    pantalla.blit(texto_opcion_a,(95, 430))
    pantalla.blit(texto_opcion_b,(330, 430))
    pantalla.blit(texto_opcion_c,(560, 430))
    pantalla.blit(puntuacion, (400, 560))
    pantalla.blit(texto_correcto, (100, 250))
    pygame.display.flip()
pygame.quit()

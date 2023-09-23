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

from datos_preguntados import lista
from constantes import *



pygame.init()

#defino pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))# tamaño de la pantalla

#nombre de la pestaña
pygame.display.set_caption("ENANO")# titulo de la pantalla

#definimos una imagen
imagen = pygame.image.load("enano.jpeg")
imagen = pygame.transform.scale(imagen,(150, 150))
pantalla.fill((COLOR_CELESTE))
pantalla.blit(imagen, (325,70))#pegamos la imagen en la pantalla

#defino musica
pygame.mixer.init()
#pygame.mixer.music.set_volume(0,7)



def recorrer_lista(lista:list, clave:str):
    
    sublista = []
    for pregunta in lista:
        sublista.append(pregunta[clave])

    return sublista
    


sublista_preguntas = recorrer_lista(lista, 'pregunta')
sublista_opciones_a = recorrer_lista(lista, 'a')
sublista_opciones_b = recorrer_lista(lista, 'b')
sublista_opciones_c = recorrer_lista(lista, 'c')
sublista_correctas = recorrer_lista(lista, 'correcta')



posicion = 0
correr = True
while correr:

    lista_eventos = pygame.event.get()
    #defino texto
    fuente = pygame.font.SysFont("Arial Narrow", 30)
    texto = fuente.render("Pregunta", True, (COLOR_BLANCO))
    p = fuente.render("Siguiente", True, (COLOR_BLANCO))
    reinicio = fuente.render("Reiniciar", True, (COLOR_BLANCO))
    texto_pregunta = fuente.render("", True, COLOR_BLANCO)
    pantalla.blit(texto, (100, 350))
    pantalla.blit(p, (550,140))
    pantalla.blit(reinicio, (150, 140))

    pygame.display.flip()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            correr = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            print(posicion_click)
            #iteraccion = lista[posicion_click]
            siguiente = fuente.render("Siguiente", True, (COLOR_BLANCO))
            
            if (posicion_click[0] >= 530 and posicion_click [0] <= 670) and (posicion_click[1] >= 110 and posicion_click [1] < 180):
                print('hola mundo')
                if posicion < len(sublista_preguntas):
                    texto_pregunta = fuente.render(str(sublista_preguntas), True, (COLOR_BLANCO))
                for pregunta in sublista_preguntas:
                    preguntas = fuente.render(texto_pregunta, True, (COLOR_BLANCO))
                    pantalla.blit(imagen, (100,70))#pegamos la imagen en la pantalla

                # nombre = lista[posicion_click]
                
        # if evento.type == pygame.MOUSEBUTTONDOWN:
        #     posicion_click = list(posicion_click)
        #     if rectangulo_rojo.collidelist(lista_eventos) >= 0:
        #        print("click sobre siguiente")




    rectangulo_rojo = pygame.draw.rect(pantalla, (COLOR_ROJO),(100, 100, 200, 100))#LEFT, TOP, ANCHO Y ALTO
    rectangulo_rojo_dos = pygame.draw.rect(pantalla, (COLOR_ROJO),(500, 100, 200, 100))#LEFT, TOP, ANCHO Y ALTO

    # rect_siguiente = rectangulo_rojo_dos.get_rect()
    # rect_siguiente.centerx = 200
    # rect_siguiente.centery = 100
    # print(rect_siguiente.width,rect_siguiente.height)
    # pantalla.blit(rectangulo_rojo_dos, rect_siguiente)







pygame.quit()
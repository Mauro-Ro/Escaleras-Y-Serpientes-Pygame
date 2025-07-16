import pygame
from frontend.variables import score_imagen, score_boton, score_boton_sin_sombra


def mostrar_puntajes(pantalla, fuente):
    with open("score.csv", "r") as archivo:
        y = 230
        for linea in archivo:
            texto = fuente.render(linea.strip(), True, (255, 255, 255))
            pantalla.blit(texto, (250, y))
            y += 60


def dibujar_puntaje(pantalla, verificador_botones, pantalla_actual, estado_juego)->str:
    pantalla.blit(score_imagen, (0, 0))
    print(estado_juego["engyinicio"])

    if verificador_botones(5, 0):
        pantalla.blit(score_boton_sin_sombra, (10, 20))
        if estado_juego["engyinicio"] == 1:
            pantalla_actual = "inicio"
        elif estado_juego["engyinicio"] == 0:
            pantalla_actual = "tablero"
    else:
        pantalla.blit(score_boton, (10, 10))

    fuente = pygame.font.Font("assets/fonts/gumball.ttf", 60)

    mostrar_puntajes(pantalla, fuente)

    return pantalla_actual

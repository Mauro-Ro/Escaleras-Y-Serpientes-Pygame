import pygame
from frontend.animation.animaciones import (
    elegir_botones_mouse,
    lista_botones,
)
from constantes import HEIGTH, WIDTH, FPS
from frontend.screen.menu_engranaje import dibujar_menu
from frontend.screen.inicio import dibujar_inicio
from frontend.screen.puntaje import dibujar_puntaje
from frontend.screen.tablero import tablero_dibujo
from frontend.screen.tablero_preguntas import dibujar_tablero_preguntas
from frontend.screen.input_nombre import dibujar_input


timer_segundos = pygame.USEREVENT


def init_pygame():
    """Este es el inicializador del juego,

    Returns:
        _type_: Retorna la pantalla en la que se va a ver el juego, segun las dimensiones que le dimos.
    """    
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH, HEIGTH))
    pygame.display.set_caption("Serpientes y Escaleras")
    return pantalla


def manejar_eventos()->dict:
    """Esto es un manejador de eventos (maneja interacciones que hacemos con nuestros perifericos).

    Returns:
        _type_: Retorna un Diccionario con las interacciones que hace el jugador.
    """    
    resultados = {
        "mouse_click": (0, 0),
        "salir": False,
        "tiempo": False,
        "teclado": False,
    }

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            resultados["salir"] = True

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            resultados["mouse_click"] = evento.pos

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                resultados["teclado"] = "eliminar"
            else:
                resultados["teclado"] = evento.unicode

        elif evento.type == timer_segundos:
            resultados["tiempo"] = True

    return resultados


def game_loop():
    """Este es loop del juego, basicamente un juego se conforma de un "while true" es masomenos asi como funciona
        solo que va a 60 frames por segun, en este caso
    """    
    pantalla = init_pygame()
    clock = pygame.time.Clock()

    estado_juego = {
        "contador": 16,
        "tiempo_opcion": 2,
        "nombre": "",
        "num_random": False,
        "opcion": None,
        "posicion": 14,
        "engyinicio": 0,
    }
    pantallas = {
        "inicio": dibujar_inicio,
        "input": dibujar_input,
        "tablero": tablero_dibujo,
        "menu": dibujar_menu,
        "preguntas": dibujar_tablero_preguntas,
        "puntaje": dibujar_puntaje,
    }
    pantalla_actual = "inicio"

    pygame.time.set_timer(timer_segundos, 1000)

    run = True
    while run:

        manejar_salida_eventos = manejar_eventos()

        if manejar_salida_eventos["salir"]:
            pygame.quit()

        boton_clickeado = manejar_salida_eventos["mouse_click"]

        verificador_botones = elegir_botones_mouse(boton_clickeado, lista_botones, pantalla)


        # cuando tenga tiempo resuelvo el desastre de ifs que tengo aca abajo ↓ 

        if pantalla_actual == "inicio" or pantalla_actual == "puntaje":
            pantalla_actual = pantallas[pantalla_actual](pantalla, verificador_botones, pantalla_actual, estado_juego)
        elif pantalla_actual == "tablero":
            pantalla_actual = pantallas[pantalla_actual](pantalla, verificador_botones, pantalla_actual, estado_juego)
            estado_juego["contador"] = 16
            if manejar_salida_eventos["tiempo"]:
                if estado_juego["tiempo_opcion"] > 0:
                    estado_juego["tiempo_opcion"] -= 1
        elif pantalla_actual == "preguntas":
            estado_juego["tiempo_opcion"] = 2
            estado_juego["opcion"] = None
            pantalla_actual = pantallas[pantalla_actual](pantalla, verificador_botones, pantalla_actual, estado_juego)
            if manejar_salida_eventos["tiempo"]:
                if estado_juego["contador"] > 0:
                    estado_juego["contador"] -= 1

        elif pantalla_actual == "input":
            pantalla_actual = pantallas[pantalla_actual](pantalla, verificador_botones, pantalla_actual, manejar_salida_eventos, estado_juego,)
        if pantalla_actual == "menu":
            pantalla_actual = pantallas[pantalla_actual](pantalla, verificador_botones, pantalla_actual)
        pygame.display.flip()

        clock.tick(FPS)


if __name__ == "__main__":
    game_loop()

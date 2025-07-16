import pygame

from frontend.variables import (
    inicio_imagen,
    comenzar_imagen,
    comenzar_sin_sombra_imagen,
    puntaje_inicio_imagen,
    puntaje_sin_sombra_inicio_imagen,
    salir_inicio_imagen,
    salir_sin_sombra_inicio_imagen,
)


def dibujar_inicio(pantalla, verificador_botones, pantalla_actual, estado_juego)->str:
    """Dibuja el inicio segun la imagen 

    Args:
        pantalla (_type_): _description_
        verificador_botones (_type_): _description_
        pantalla_actual (_type_): _description_
        estado_juego (_type_): _description_

    Returns:
        _type_: _description_
    """    
    pantalla.blit(inicio_imagen, (0, 0))

    if verificador_botones(0, 0):
        pantalla.blit(comenzar_sin_sombra_imagen, (0, 10))
        estado_juego["engyinicio"] = 0
        pantalla_actual = "input"
    else:
        pantalla.blit(comenzar_imagen, (0, 0))

    if verificador_botones(0, 1):
        pantalla.blit(puntaje_sin_sombra_inicio_imagen, (0, 10))
        pantalla_actual = "puntaje"
        estado_juego["engyinicio"] = 1
    else:
        pantalla.blit(puntaje_inicio_imagen, (0, 0))

    if verificador_botones(0, 2):
        pantalla.blit(salir_sin_sombra_inicio_imagen, (0, 10))
        pygame.quit()
    else:
        pantalla.blit(salir_inicio_imagen, (0, 0))

    return pantalla_actual

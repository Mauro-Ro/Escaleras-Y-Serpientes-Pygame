import pygame

from frontend.variables import (
    menu_imagen,
    engranaje_imagen, engranaje_sin_sombra_imagen,
    reanudar_imagen, reanudar_sin_sombra_imagen,
    puntaje_imagen, puntaje_sin_sombra_imagen,
    salir_imagen, salir_sin_sombra_imagen
)


def dibujar_menu(pantalla, verificador_botones, pantalla_actual, estado_juego):

    pantalla.blit(menu_imagen, (7, 0))

    if verificador_botones(2, 0):
        pantalla.blit(reanudar_sin_sombra_imagen, (0, 10))
        pantalla_actual = "tablero"
    else:
        pantalla.blit(reanudar_imagen, (0, 0))

    if verificador_botones(2, 1):
        pantalla.blit(puntaje_sin_sombra_imagen, (0, 10))
        pantalla_actual = "puntaje"
        
    else:
        pantalla.blit(puntaje_imagen, (0, 0))

    if verificador_botones(2, 2):
        pantalla.blit(salir_sin_sombra_imagen, (0, 10))
        pygame.quit()
    else:
        pantalla.blit(salir_imagen, (0, 0))

    return pantalla_actual
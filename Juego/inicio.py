import pygame

from frontend.funciones import (
    inicio_imagen,
    comenzar_imagen,comenzar_sin_sombra_imagen,
    puntaje_inicio_imagen,puntaje_sin_sombra_inicio_imagen,
    salir_inicio_imagen,salir_sin_sombra_inicio_imagen

)


def dibujar_inicio(pantalla, verficador_botones, pantalla_actual):
    pantalla.blit(inicio_imagen(),(0,0))

    if verficador_botones(0,0):
        pantalla.blit(comenzar_sin_sombra_imagen(),(0, 10))
        pantalla_actual = "tablero"
    else:
        pantalla.blit(comenzar_imagen(),(0,0))

    if verficador_botones(0,1):
        pantalla.blit(puntaje_sin_sombra_inicio_imagen(),(0, 10))
    else:
        pantalla.blit(puntaje_inicio_imagen(),(0,0))

    if verficador_botones(0,2):
        pantalla.blit(salir_sin_sombra_inicio_imagen(),(0, 10))
        pygame.quit()
    else:
        pantalla.blit(salir_inicio_imagen(),(0,0))
    
    return pantalla_actual
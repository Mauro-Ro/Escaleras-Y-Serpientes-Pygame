import pygame
from frontend.funciones import (boton_seguir_sin_sombra_imagen, 
                                boton_seguir_imagen, tablero_imagen,
                                engranaje_imagen, engranaje_sin_sombra_imagen)



def tablero_dibujo(pantalla, verificador_botones, pantalla_actual):
    pantalla.blit(tablero_imagen(),(0,0))

    if verificador_botones(1, 0):
        pantalla.blit(engranaje_sin_sombra_imagen(), (274, -267))
        pantalla_actual = "menu"
    else:
        pantalla.blit(engranaje_imagen(), (270, -270))

    if verificador_botones(1, 1):
        pantalla.blit(boton_seguir_sin_sombra_imagen(),(4, 4))
        pantalla_actual = "preguntas"
    else:    
        pantalla.blit(boton_seguir_imagen(),(0, 0))

    return pantalla_actual


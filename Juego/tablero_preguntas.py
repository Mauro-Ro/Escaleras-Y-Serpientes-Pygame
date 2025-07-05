import pygame

from funciones.funciones import *
from frontend.funciones import tablero_preguntas_imagen
from frontend.animaciones import dibujar_string_pantalla
from frontend.funciones import (
    tablero_preguntas_imagen,
    boton_preguntas_imagen,
    boton_preguntas_sin_sombra_imagen
)


def dibujar_tablero_preguntas(pantalla, verificador_botones, pantalla_actual, tiempo):
    pantalla.blit(tablero_preguntas_imagen(),(0,0))
    

    if tiempo > 9:
        pantalla.blit(dibujar_string_pantalla(70, str(tiempo)), (325, 65))
    else:
        pantalla.blit(dibujar_string_pantalla(70, str(tiempo)), (340, 65))


    if verificador_botones(3, 0):
        pantalla.blit(boton_preguntas_sin_sombra_imagen(),(0, 10))
    else:
        pantalla.blit(boton_preguntas_imagen(),(0, 0))
        
        
    if verificador_botones(3, 1):
        pantalla.blit(boton_preguntas_sin_sombra_imagen(),(0, 90))
    else:
        pantalla.blit(boton_preguntas_imagen(),(0, 80))
        

    if verificador_botones(3, 2):
        pantalla.blit(boton_preguntas_sin_sombra_imagen(),(0, 170))
    else:
        pantalla.blit(boton_preguntas_imagen(),(0, 160))
        
    if tiempo > 14:
        pantalla_actual = "tablero"

    return pantalla_actual
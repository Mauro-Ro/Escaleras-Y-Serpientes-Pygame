import pygame

from frontend.animation.animaciones import dibujar_string_pantalla
from frontend.variables import input_imagen, boton_input_img, boton_input_sin_sombra_img





def dibujar_input(pantalla, verificador_botones, pantalla_actual,  eventos, estado_juego):

    pantalla.blit(input_imagen ,(0,0))


    if eventos["teclado"] and eventos["teclado"] != "eliminar" and len(estado_juego["nombre"]) < 14:
        estado_juego["nombre"] += eventos["teclado"]

    if eventos["teclado"] == "eliminar":
        estado_juego["nombre"] = estado_juego["nombre"][:-1]


    if verificador_botones(4,0) :
        pantalla.blit(boton_input_sin_sombra_img, (0,10))
        if len(estado_juego["nombre"]) != 0:
            pantalla_actual = "tablero"
    else:
        pantalla.blit(boton_input_img, (0,0))


    pantalla.blit(dibujar_string_pantalla(50, estado_juego["nombre"]), (140,278))

    return pantalla_actual
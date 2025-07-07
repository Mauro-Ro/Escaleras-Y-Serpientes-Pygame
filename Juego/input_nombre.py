import pygame

from frontend.animaciones import dibujar_string_pantalla
from frontend.funciones import input_imagen, boton_input_img, boton_input_sin_sombra_img





def dibujar_input(pantalla, verificador_botones, pantalla_actual,  eventos, estado):

    pantalla.blit(input_imagen() ,(0,0))


    if eventos["teclado"] and eventos["teclado"] != "eliminar" and len(estado["nombre"]) < 15:
        estado["nombre"] += eventos["teclado"]

    if eventos["teclado"] == "eliminar":
        estado["nombre"] = estado["nombre"][:-1]



    if verificador_botones(4,0):
        pantalla.blit(boton_input_sin_sombra_img(), (0,10))
        pantalla_actual = "tablero"
    else:
        pantalla.blit(boton_input_img(), (0,0))


    pantalla.blit(dibujar_string_pantalla(50, estado["nombre"]), (140,278))

    return pantalla_actual
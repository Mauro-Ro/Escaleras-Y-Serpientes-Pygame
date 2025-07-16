import pygame
from data.funciones import numero_random, lista_preguntas
from frontend.animation.animaciones import dibujar_mensaje_con_borde
from frontend.screen.jugador import movimiento_jugador
from frontend.variables import (
    boton_seguir_sin_sombra_imagen,
    boton_seguir_imagen,
    tablero_imagen,
    engranaje_imagen,
    engranaje_sin_sombra_imagen,
)

tablero = [ 0, 1, 0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 2, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 0,]


def tablero_dibujo(pantalla, verificador_botones, pantalla_actual, estado_juego)->str:
    pantalla.blit(tablero_imagen, (0, 0))

    if verificador_botones(1, 0):
        pantalla.blit(engranaje_sin_sombra_imagen, (274, -267))
        pantalla_actual = "menu"

    else:
        pantalla.blit(engranaje_imagen, (270, -270))

    if verificador_botones(1, 1):
        pantalla.blit(boton_seguir_sin_sombra_imagen, (4, 4))
        if len(lista_preguntas) != 0:
            estado_juego["num_random"] = numero_random(lista_preguntas)
        else:
            estado_juego["num_random"] = "No hay mas numeros"

        pantalla_actual = "preguntas"
    else:
        pantalla.blit(boton_seguir_imagen, (0, 0))

    rect = pygame.Rect(50, 275, 600, 150)

    movimiento_jugador(pantalla, estado_juego)

    if estado_juego["opcion"] != None and estado_juego["tiempo_opcion"] > 0:
        if estado_juego["opcion"] == True:
            dibujar_mensaje_con_borde(pantalla, "Opción Correcta!", rect)
        elif estado_juego["opcion"] == False:
            dibujar_mensaje_con_borde(pantalla, "Opción Incorrecta", rect)

    if estado_juego["tiempo_opcion"] == 0:
        if estado_juego["opcion"] == True:
            estado_juego["posicion"] += 1
            if tablero[estado_juego["posicion"]] != 0:
                estado_juego["posicion"] += tablero[estado_juego["posicion"]]

        elif estado_juego["opcion"] == False:
            estado_juego["posicion"] -= 1
            if tablero[estado_juego["posicion"]] != 0:
                estado_juego["posicion"] -= tablero[estado_juego["posicion"]]

        estado_juego["opcion"] = None

    return pantalla_actual

import pygame
from frontend.variables import jugador_img


coordenadas_casilleros = [
    (0, 0), (78, 0), (156, 0), (234, 0), (312, 0), (390, 0),                     # fila 1 → →
    (390, -78), (312, -78), (234, -78), (156, -78), (78, -78), (0, -78),         # fila 2 ← ←
    (0, -158), (78, -158), (156, -158), (234, -158), (312, -158), (390, -158),   # fila 3 → →
    (390, -236), (312, -236), (234, -236), (156, -236), (78, -236), (0, -236),   # fila 4 ← ←
    (0, -315), (78, -315), (156, -315), (234, -315), (312, -315), (390, -315)    # fila 5 → →
]




def movimiento_jugador(pantalla, estado_juego):

    posicion_actual = estado_juego["posicion"]


    coordenadas = coordenadas_casilleros[posicion_actual]
    pantalla.blit(jugador_img, coordenadas)

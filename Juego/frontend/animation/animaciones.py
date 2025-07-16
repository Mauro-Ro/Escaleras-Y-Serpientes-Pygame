import pygame


tupla_botones_inicio = (
    pygame.Rect(59, 550, 592, 63),  # 0 Comenzar
    pygame.Rect(58, 412, 181, 63),  # 1 Puntaje
    pygame.Rect(471, 412, 181, 63),
)  # 2 Salir

tupla_botones_tablero = (
    pygame.Rect(593, 54, 75, 70),  # 0 Engranaje
    pygame.Rect(176, 543, 358, 62),
)  # 1 Seguir

tupla_botones_menu = (
    pygame.Rect(172, 261, 357, 60),  # 0 Reanudar
    pygame.Rect(172, 353, 357, 60),  # 1 Puntaje
    pygame.Rect(172, 445, 358, 60),
)  # 2 Salir

tupla_botones_preguntas = (
    pygame.Rect(110, 183, 480, 210),  # Cuadro Preguntas
    pygame.Rect(176, 409, 357, 60),  # 1 Boton A
    pygame.Rect(176, 489, 357, 60),  # 2 Boton B
    pygame.Rect(176, 569, 357, 60),
)  # 3 Boton C

tupla_botones_input = (
    pygame.Rect(235, 362, 240, 62),  # 0 Reanudar
    pygame.Rect(120, 272, 357, 63),
)  # 1 Puntaje


tupla_botones_puntaje = (pygame.Rect(10, 10, 183, 64),)


lista_botones = [
    tupla_botones_inicio,
    tupla_botones_tablero,
    tupla_botones_menu,
    tupla_botones_preguntas,
    tupla_botones_input,
    tupla_botones_puntaje,
]


def botones_sobre_mouse(posicion: tuple, lista_botones: list, fila_list: int, fila_tupla: int, pantalla) -> bool:
    objecto = lista_botones[fila_list][fila_tupla]
    # pygame.draw.rect(pantalla, (255, 0, 0), (lista_botones[fila_list][fila_tupla]), 1)
    # print(objecto.collidepoint(posicion))
    return objecto.collidepoint(posicion)


def elegir_botones_mouse(posicion: tuple, lista_botones: list, pantalla):
    return lambda fila_list, fila_tupla: botones_sobre_mouse(posicion, lista_botones, fila_list, fila_tupla, pantalla)


def dibujar_string_pantalla(size: int, texto: str):
    fuente = pygame.font.Font("assets/fonts/gumball.ttf", size)
    texto_renderizado = fuente.render(texto, True, (255, 255, 255))
    return texto_renderizado


def dibujar_texto_centrado(texto, rect):
    texto_rect = texto.get_rect(center=rect.center)
    texto_rect = texto_rect.clamp(rect)
    return texto_rect



# Tengo que arreglar esta funcion de aca abajo,

def dibujar_mensaje_con_borde( pantalla, texto, rect, color_fondo=(223, 120, 135), color_borde=(0, 0, 0), color_texto=(0, 0, 0), fuente_path="assets/fonts/gumball.ttf", tamano=55, radio_borde=20,):
    # Fondo del rectángulo con bordes redondeados
    pygame.draw.rect(pantalla, color_fondo, rect, border_radius=radio_borde)

    # Borde del rectángulo (1 píxel) con bordes redondeados
    pygame.draw.rect(pantalla, color_borde, rect, width=4, border_radius=radio_borde)

    # Texto
    fuente = pygame.font.Font(fuente_path, tamano)
    texto_render = fuente.render(texto, True, color_texto)
    texto_rect = texto_render.get_rect(center=rect.center)

    # Dibujar texto encima
    pantalla.blit(texto_render, texto_rect)

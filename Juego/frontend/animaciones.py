import pygame


tupla_botones_inicio = (
                pygame.Rect(59, 550, 592, 63),  # 0 Comenzar
                pygame.Rect(58, 412, 181, 63),  # 1 Puntaje
                pygame.Rect(471, 412, 181, 63)) # 2 Salir
                                
tupla_botones_tablero = (
                pygame.Rect(593, 54, 75, 70),   # 0 Engranaje
                pygame.Rect(176, 543, 358, 62)) # 1 Seguir

tupla_botones_menu = (
                pygame.Rect(172, 261, 357, 60), # 0 Reanudar
                pygame.Rect(172, 353, 357, 60), # 1 Puntaje
                pygame.Rect(172, 445, 358, 60)) # 2 Salir

tupla_botones_preguntas = (
                pygame.Rect(176, 409, 357, 60),  # 0 Boton A
                pygame.Rect(176, 489, 357, 60),  # 1 Boton B
                pygame.Rect(176, 569, 357, 60))  # 2 Boton C

tupla_botones_input = (
                pygame.Rect(235, 362, 240, 62), # 0 Reanudar
                pygame.Rect(120, 272, 357, 63)) # 1 Puntaje


lista_botones = [
    tupla_botones_inicio,
    tupla_botones_tablero,
    tupla_botones_menu,
    tupla_botones_preguntas,
    tupla_botones_input
]

def botones_sobre_mouse(posicion: tuple, lista_botones: list, fila_list: int, fila_tupla: int, pantalla)-> bool:
    objecto = lista_botones[fila_list][fila_tupla]
    pygame.draw.rect(pantalla, (255, 0, 0), (lista_botones[fila_list][fila_tupla]), 1)
    # print(objecto.collidepoint(posicion))
    return objecto.collidepoint(posicion)



def elegir_botones_mouse(posicion: tuple, lista_botones: list, pantalla):
    return lambda fila_list, fila_tupla : botones_sobre_mouse(posicion, lista_botones, fila_list, fila_tupla, pantalla)



def dibujar_string_pantalla(size: int, texto: str ):
    fuente = pygame.font.Font("assets/fonts/gumball.ttf", size)
    texto_renderizado = fuente.render(texto, True, (255, 255, 255))
    return texto_renderizado
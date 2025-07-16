
from frontend.animation.animaciones import dibujar_texto_centrado, lista_botones
from data.funciones import buscar_pregunta
from frontend.variables import tablero_preguntas_imagen
from frontend.animation.animaciones import dibujar_string_pantalla


from frontend.variables import (
    imagenes_preguntas,
    boton_preguntas_imagen,
    boton_preguntas_sin_sombra_imagen,
)


def dibujar_tablero_preguntas(pantalla, verificador_botones, pantalla_actual, estado)->str:
    pantalla.blit(tablero_preguntas_imagen, (0, 0))

    respuesta = ""

    num_random = estado["num_random"]

    lista_texto = buscar_pregunta(num_random)
    contador = estado["contador"]

    # Cronometro
    if contador > 9:
        pantalla.blit(dibujar_string_pantalla(70, str(contador)), (325, 65))
    else:
        pantalla.blit(dibujar_string_pantalla(70, str(contador)), (340, 65))

    pantalla.blit(imagenes_preguntas[num_random], (5, -85))

    texto_a = dibujar_string_pantalla(28, lista_texto[1])
    boton_rect_a = lista_botones[3][1]

    texto_b = dibujar_string_pantalla(28, lista_texto[2])
    boton_rect_b = lista_botones[3][2]

    texto_c = dibujar_string_pantalla(28, lista_texto[3])
    boton_rect_c = lista_botones[3][3]

    # Boton A
    if verificador_botones(3, 1):
        pantalla.blit(boton_preguntas_sin_sombra_imagen, (0, 10))
        respuesta = "a"
        if respuesta != lista_texto[4]:
            estado["opcion"] = False
            pantalla_actual = "tablero"
        else:
            estado["opcion"] = True
    else:
        pantalla.blit(boton_preguntas_imagen, (0, 0))
        # pantalla.blit(dibujar_string_pantalla(30, lista_texto[1]), texto_rect_a)

        pantalla.blit(texto_a, dibujar_texto_centrado(texto_a, boton_rect_a))

    # Boton B
    if verificador_botones(3, 2):
        pantalla.blit(boton_preguntas_sin_sombra_imagen, (0, 90))
        respuesta = "b"
        if respuesta != lista_texto[4]:
            estado["opcion"] = False
            pantalla_actual = "tablero"
        else:
            estado["opcion"] = True
    else:
        pantalla.blit(boton_preguntas_imagen, (0, 80))
        # pantalla.blit(dibujar_string_pantalla(30, lista_texto[2]), texto_rect_b)

        pantalla.blit(texto_b, dibujar_texto_centrado(texto_b, boton_rect_b))

    # Boton C
    if verificador_botones(3, 3):
        pantalla.blit(boton_preguntas_sin_sombra_imagen, (0, 170))
        respuesta = "c"
        if respuesta != lista_texto[4]:
            estado["opcion"] = False
            pantalla_actual = "tablero"
        else:
            estado["opcion"] = True
    else:
        pantalla.blit(boton_preguntas_imagen, (0, 160))
        # pantalla.blit(dibujar_string_pantalla(30, lista_texto[3]), texto_rect_c)

        pantalla.blit(texto_c, dibujar_texto_centrado(texto_c, boton_rect_c))

    if estado["opcion"] == True:
        pantalla_actual = "tablero"

    if estado["contador"] == 0:
        estado["opcion"] = False
        pantalla_actual = "tablero"

    return pantalla_actual

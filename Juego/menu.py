import pygame
from funciones.funciones import *
from constantes import *
from frontend.funciones import *
from frontend.animaciones import *
from menu_engranaje import dibujar_menu
from inicio import dibujar_inicio
from tablero import tablero_dibujo
from tablero_preguntas import dibujar_tablero_preguntas

tablero = [
    0, 1, 0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 2, 1, 1, 2, 1, 0, 1, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 0]



def posicion_jugador(x, y):
    x *= 2
    y *= 2
    return (x, y)


def init_pygame():
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH, HEIGTH))
    pygame.display.set_caption("Serpientes y Escaleras")
    return pantalla


def posicion_mouse(evento):
    if evento.type == pygame.MOUSEBUTTONDOWN:
        # print(posicion_mouse[0])
        return evento.pos



timer_segundos = pygame.USEREVENT 



def manejar_eventos():
    resultados = {
        "mouse_click": (0, 0),
        "salir": False,
        "tiempo": False
    }


    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            resultados["salir"] = True

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            resultados["mouse_click"] = evento.pos

        elif evento.type == pygame.KEYDOWN:
            resultados["tecla"] = evento.key

        elif evento.type == timer_segundos:
            resultados["tiempo"] = True



    return resultados


def ubicacion_del_mouse():
    return pygame.mouse.get_pos()


def cambiar_pantalla(pantalla, pantalla_actual_1):
    for key in pantalla_actual_1:
        if pantalla_actual_1[key] == pantalla:
            pantalla_actual_1[key] = True
            return pantalla_actual_1[key]
        

def contar_tiempo(bool_contador):
    contador = 0
    if contador < 15:
        if bool_contador == True:
            contador += 1
            
    return contador




def game_loop():
    
    pantalla = init_pygame()
    clock = pygame.time.Clock()

    estado_juego = {
        "contador": 0
    }

    pantalla_actual = "inicio"
    
    pantallas = {
        "inicio": dibujar_inicio,
        "tablero": tablero_dibujo,
        "menu": dibujar_menu,
        "preguntas": dibujar_tablero_preguntas
    }


    pantalla_actual = "inicio"

    numero_aleatorio = numero_random(lista_preguntas)

    lista_string_preguntas = buscar_pregunta(numero_aleatorio)

    pygame.time.set_timer(timer_segundos, 1000) 



    run = True
    while run:

        manejar_salida = manejar_eventos()

        if manejar_salida["salir"] == True:
            pygame.quit()

        boton_clickeado = manejar_salida["mouse_click"]


        verificador_botones = elegir_botones_mouse(boton_clickeado, lista_botones, pantalla)
        

        if pantalla_actual != "preguntas":
            pantalla_actual = pantallas[pantalla_actual](pantalla, verificador_botones, pantalla_actual)
            if estado_juego["contador"] == 15:
                estado_juego["contador"] = 0 
        else:
            pantalla_actual = pantallas[pantalla_actual](pantalla, verificador_botones, pantalla_actual, estado_juego["contador"])
            if manejar_salida["tiempo"]:
                if estado_juego["contador"] <= 15:
                    estado_juego["contador"] += 1
                    print(estado_juego["contador"])

    


        pygame.display.flip()
        
        clock.tick(FPS)




"""
def menu():
    run = True
    posicion = 14
    input_nombre = input("ingrese su nombre: ")
    lista_nums = []
    while run:
        # print(tablero[posicion])
        validar = validar_seguir_jugando("Desea seguir jugando responda (si/no): ", "error")
        
        if validar == False:
            print("Cerrando Juego")
            run = False
        else:
            numero_elegido = numero_random(lista_preguntas)

            buscar_pregunta(numero_elegido)

            acierto = validar_respuesta(numero_elegido)

            lista_nums.append(numero_elegido)


            if acierto:
                posicion += 1
                print("¡Respuesta correcta! Avanzás un casillero.")
            else:
                posicion -= 1
                print("Respuesta incorrecta. Retrocedés un casillero.")


            # Aplicar escalera o serpiente
            if tablero[posicion] != 0:
                if posicion > 14:
                    print("¡Escalera! Avanzás", tablero[posicion], "casilleros.")
                    posicion += tablero[posicion]
                
                if posicion < 15:
                    print("¡Serpiente! Retrocedés", tablero[posicion], "casilleros.")
                    posicion -= tablero[posicion]


            # Verificar si ganó o perdió
            if posicion >= len(tablero):
                print("¡Ganaste! Llegaste al final del tablero.")
                run = False
            elif posicion < 0:
                print("Perdiste. Retrocediste demasiado.")
                run = False

            if len(lista_nums) == 15:
                print("¡Fin del juego! Se respondieron las 15 preguntas.")
                run = False



            if len(lista_nums) == 15:
                run = False

    with open("score.csv", 'a+') as archivo:
        archivo.write(f"{input_nombre},{posicion}\n")
        
        archivo.close

"""
 
if __name__ == '__main__':
    game_loop()







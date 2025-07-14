import random
from data.preguntas import preguntas


lista_preguntas = list(range(15))

# lista_preguntas = [1, 2, 8, 0]

"""
Módulo de funciones para manejar preguntas, respuestas y flujo de juego.

Contiene utilidades para mostrar preguntas, validar respuestas del usuario,
elegir preguntas al azar sin repetir, y controlar si el usuario desea continuar jugando.
"""


def numero_random(lista: list)->int:
    """
    Elige un número aleatorio de una lista y lo elimina de la misma.

    Selecciona un elemento al azar de la lista `lista`, lo elimina para evitar repeticiones,
    y lo devuelve.

    Args:
        lista (list): Lista de números disponibles para seleccionar.

    Returns:
        int: El número seleccionado aleatoriamente de la lista.
    """  
    elegido = random.choice(lista)

    lista.remove(elegido)

    return elegido

def buscar_pregunta(num: int):
    """
    Muestra por pantalla una pregunta y sus tres opciones (a, b, c).

    La función accede al diccionario ubicado en la posición `num` de la lista `preguntas`,
    e imprime en orden: la pregunta, seguida de las opciones a, b y c.

    Args:
        num (int): Índice de la pregunta dentro de la lista `preguntas`.
    """ 
    valor = preguntas[num]
    lista_preguntas = [
        valor["pregunta"], valor["respuesta_a"],
        valor["respuesta_b"], valor["respuesta_c"],
        valor["respuesta_correcta"]
    ]

    return lista_preguntas

def buscar_respuesta(num: int)->str:
    """
    Busca y devuelve la respuesta correcta de una pregunta según su índice.

    Asume que cada elemento en la lista `preguntas` es un diccionario,
    y que el valor de la clave número 4 (posición 4 del `.values()`)
    corresponde a la respuesta correcta.

    Args:
        num (int): Índice de la pregunta dentro de la lista `preguntas`.

    Returns:
        str: La respuesta correcta de la pregunta indicada.
    """
    respuesta = ""
    valor = preguntas[num]
    respuesta = valor["respuesta_correcta"]
    return respuesta

def validar_respuesta(num: int)->bool:
    """
    Valida si la respuesta ingresada por el usuario coincide con la respuesta correcta.

    Si el usuario ingresa un número como respuesta, se rechaza automáticamente.
    Compara la respuesta del usuario (en minúsculas) con la respuesta correcta
    obtenida mediante la función `buscar_respuesta`.

    Args:
        num (int): Índice o identificador de la pregunta para buscar la respuesta correcta.

    Returns:
        bool: True si la respuesta es correcta, False si es incorrecta o inválida.
    """  
    respuesta = True
    run = True
    while run:
        ingrese = input("Ingrese su respuesta: ")

        if ingrese.isdigit() == True:
            print("No puede ser un numero")
        else:
            if buscar_respuesta(num) == ingrese.lower():
                respuesta = True
            else:
                respuesta = False
            run = False

    return respuesta

def validar_seguir_jugando(entrada:str, error: str)->bool:
    """
    Pide al usuario que ingrese 'si' o 'no' y valida la respuesta.

    Se repite hasta que el usuario escriba una opción válida ('si' o 'no').
    Devuelve True si el usuario ingresó 'si', o False si ingresó 'no'.

    Args:
        entrada (str): Mensaje que se muestra al usuario para pedir la entrada.
        error (str): Mensaje que se muestra si la entrada es inválida.

    Returns:
        bool: True si el usuario ingresó 'si', False si ingresó 'no'.
    """ 
    correr = True
    seguir_jugando = True
    while correr:
        ingrese = input(entrada).lower()

        if ingrese == "si" or ingrese == "no":
            if ingrese == "si":
                seguir_jugando = True
            else:
                seguir_jugando = False
            correr = False
        else:
            print(error)

    return seguir_jugando

def mostrar_tablero(posicion: int, tablero: list):
    """Muestra el tablero y donde se ubica el jugador con una "J"

    Args:
        posicion (int): Posicion en la que esta el jugador
        tablero (list): La lista del tablero para convertirla en una lista con guiones
    """    
    linea = ""
    for i in range(len(tablero)):
        if i == posicion:
            linea += "J "
        else: 
            linea += "- "
    print(f"Tablero:\n{linea}\n")

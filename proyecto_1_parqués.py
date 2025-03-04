# -*- coding: utf-8 -*-
"""Proyecto #1 - Parqués.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x9mjNSyFo_jqg0y49IWiJ8iJoE69D7dS
"""

import os
import random
import sys

# Tablero inicial
tablero = [
    ["*****", "*****", "*****", "*****", "*****", "*****", "*****", "____|", "____|", "____|", "*****", "*****", "*****", "*****", "*****", "*****", "*****"],
    ["*****", "*****", "*****", "*****", "*****", "*****", "*****", "____|", "____|", "____|", "*****", "*****", "*****", "*****", "*****", "*****", "*****"],
    ["*****", "*****", "*****", "*****", "*****", "*****", "*****", "____|", "____|", "____|", "*****", "*****", "*****", "*****", "*****", "*****", "*****"],
    ["*****", "*****", "*****", "*****", "*****", "*****", "*****", "____|", "____|", "____|", "*****", "*****", "*****", "*****", "*****", "*****", "*****"],
    ["*****", "*****", "*****", "*****", "*****", "*****", "*****", "____|", "____|", "____|", "*****", "*****", "*****", "*****", "*****", "*****", "*****"],
    ["*****", "*****", "*****", "*****", "*****", "*****", "*****", "____|", "____|", "____|", "*****", "*****", "*****", "*****", "*****", "*****", "*****"],
    [" A1 |", " A2 |", "*****", "*****", "*****", "*****", "*****", "____|", "____|", "____|", "*****", "*****", "*****", "*****", "*****", "*****", "*****"],
    ["____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|"],
    ["____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "Meta ", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|"],
    ["____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|", "____|"],
    ["*****", "*****", "*****", "*****", "*****", "*****", "*****", "____|", "____|", "____|", " B1 |", " B2 |", "*****", "*****", "*****", "*****", "*****"],
    ["*****", "*****", "*****", "*****", "*****", "*****", "*****", "____|", "____|", "____|", "*****", "*****", "*****", "*****", "*****", "*****", "*****"],
    ["*****", "*****", "*****", "*****", "*****", "*****", "*****", "____|", "____|", "____|", "*****", "*****", "*****", "*****", "*****", "*****", "*****"],
    ["*****", "*****", "*****", "*****", "*****", "*****", "*****", "____|", "____|", "____|", "*****", "*****", "*****", "*****", "*****", "*****", "*****"],
    ["*****", "*****", "*****", "*****", "*****", "*****", "*****", "____|", "____|", "____|", "*****", "*****", "*****", "*****", "*****", "*****", "*****"],
    ["*****", "*****", "*****", "*****", "*****", "*****", "*****", "____|", "____|", "____|", "*****", "*****", "*****", "*****", "*****", "*****", "*****"],
    ["*****", "*****", "*****", "*****", "*****", "*****", "*****", "____|", "____|", "____|", "*****", "*****", "*****", "*****", "*****", "*****", "*****"]
]

# Función para limpiar la pantalla
def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

# Función para mostrar el tablero
def mostrar_tablero():
    limpiar()
    for fila in tablero:
        print("".join(fila))
    print()

# Función para lanzar el dado
def lanzar_dado(jugador):
    x = random.randint(1, 6)
    caras_dado = {
        1: [[" __","__","_"], ["| ", "  ", "  |"], ["| ", " o ", " |"], ["|_","__","__|"]],
        2: [[" __","__","_"], ["|o", "  ", "  |"], ["| ", "   ", " |"], ["|_","__","_o|"]],
        3: [[" __","__","_"], ["|o", "  ", "  |"], ["| ", " o ", " |"], ["|_","__","_o|"]],
        4: [[" __","__","_"], ["|o", "  ", " o|"], ["| ", "   ", " |"], ["|o","__","_o|"]],
        5: [[" __","__","_"], ["|o", "  ", " o|"], ["| ", " o ", " |"], ["|o","__","_o|"]],
        6: [[" __","__","_"], ["|o", "  ", " o|"], ["|o", "   ", "o|"], ["|o","__","_o|"]],
    }

    limpiar()
    for linea in caras_dado[x]:
        print("".join(linea))

    print(f"Has sacado un {x}")
    input("Presiona ENTER para continuar...")
    limpiar()
    if jugador == "A":
        sacar_fichaA(x)
    elif jugador == "B":
        sacar_fichaB(x)
    return x

# Función para sacar una ficha de la cárcel si se saca el número 5
def sacar_fichaA(x):
    if x == 5:
        if tablero[6][0] == " A1 |":
            tablero[0][7] = " A1 |"
            tablero[6][0] = "     "
        elif tablero[6][1] == " A2 |":
            tablero[0][7] = " A2 |"
            tablero[6][1] = "     "
        mostrar_tablero()
    else:
        seleccionar_fichaA(x)

def sacar_fichaB(x):
    if x == 5:
        if tablero[10][10] == " B1 |":
            tablero[16][9] = " B1 |"
            tablero[10][10] = "     "
        elif tablero[10][11] == " B2 |":
            tablero[16][9] = " B2 |"
            tablero[10][11] = "     "
        mostrar_tablero()
    else:
        seleccionar_fichaB(x)

# Función para mover una ficha
def mover_fichaA(pasos, x):
    matriz_jugador1 = [
        [0, 0, 0, 0, 0, 0, 0, 1, 64, 63, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 65, 62, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 66, 61, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 67, 60, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 68, 59, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 69, 58, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 70, 57, 0, 0, 0, 0, 0, 0, 0],
        [15, 14, 13, 12, 11, 10, 9, 8, 71, 56, 55, 54, 53, 52, 51, 50, 49],
        [16, 0, 0, 0, 0, 0, 0, 0, 72, 0, 0, 0, 0, 0, 0, 0, 48],
        [17, 18, 19, 20, 21, 22, 23, 24, 0, 40, 41, 42, 43, 44, 45, 46, 47],
        [0, 0, 0, 0, 0, 0, 0, 25, 0, 39, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 26, 0, 38, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 27, 0, 37, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 28, 0, 36, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 29, 0, 35, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 30, 0, 34, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 31, 32, 33, 0, 0, 0, 0, 0, 0, 0]
    ]

    ficha_found = False
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == " A1 |":
                fila_actual = i
                columna_actual = j
                valor_actual = matriz_jugador1[fila_actual][columna_actual]
                ficha_found = True  # Flag to indicate ficha was found
                break  # Break out of inner loop if ficha is found
        if ficha_found:
            break  # Break out of outer loop if ficha is found

    # Handle case where ficha is not found
    else:
        print("Ficha no se encuentra en el tablero")
        return

    fila_inicial = fila_actual
    columna_inicial = columna_actual
    ficha_id = 1 if tablero[fila_actual][columna_actual] == " A1 |" else 2

    for paso in range(pasos, x):
        # Determinar la dirección del movimiento
        if valor_actual in [1, 2, 3, 4, 5, 6, 7]:  # Moverse hacia abajo
            fila_actual += 1
        elif valor_actual in [8, 9, 10, 11, 12, 13, 14]:  # Moverse hacia la izquierda
            columna_actual -= 1
        elif valor_actual in [15, 16]:  # Moverse hacia abajo
            fila_actual += 1
        elif valor_actual in [17, 18, 19, 20, 21, 22, 23]:  # Moverse hacia la derecha
            columna_actual += 1
        elif valor_actual in [24, 25, 26, 27, 28, 29, 30]:  # Moverse hacia abajo
            fila_actual += 1
        elif valor_actual in [31, 32]:  # Moverse hacia la derecha
            columna_actual += 1
        elif valor_actual in [33, 34, 35, 36, 37, 38, 39]:  # Moverse hacia arriba
            fila_actual -= 1
        elif valor_actual in [40, 41, 42, 43, 44, 45, 46]:  # Moverse hacia la derecha
            columna_actual += 1
        elif valor_actual in [47, 48]:  # Moverse hacia arriba
            fila_actual -= 1
        elif valor_actual in [49, 50, 51, 52, 53, 54, 55]:  # Moverse hacia la izquierda
            columna_actual -= 1
        elif valor_actual in [56, 57, 58, 59, 60, 61, 62]:  # Moverse hacia arriba
            fila_actual -= 1
        elif valor_actual in [63, 64]:  # Moverse hacia la izquierda
            columna_actual -= 1
        elif valor_actual in [65, 66, 67, 68, 69, 70, 72]:  # Moverse hacia abajo
            fila_actual += 1
        elif valor_actual == 72:  # Casilla de coronación
            print("¡Coronaste una ficha!")
            tablero[fila_inicial][columna_inicial] = "____|"
            if ficha_id == 1:
                tablero[0][0] = "1****"
            else:
                tablero[0][1] = "2****"
            return

        if tablero[fila_actual][columna_actual] != "____|":
            print("¡Te comiste una ficha!")
            # Definir las variables necesarias para comer()
            k, t = fila_inicial, columna_inicial  # Posición inicial de la ficha que se mueve
            f = ficha_id  # Identificador de la ficha que se mueve
            n = 1 if tablero[fila_actual][columna_actual] == " A1 |" else 2  # Identificador de la ficha comida
            jugador = "B"  # Identificador del jugador
            comer(fila_actual, columna_actual, k, t, f, n, jugador)
        else:
            # Definir las variables necesarias para actualizar_tablero()
            x0, v0 = fila_inicial, columna_inicial  # Posición anterior
            f = ficha_id  # Identificador de la ficha
            jugador = "A"  # Identificador del jugador
            actualizar(fila_actual, columna_actual, x0, v0, f, jugador)

def mover_fichaB(pasos, x):
    matriz_jugador2 = [
        [0, 0, 0, 0, 0, 0, 0, 33, 32, 31, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 34, 0, 30, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 35, 0, 29, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 36, 0, 28, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 37, 0, 27, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 38, 0, 26, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 39, 0, 25, 0, 0, 0, 0, 0, 0, 0],
        [47, 46, 45, 44, 43, 42, 41, 40, 0, 24, 23, 22, 21, 20, 19, 18, 17],
        [48, 0, 0, 0, 0, 0, 0, 0, 72, 0, 0, 0, 0, 0, 0, 0, 16],
        [49, 50, 51, 52, 53, 54, 55, 56, 71, 8, 9, 10, 11, 12, 13, 14, 15],
        [0, 0, 0, 0, 0, 0, 0, 57, 70, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 58, 69, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 59, 68, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 60, 67, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 61, 66, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 62, 65, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 63, 64, 1, 0, 0, 0, 0, 0, 0, 0]
    ]
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == " B1 |":
                fila_actual = i
                columna_actual = j
                valor_actual = matriz_jugador2[fila_actual][columna_actual]
                break
        else:
            continue
        break
    else:
        print("Ficha no se encuentra en el tablero")
        return

    fila_inicial = fila_actual
    columna_inicial = columna_actual
    ficha_id = 1 if tablero[fila_actual][columna_actual] == " B1 |" else 2

    for paso in range(pasos):
        # Determinar la dirección del movimiento
        if valor_actual in [1, 2, 3, 4, 5, 6, 7]:  # Moverse hacia arriba
            fila_actual -= 1
        elif valor_actual in [8, 9, 10, 11, 12, 13, 14]:  # Moverse hacia la derecha
            columna_actual += 1
        elif valor_actual in [15, 16]:  # Moverse hacia arriba
            fila_actual -= 1
        elif valor_actual in [17, 18, 19, 20, 21, 22, 23]:  # Moverse hacia la izquierda
            columna_actual -= 1
        elif valor_actual in [24, 25, 26, 27, 28, 29, 30]:  # Moverse hacia arriba
            fila_actual -= 1
        elif valor_actual in [31, 32]:  # Moverse hacia la izquierda
            columna_actual -= 1
        elif valor_actual in [33, 34, 35, 36, 37, 38, 39]:  # Moverse hacia abajo
            fila_actual += 1
        elif valor_actual in [40, 41, 42, 43, 44, 45, 46]:  # Moverse hacia la izquierda
            columna_actual -= 1
        elif valor_actual in [47, 48]:  # Moverse hacia abajo
            fila_actual += 1
        elif valor_actual in [49, 50, 51, 52, 53, 54, 55]:  # Moverse hacia la derecha
            columna_actual += 1
        elif valor_actual in [56, 57, 58, 59, 60, 61, 62]:  # Moverse hacia abajo
            fila_actual += 1
        elif valor_actual in [63, 64]:  # Moverse hacia la derecha
            columna_actual += 1
        elif valor_actual in [65, 66, 67, 68, 69, 70, 72]:  # Moverse hacia arriba
            fila_actual -= 1
        elif valor_actual == 72:  # Casilla de coronación
            print("¡Coronaste una ficha!")
            tablero[fila_inicial][columna_inicial] = "____|"
            if ficha_id == 1:
                tablero[16][16] = "1****"
            else:
                tablero[16][15] = "2****"
            return

        if tablero[fila_actual][columna_actual] != "____|":
            print("¡Te comiste una ficha!")
            # Definir las variables necesarias para comer()
            k, t = fila_inicial, columna_inicial  # Posición inicial de la ficha que se mueve
            f = ficha_id  # Identificador de la ficha que se mueve
            n = 1 if tablero[fila_actual][columna_actual] == " B1 |" else 2  # Identificador de la ficha comida
            jugador = "A"  # Identificador del jugador
            comer(fila_actual, columna_actual, k, t, f, n, jugador)
        else:
            # Definir las variables necesarias para actualizar_tablero()
            x0, v0 = fila_inicial, columna_inicial  # Posición anterior
            f = ficha_id  # Identificador de la ficha
            jugador = "A"  # Identificador del jugador
            actualiza(fila_actual, columna_actual, x0, v0, f, jugador)

# Función para seleccionar una ficha de A
def seleccionar_fichaA(x):
    while True:
        limpiar()
        mostrar_tablero()
        print(f"Sacaste {x}")
        print("Selecciona qué ficha quieres mover")
        ficha = input("Si quieres mover la ficha A1 presiona 1, si quieres mover la ficha A2 presiona 2: ")

        if ficha == "1":
            ubicacion_fichaA1(x)
            break
        elif ficha == "2":
            ubicacion_fichaA2(x)
            break
        else:
            print("Opción inválida. Por favor, elige 1 o 2.")
            input("Presiona ENTER para continuar...")
            limpiar()
            continue

# Función para seleccionar una ficha de B
def seleccionar_fichaB(x):
    while True:
        limpiar()
        mostrar_tablero()
        print(f"Sacaste {x}")
        print("Selecciona qué ficha quieres mover")
        ficha = input("Si quieres mover la ficha A1 presiona 1, si quieres mover la ficha A2 presiona 2: ")

        if ficha == "1":
            ubicacion_fichaB1(x)
            break
        elif ficha == "2":
            ubicacion_fichaB2(x)
            break
        else:
            print("Opción inválida. Por favor, elige 1 o 2.")
            input("Presiona ENTER para continuar...")
            limpiar()
            continue

def ubicacion_fichaA1(x):
    for fila in range(17):
        for columna in range(17):
            if tablero[fila][columna] == " A1 |":
                print(f"La ficha A1 está en la posición: ({fila}, {columna})")
                mover_fichaA(x, x)
                return
    print("Error: No se encontró la ficha A1 en el tablero.")

def ubicacion_fichaA2(x):
    for fila in range(17):
        for columna in range(17):
            if tablero[fila][columna] == " A2 |":
                print(f"La ficha A2 está en la posición: ({fila}, {columna})")
                mover_fichaA(x, x)
                return
    print("Error: No se encontró la ficha A2 en el tablero.")

def ubicacion_fichaB1(x):
    for fila in range(17):
        for columna in range(17):
            if tablero[fila][columna] == " B1 |":
                print(f"La ficha A1 está en la posición: ({fila}, {columna})")
                mover_fichaB(x, x)
                return
    print("Error: No se encontró la ficha B1 en el tablero.")

def ubicacion_fichaB2(x):
    for fila in range(17):
        for columna in range(17):
            if tablero[fila][columna] == " B2 |":
                print(f"La ficha A2 está en la posición: ({fila}, {columna})")
                mover_fichaB(x, x)
                return
    print("Error: No se encontró la ficha B2 en el tablero.")

def comer(x, v, k, t, f, n, jugador):
    """
    Maneja la lógica cuando una ficha "come" a otra.
    :param x: Fila de la casilla destino.
    :param v: Columna de la casilla destino.
    :param k: Fila de la posición inicial de la ficha que se mueve.
    :param t: Columna de la posición inicial de la ficha que se mueve.
    :param f: Identificador de la ficha que se mueve (1 para A1/B1, 2 para A2/B2).
    :param n: Identificador de la ficha que es comida (1 para A1/B1, 2 para A2/B2).
    :param jugador: Identificador del jugador ('A' o 'B').
    """
    # Diccionario que mapea las fichas a sus posiciones iniciales (cárceles)
    carceles = {
        ('A', 1): (6, 0),  # Ficha A1 va a (6, 0)
        ('A', 2): (6, 1),  # Ficha A2 va a (6, 1)
        ('B', 1): (10, 10),  # Ficha B1 va a (10, 10)
        ('B', 2): (10, 11),  # Ficha B2 va a (10, 11)
    }

    # Obtener la posición de la cárcel para la ficha comida
    carcel_fila, carcel_columna = carceles.get((jugador, n), (None, None))

    if carcel_fila is not None and carcel_columna is not None:
        # Mover la ficha que come a la nueva posición
        actualizar(x, v, k, t, f, jugador)
        # Enviar la ficha comida a su cárcel
        tablero[carcel_fila][carcel_columna] = f" {jugador}{n} |"

        # Mostrar el tablero actualizado
        mostrar_tablero()
    else:
        print("Algo anda mal: No se encontró la cárcel para la ficha comida.")

def actualizar(x, v, x0, v0, f, jugador):
    """
    Actualiza el tablero después de mover una ficha.
    :param x: Fila de la nueva posición.
    :param v: Columna de la nueva posición.
    :param x0: Fila de la posición anterior.
    :param v0: Columna de la posición anterior.
    :param f: Identificador de la ficha (1 o 2).
    :param jugador: Identificador del jugador ('A' o 'B').
    """
    # Limpiar la posición anterior
    tablero[x0][v0] = "____|"

    # Colocar la ficha en la nueva posición
    if jugador == 'A':
        tablero[x][v] = f" A{f} |"
    elif jugador == 'B':
        tablero[x][v] = f" B{f} |"
    else:
        print("Error: Jugador no válido.")
        return

    # Mostrar el tablero actualizado
    mostrar_tablero()

def jugar_dos_jugadores():
    limpiar()
    j1 = input("Ingresa el nombre del jugador 1: ")
    j2 = input("Ingresa el nombre del jugador 2: ")

    for fila in tablero:
        print("".join(fila))
    print()

    while True:
        if tablero[0][0] == "1****" and tablero[0][1] == "2****":
            print(f"¡Ganó {j1}! Felicitaciones")
            input("Presiona Enter para continuar")
            menu()
            break

        limpiar()
        print(f"Turno de {j1}")
        input("Presiona Enter para lanzar el dado...")
        lanzar_dado("A")
        mostrar_tablero()

        if tablero[16][16] == "1****" and tablero[16][15] == "2****":
            print(f"¡Ganó {j2}! Felicitaciones")
            input("Presiona Enter para continuar")
            menu()
            break

        limpiar()
        print(f"Turno de {j2}")
        input("Presiona Enter para lanzar el dado...")
        lanzar_dado("B")
        mostrar_tablero()

# Menú principal
def menu():
    while True:
        limpiar()
        print("------ Bienvenido al PARQUÉS UN INTERACTIVO DE PHYTON ------")
        print()
        print("1. Jugar con 2 jugadores")
        print("2. Instrucciones")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            jugar_dos_jugadores()
        elif opcion == "2":
            dar_instrucciones()
            input("Presiona ENTER para continuar:")
        elif opcion == "3":
            print("Gracias por jugar. ¡Hasta luego!")
            sys.exit()
        else:
            print("Error")
        limpiar()

# Función para mostrar las instrucciones
def dar_instrucciones():
    limpiar()
    print("Instrucciones")
    print()
    print("1. Con un dado c se puede sacar maximo 1 ficha.")
    print("2. Es obligatorio primero salir de la cárcel. Si no se tienen fichas en la cárcel, la prioridad será capturar la ficha del jugador contrario.")
    print("3. Si se tiene una ficha en la cárcel y se obtiene un par (ambos dados muestran el mismo número), se saca la ficha de la cárcel y se utiliza el restante con una ficha diferente a la que salió. En caso de no tener otra ficha, se perderá ese movimiento y solo se saldrá de la cárcel.")
    print("4. Si saca un par(Los dos dados concuerden con el mismo número)le vuelve a tirar.")
    print("5. Solo se permiten dos fichas máximo por cada casilla.")
    print("6. Si una ficha se encuentra en una salida o en un seguro, esta ficha no puede ser capturada por ninguna otra. Esta regla no se cumple cuando una ficha se encuentra en la salida de un equipo enemigo junto a una ficha del equipo enemigo y el equipo enemigo saca una ficha en su turno, éste capturará a la ficha que no pertenece a dicha salida.")
    print("7. Si dos fichas se encuentran en una casilla, tenemos estas posibilidades:")
    print("a) Son del mismo color/equipo, y por ende, forman un bloqueo siempre.")
    print("b) Son de diferente color/equipo pero se encuentran en un seguro o en una salida y entonces forman un bloqueo.")
    print("c) Son de diferente equipo y no se encuentran en ninguna casilla especial, por lo que la que la ficha que llega en segundo lugar a la casilla captura a laprimera ficha y la envía a su respectiva cárcel.")
    print("8. Si no existe un movimiento posible para ninguna de las fichas, ya sea porque existe un bloqueo o porque la casilla de llegada está a menos movimientos de lo que se obtuvo en los dados, entonces el turno simplemente pasa.")
    print("9. Si una ficha es coronada, se le concederán 10 movimientos adicionales con otra ficha, siempre que sea permitido. Si se captura una ficha, se le otorgarán 20 movimientos adicionales con la ficha que elija, si es posible. Estos movimientos extra se aplican inmediatamente al coronar una ficha o al capturar una ficha.")
    print("10. Si un jugador obtiene tres pares consecutivos, coronará inmediatamente la ficha más adelantada que tenga. (Si solo tiene una ficha, ganará la partida).")
    print("11.Un jugador no puede bloquear una casilla por más de dos turnos; al tercer turno, estará obligado a mover una de sus fichas de bloqueo.")
    print("12. Gana quien logre coronar todas sus fichas primero, momento en el cual la partida terminará.")
    print()
    input("Presione ENTER para regresar al menú")
    limpiar()
    menu()

# Iniciar el juego
menu()
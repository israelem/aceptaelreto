import numpy as np


def sumar_caminos(caminos, tamaño, fila, columna):
    abajo = 0
    izquierda = 0
    if fila + 1 < tamaño:
        abajo = caminos[fila + 1, columna]
    if columna - 1 >= 0:
        izquierda = caminos[fila, columna - 1]
    suma = abajo + izquierda + caminos[fila, columna]
    return suma


def calcular_caminos(tablero, tamaño):
    caminos = np.zeros((tamaño, tamaño), int)
    caminos[tamaño - 1, 0] = 1
    for fila in range(tamaño - 1, -1, -1):
        for columna in range(tamaño):
            if tablero[fila][columna] != 'X':
                caminos[fila, columna] = sumar_caminos(caminos, tamaño, fila, columna)
    return caminos[0, tamaño - 1]


if __name__ == "__main__":
    respuestas = []
    tamaño = int(input())
    while tamaño:
        tablero = []
        for x in range(tamaño):
            tablero.append(list(input()))
        respuestas.append(calcular_caminos(tablero, tamaño))
        tamaño = int(input())
    for respuesta in respuestas:
        print(respuesta)

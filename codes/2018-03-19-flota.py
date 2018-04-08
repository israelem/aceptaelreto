import numpy as np
from collections import Counter


def iguales(diccionario_1, diccionario_2):
    pass
    return True


def comprobar_barcos(oceano, cuenta_barcos):
    barcos_oceano = {}
    tamaño = 0
    respuesta = False
    for fila in range(oceano.shape[0]):
        for casilla in oceano[fila, :]:
            if casilla == 0:
                if tamaño > 1:
                    if tamaño in barcos_oceano:
                        barcos_oceano[tamaño] += 1
                    else:
                        barcos_oceano[tamaño] = 1
                tamaño = 0
            else:
                tamaño += 1
    for columna in range(oceano.shape[1]):
        for casilla in oceano[:, columna]:
            if casilla == 0:
                if tamaño > 1:
                    if tamaño in barcos_oceano:
                        barcos_oceano[tamaño] += 1
                    else:
                        barcos_oceano[tamaño] = 1
                tamaño = 0
            else:
                tamaño += 1

    if iguales(barcos_oceano, cuenta_barcos) == 0:
        respuesta = True
    return respuesta


if __name__ == '__main__':
    respuestas = []
    numero_barcos = int(input())
    while numero_barcos > 0:
        lista_barcos = [int(x) for x in input().split()]
        cuenta_barcos = Counter(lista_barcos)
        tamaño_oceano = int(input())
        oceano = []
        for fila in range(tamaño_oceano):
            oceano.append([int(x) for x in input().split()])
        oceano = np.array(oceano)
        if comprobar_barcos(oceano, cuenta_barcos):
            respuestas.append('SI')
        else:
            respuestas.append('NO')
        numero_barcos = int(input())
    for respuesta in respuestas:
        print(respuesta)

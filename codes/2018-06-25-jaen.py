import numpy as np
from itertools import product


def vacío(mapa):
    vacío = True
    for fila, columna in list(product(range(mapa.shape[0]), range(mapa.shape[1]))):
        vacío = vacío and mapa[fila, columna] == ' '
    return vacío


def calcular_contiguos(mapa, lista_puntos, inicio):
    if mapa[inicio[0], inicio[1]] == ' ':
        lista_puntos.remove(inicio)
        return 0
    elif mapa[inicio[0], inicio[1]] == '#':
        mapa[inicio[0], inicio[1]] = ' '
        lista_puntos.remove(inicio)
        contiguos_fila = 0
        contiguos_columna = 0
        if [inicio[0] + 1, inicio[1]] in lista_puntos:
            contiguos_fila = calcular_contiguos(mapa, lista_puntos, [inicio[0] + 1, inicio[1]])
        if [inicio[0], inicio[1] + 1] in lista_puntos:
            contiguos_columna = calcular_contiguos(mapa, lista_puntos, [inicio[0], inicio[1] + 1])
        return 1 + contiguos_fila + contiguos_columna

if __name__ == '__main__':
    soluciones = []
    filas, columnas = [int(x) for x in input().split()]
    while filas and columnas:
        mapa = np.empty([filas, columnas], str)
        for fila in range(filas):
            mapa[fila, :] = [c for c in input()]
        lista_parcelas = []
        lista_puntos = [[x, y] for x, y in
                        list(product(range(mapa.shape[0]),
                                     range(mapa.shape[1])))]
        while not vacío(mapa):
            lista_parcelas.append(calcular_contiguos(mapa, lista_puntos, lista_puntos[0]))
        soluciones.append(max(lista_parcelas))
        filas, columnas = [int(x) for x in input().split()]
    for solución in soluciones:
        print(solución)

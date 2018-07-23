import numpy as np


def calcular_camino_mas_largo(mapa, inicio=(0, 0)):
    if not (inicio[0] < mapa.shape[0] and inicio[1] < mapa.shape[1]):
        return 0
    elif mapa[inicio[0], inicio[1]] == '#':
        mapa[inicio[0], inicio[1]] = ' '
        return 1 + calcular_camino_mas_largo(mapa, [inicio[0] + 1, inicio[1]]) + \
               calcular_camino_mas_largo(mapa, [inicio[0], inicio[1] + 1])
    else:
        return max(calcular_camino_mas_largo(mapa, [inicio[0] + 1, inicio[1]]),
                   calcular_camino_mas_largo(mapa, [inicio[0], inicio[1] + 1]))


if __name__ == '__main__':
    soluciones = []
    filas, columnas = [int(x) for x in input().split()]
    while filas and columnas:
        mapa = np.empty([filas, columnas], str)
        for fila in range(filas):
            mapa[fila, :] = [c for c in input()]
        soluciones.append(calcular_camino_mas_largo(mapa))
        filas, columnas = [int(x) for x in input().split()]
    for solución in soluciones:
        print(solución)

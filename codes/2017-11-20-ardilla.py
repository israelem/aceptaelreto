import numpy as np
from itertools import product

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, punto):
        return self.x == punto.x and self.y == punto.y


def hay_camino(mapa, salto, inicio=Punto(0, 0)):
    if inicio.x == mapa.shape[0] and inicio.y == mapa.shape[1]:
        return True
    else:
        lista_puntos = [Punto(x, y) for x, y in
                        list(product(range(inicio.x, inicio.x + salto + 1), range(inicio.x, inicio.x + salto + 1)))]
        posición = 0
        while posición < len(lista_puntos) and mapa[lista_puntos[posición].x, lista_puntos[posición].y] == '':
            posición += 1
        if posición == len(lista_puntos):
            return False
        else:
            return hay_camino(mapa, salto, lista_puntos[posición])


if __name__ == '__main__':
    soluciones = []
    filas, columnas, salto, árboles = [int(x) for x in input().split()]
    while filas and columnas:
        filas += 1
        columnas += 1
        mapa = np.empty([filas, columnas], str)
        mapa[0, 0] = mapa[filas - 1, columnas - 1] = 'A'
        cortados = []
        for _ in range(árboles):
            fila, columna = [int(x) for x in input().split()]
            cortados.append(Punto(fila, columna))
            mapa[fila, columna] = 'A'
        cortado = None
        while hay_camino(mapa, salto) and cortados:
            cortado = cortados[0]
            cortados = cortados[1:]
            mapa[cortado.x, cortado.y] = ''
        if not cortado:
            soluciones.append('NUNCA SE PUDO')
        else:
            soluciones.append(cortado)
        filas, columnas, salto, árboles = [int(x) for x in input().split()]

import numpy as np

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def hay_camino(mapa, salto, inicio = Punto(0, 0)):
    pass

if __name__ == '__main__':
    soluciones = []
    filas, columnas, salto, árboles = [int(x) for x in input().split()]
    while filas and columnas:
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

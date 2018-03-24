import numpy as np
from collections import Counter

def comprobar_barcos(oceano, cuenta_barcos):
    barcos_oceano = {}
    tamaño = 0
    for fila in range(oceano.shape[0]):


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

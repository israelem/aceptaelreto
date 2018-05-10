import numpy as np

respuestas = []
tamaño = (int(input()))
while tamaño:
    matriz = []
    for _ in range(tamaño):
        matriz.append([int(x) for x in input().split()])
    matriz = np.array(matriz, dtype=int)
    identidad = np.identity(tamaño, int)
    if np.array_equal(matriz, identidad):
        respuestas.append('SI')
    else:
        respuestas.append('NO')
    tamaño = int(input())

for respuesta in respuestas:
    print(respuesta)

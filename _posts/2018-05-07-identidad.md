---
layout: post
title: ¿Es matriz identidad?
---

Se dice que una matriz es _identidad_ cuando todos sus elementos son cero a excepción de la diagonal principal, que se encuentra rellena de unos.

Para que una matriz sea identidad debe de ser _cuadrada_, es decir, tener el mismo número de filas que de columnas.

# Entrada

La entrada consta de una serie de casos de prueba. Cada uno comienza con un número que representa el número de filas, como máximo 50, de una matriz cuadrada. Tras él, aparecen los elementos que forman la matriz, que serán valores entre -1.000 y 1.000 (incluídos).

La entrada terminará con una matriz de 0 filas.

# Salida

Para cada caso de prueba se indicará SI si la matriz es identidad y NO en caso contrario.

# Entrada de ejemplo

```
3
1 0 0
0 1 0
0 0 1
2
0 1
1 0
5
1 0 0 0 0
0 5 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
0
```

# Salida de ejemplo

```
SI
NO
NO
```
# Solución propuesta

``` python
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
```

[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2018-05-7-identidad.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=151)

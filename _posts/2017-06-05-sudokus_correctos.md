---
layout: post
title: Sudokus corretos
---

El sudoku es un pasatiempo lógico que consiste en rellenar una cuadrícula de 9×9 casillas dividida en nueve regiones 3×3 (las separadas con líneas más gruesas en la imagen) con los números del 1 al 9 de tal forma que no se repitan números en ninguna fila, columna o región. El sudoku inicialmente se presenta con algunas casillas ya rellenas, a modo de pistas, y el jugador debe deducir los valores de las casillas vacías. Si el sudoku está bien planteado, la solución es única.

Dado un sudoku completamente relleno, ¿sabrías construir un programa que comprobara si es correcto (es decir, cada fila, columna o región contiene los números del 1 al 9 exactamente una vez)?

# Entrada

La entrada comienza con un número que representa el número de casos de prueba que vendrán a continuación.

Cada caso de prueba está formado por 9 líneas, cada una con 9 números entre el 1 y el 9 separados por espacios, que representan un sudoku completamente relleno.

# Salida

Para cada caso, se escribirá una línea con la palabra SI si el sudoku ha sido resuelto correctamente, y NO en caso contrario.

# Entrada de ejemplo

```
1
4 1 3 8 2 5 6 7 9
5 6 7 1 4 9 8 3 2
2 8 9 7 3 6 1 4 5
1 9 5 4 6 2 7 8 3
7 2 6 9 8 3 5 1 4
3 4 8 5 1 7 2 9 6
8 5 1 6 9 4 3 2 7
9 7 2 3 5 8 4 6 1
6 3 4 2 7 1 9 5 8
```

# Salida de ejemplo

```
SI
```
# Solución propuesta

``` python
def f_leer_sudoku():
    r_sudoku = []
    # f = open("sudoku.txt", "r")
    for iteracion in range(9):
        # l_str = f.readline().split(' ')
        l_str = str(input()).split(' ')
        r_sudoku.append([int(x) for x in l_str])
    # f.close()
    return r_sudoku


def f_comprobar_linea(p_linea):
    return list(range(1, 10)) == sorted(p_linea)

if __name__ == '__main__':
    correcto = True
    columnas = [[] for i in range(9)]
    cuadrantes = [[] for i in range(9)]
    posicion_fila = 0
    veces = int(input())
    for vez in range(veces):
        sudoku = f_leer_sudoku()
        for fila in sudoku:
            correcto = correcto and f_comprobar_linea(fila)
            posicion_columna = 0
            for casilla in fila:
                columnas[posicion_columna].append(casilla)
                posicion_cuadrante = (posicion_fila // 3) * 3 + (posicion_columna // 3)
                cuadrantes[posicion_cuadrante].append(casilla)
                posicion_columna += 1
            posicion_fila += 1
        for fila in columnas:
            correcto = correcto and f_comprobar_linea(fila)
        for fila in cuadrantes:
            correcto = correcto and f_comprobar_linea(fila)
        if correcto:
            print("SI")
        else:
            print("NO")
```


[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2017-06-05-sudokus_correctos.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=345&potw=1)

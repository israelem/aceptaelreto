---
layout: post
title: Temperaturas extremas
---

La Agencia Estatal de Meteorología (AEMET) actualiza diariamente el Banco Nacional de Datos Climatológicos, en el que se almacenan las observaciones climatológicas (precipitación y temperatura) realizadas en España desde hace unos 150 años.

Nuria está estudiando la relación entre la variabilidad de la temperatura y el estado hídrico del suelo en una región de secano en España. Para ello, acude al Banco y solicita los registros de temperaturas en dicha zona año a año desde que existen registros.

En la primera fase de su estudio pretende determinar el número de picos y valles en las temperaturas en un determinado periodo de tiempo. Una temperatura se considera pico (resp. valle) en una secuencia cuando la anterior y la siguiente en la secuencia son estrictamente menores (resp. mayores).

# Entrada

La primera línea contiene un número que indica el número de casos de prueba que aparecen a continuación.

Cada caso de prueba se compone de dos líneas. La primera de ellas tiene un único entero con el número de temperaturas registradas (mayor que 0 y menor o igual que 10.000), mientras que la segunda línea contiene la secuencia de temperaturas (números enteros entre −50 y 60 grados centígrados).

# Salida

Para cada caso de prueba se escribirá el número de picos y de valles, separados por un espacio y seguidos de un salto de línea.

# Entrada de ejemplo

```
4
5
7 5 3 8 9
8
8 9 7 6 5 3 4 2
2
3 -5
8
4 -1 5 3 7 7 6 8
```

# Salida de ejemplo

```
0 1
2 1
0 0
1 3
```
# Solución propuesta

``` python
if __name__ == '__main__':
    soluciones = []
    numero_casos = int(input())
    for caso in range(numero_casos):
        casos = [int(x) for x in input().split(' ')]
        temperaturas = [int(x) for x in input().split(' ')]
        picos = 0
        valles = 0
        for i in range(1, len(temperaturas)-1):
            if temperaturas[i - 1] < temperaturas[i] > temperaturas[i + 1]:
                picos += 1
            elif temperaturas[i - 1] > temperaturas[i] < temperaturas[i + 1]:
                valles += 1
        soluciones.append("%d %d" % (picos, valles))
    for solucion in soluciones:
        print(solucion)
```

La complejidad de este problema es la de tener cuidado con los índices de un
array o lista. Por eso el for va desde 1 a la longitud (tamaño) menos 1, ya que
la función range realmente desde el valor inicial al final-1.

Por cada elemento, hemos de compararlo con el de la izquierda y el de la derecha,
y si cumple ser un pico, sumar 1 o si es un valle, sumar 1 a dicha variable.

Otro ejercicio relativamente sencillo.

[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2017-09-18-temperaturas.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=314&potw=1)

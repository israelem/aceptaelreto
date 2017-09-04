---
layout: post
title: Saliendo de la crisis
---

La abeja reina dijo hace unos cuantos meses que la colmena estaba por fin saliendo de la crisis. Ahora Maya quiere comprobar cómo de ciertas eran aquellas declaraciones, así que ha recopilado el histórico de distintos indicadores económicos desde el día de la declaración hasta hoy para ver si, efectivamente, todos ellos han ido creciendo día a día desde entonces.

# Entrada

La entrada estará compuesta de distintos indicadores económicos, cada uno de ellos en dos líneas distintas. La primera línea indica el número de muestras recogidas del indicador (0 < n ≤ 100). La segunda línea contiene n números positivos con los valores económicos (entre 1 y 10.000.000) medidos desde el día de la declaración de la abeja reina hasta el día de hoy.

La entrada termina con un indicador sin muestras (0) que no debe procesarse.

# Salida

Por cada caso de prueba se dirá si según ese indicador la abeja reina tenía razón (SI) o las cosas no están tan bien como ella cree (NO).

# Entrada de ejemplo

```
3
1 3 6
4
1 3 2 5
3
6 6 6
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
if __name__ == '__main__':
    respuestas = []
    numero_muestras = int(input())
    while numero_muestras != 0:
        salida = True
        indicadores = [int(x) for x in input().split(' ')]
        anterior = indicadores[0]
        posicion = 1
        while posicion < len(indicadores) and anterior < indicadores[posicion]:
            anterior = indicadores[posicion]
            posicion += 1
        if posicion == len(indicadores):
            respuestas.append('SI')
        else:
            respuestas.append('NO')
        numero_muestras = int(input())
    for respuesta in respuestas:
        print(respuesta)

```

En este ejercicio, lo imporante es el uso de los bucles. Ya que lo único que debemos
comprobar es que el valor dado es mayor estrictamente que el anterior. En este caso
hacemos uso de un while donde vamos un paso por delante, ya que debemos comparar
cada valor con el anterior, sin embargo, en la primera comparación. ¿Quién es el
anterior? Pues ni más ni menos que el primero, es decir, el que ocupa la posición 0, 
de modo que el que hace la vez de siguiente es el segundo elemento de la lista, o 
dicho de otra forma, el que ocupa la posición 1. A partir de ahí comparamos el
anterior con el siguiente.

El resto ya se puede dar por conocido. Si tenéis alguna duda, no  tenéis más que
escribir en este blog.

[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2017-08-21-saliendo_crisis.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=247&potw=1)

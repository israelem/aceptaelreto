---
layout: post
title: Distancia al siguiente capicúa
---

Los *números capicúa* son aquellos que, tras ser escritos, se leen igual de izquierda a derecha que de derecha a izquierda. Por ejemplo,
los números 11, 474 o 9.889 son capicúa.

Como ocurre con los números primos, entre los números bajos hay muchos números capicúa. Los primeros son el 0, 1, 2, …, 9, que están todos
a distancia 1. Más adelante llegan el 11, 22, 33, …, 99 que están a distancia 11. El siguiente, sin embargo, vuelve a estar cerca: el 101
está sólo a distancia 2 del anterior.

¿Eres capaz de saber a qué distancia está el siguiente capicúa de un número dado?

# Entrada

La entrada comienza con una línea indicando el número de casos de prueba que vienen a continuación.

Cada caso de prueba es un número mayor o igual que 0 y menor o igual que 2.000.000.000.

# Salida

Para cada caso de prueba se indicará la distancia del número al siguiente capicúa. Ten en cuenta que si el número leído resulta ser
capicúa él mismo, habrá que indicar la distancia al siguiente.

# Entrada de ejemplo

```
8
27
179
```

# Salida de ejemplo

```
1
6
2
```
# Solución propuesta

``` python
def capicua(numero):
    return  numero == numero[::-1]

if  __name__ == '__main__':
    inicio = int(input())
    numero = inicio + 1
    while not capicua(str(numero)):
        numero += 1
    print(numero - inicio)
```

Este código muestra la potencia de Python para manejar listas o en este caso
cadenas de caracteres, ya que en otros lenguajes deberíamos haber realizado la
cadena inversa de recorriendo cada posición. Sin embargo, en Python tenemos la
posibilidad de realizar esto con una sola instrucción, en este caso la siguiente:

``` python
s[i:j:k]
```

El resultado es la porción de *s* desde *i* a *j* con un paso de *k*. En el
código que se propone como solución, las variables o índices *i* y *j* no están
indicados, además, que el paso *k* es negativo, de forma que lo que devuelve es
la cadena entera, pero justo del revés que es lo que nos interesa.

[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2017-05-29-distancia_capicua.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=348&potw=1)

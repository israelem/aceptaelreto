---
layout: post
title: El triángulo de mayor área
---

A partir de dos segmentos de cualquier longitud, es posible formar un triángulo añadiendo un tercero. De hecho, podremos formar un número 
infinito de triángulos dependiendo del ángulo que formemos con los dos segmentos originales:

![Triángulos](https://www.aceptaelreto.com/pub/problems/v003/50/st/statements/Spanish/Triangulos.svg)

De todos esos triángulos hay uno especial por ser el de mayor área. ¿Sabes encontrarlo?

# Entrada

El programa deberá procesar múltiples casos de prueba, cada uno recibido en una línea por la entrada estándar.

Un caso de prueba estará formado por una pareja de números naturales mayores que 0 y menores que 1.000, cada uno indicando la longitud de uno de los segmentos. La entrada terminará con un caso de prueba especial, que no deberá procesarse, en el que ambos números serán 0.

# Salida

Para cada caso de prueba el programa escribirá, en una línea, el área del mayor triángulo que se pueda formar con los dos segmentos. La salida se redondeará a un único decimal.

# Entrada de ejemplo

```
23 13
16 29
0 0
```

# Salida de ejemplo 

```
149.5
232.0
```

Autores:	Pedro Pablo Gómez Martín; Marco Antonio Gómez Martín; Alberto Verdejo

# Solución propuesta

``` python
import math

def f_area(a, b, c):
    sol = 0
    s = (a + b + c)/2
    r = s*(s - a)*(s - b)*(s - c)
    if  r > 0:
        sol = math.sqrt(r)
    return sol

a, b = str(input()).split(" ")
a = int(a)
b = int(b)
while(a != 0 and b != 0):
    c = 1
    area = f_area(a, b, c)
    max = 0
    while (max == 0 or area > max):
        c += 1
        max = area
        area = f_area(a, b, c)
    print(round(area,1))
    a, b = str(input()).split(" ")
    a = int(a)
    b = int(b)

```

En la solución propuesta se supone que cada aumento del lado desconocido va a suponer un aumento del área del triángulo hasta alcanzar el área máxima, a partir de la cual el área resultante una vez aumetnado el lado será menor que el anterior.

Además, para calcular el área del triángulo, dado que desconocemos la altura del triángulo, no podemos utilizar la más conocida A = (b\*h)/2. En este caso debemos usar la [fórmula de Herón](https://es.wikipedia.org/wiki/F%C3%B3rmula_de_Her%C3%B3n), que utiliza solo los tres lados para calcular el área.

[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2017-05-22-triangulo_mayor.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/pub/problems/v003/50/st/statements/Spanish/index.html)

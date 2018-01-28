---
layout: post
title: San Fermines
---

Un buen corredor de San Fermines intenta mantener la emoción para fomentar el espectáculo. Este tipo de corredores está muy en forma y son capaces de correr mucho más deprisa que los toros. Sin embargo, para mantener la emoción, no lo hacen. Se limitan a mantener una velocidad adecuada para que los toros se mantenga siempre cerca, pero no lleguen a pillarles.

El problema consiste en, dadas las velocidades de todos los toros que participan en los San Fermines (y que se suponen constantes), ¿a qué velocidad deben ir estos corredores expertos para mantener el espectáculo conservando su integridad?

# Entrada

La entrada consta de una serie de casos de prueba, cada uno en una línea. El primer número de la misma indica el número de toros que intervienen en la carrera (_n_ ≥ 1). A continuación aparece un entero por cada uno de los toros, indicando la velocidad a la que correrá ese toro (recuerda, es velocidad constante). La velocidad es siempre positiva y no excede 1.000.000.000.

# Salida

Para cada caso de prueba se mostrará una línea en la que aparecerá la velocidad a la que deberán ir los corredores expertos para mantener el espectáculo.

# Entrada de ejemplo

```
7 1 9 8 7 10 3 12
1 10
```

# Salida de ejemplo

```
12
10
```
# Solución propuesta

``` python

if __name__ == '__main__':
    velocidades = [int(x) for x in input().split(' ')]
    velocidades = velocidades[1:]
    print(max(velocidades))

```

[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2017-12-11-san_fermines.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=149)

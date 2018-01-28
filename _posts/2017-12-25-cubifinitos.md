---
layout: post
title: Números cubifinitos
---

Se dice que un número es cubifinito cuando al elevar todos sus dígitos al cubo y sumarlos el resultado o bien es 1 o bien es un número cubifinito.

Por ejemplo, el número 1243 es cubifinito, pues al elevar todos sus dígitos al cubo obtenemos 100 que es cubifinito.

Por su parte, el 513 no es cubifinito, pues al elevar al cubo sus dígitos conseguimos el 153 que nunca podrá ser cubifinito, pues la suma de los cubos de sus dígitos vuelve a dar 153.

Dado un número, se trata de determinar si éste es o no cubifinito.

# Entrada

La entrada consta de una serie de casos de prueba terminados con un número 0. Cada caso de prueba es una línea con un número positivo no mayor que 10.000.000.

# Salida

Para cada caso de prueba se mostrará una única línea en la que aparecerá la serie de transformaciones del número original hasta el 1 o hasta la repetición de un número de la serie. Tras eso se indicará la conclusión a la que se llega: si el número es cubifinito o no.

Mira el ejemplo de la salida para ver el formato esperado exacto.

# Entrada de ejemplo

```
1
10
1243
513
0
```

# Salida de ejemplo

```
1 -> cubifinito.
10 - 1 -> cubifinito.
1243 - 100 - 1 -> cubifinito.
513 - 153 - 153 -> no cubifinito.
```
# Solución propuesta

``` python


```

[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2017-12-25-cubifinitos.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=139)

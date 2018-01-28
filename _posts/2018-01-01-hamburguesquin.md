---
layout: post
title: Hamburguesquín
---

El éxito y expansión de la conocida marca de restaurantes de comida rápida _Hamburguesquín_ no tiene precedentes. En poco tiempo ha llenado la ciudad con locales por todas partes. Ahora sus dueños se están planteando reducir el número de restaurantes, pero obviamente sin perder clientes.

Han detectado que por ejemplo en la calle _Gran Vía_ hay opciones de eliminar algún restaurante. Para hacerlo con garantías, han estudiado el área de influencia de cada restaurante en esa calle, es decir, los puntos de la calle tales que si alguien con hambre se encontrara ahí acudiría a dicho restaurante. Formalmente, si x es la localización del restaurante en la calle (0 ≤ _x_ ≤ _L_, donde _L_ es la longitud de la calle), el área de influencia es el intervalo [_x − r, x + r_], donde _r_ es el radio de influjo del restaurante (algo que depende de cada restaurante).

Ahora te han contratado para que, con esa información, les digas cuántos restaurantes como máximo podrían cerrar sin dejar de cubrir ningún punto de la calle. Por el mismo precio quieren también que les digas si hay puntos en la calle no cubiertos, porque en ese caso se plantearían mover algún restaurante de sitio.

# Entrada

La entrada consiste en varios casos de prueba. La primera línea de cada caso contiene dos enteros: _L_ es la longitud de la calle (1 ≤ _L_ ≤ 10<sup>9</sup>) y _N_ es el número de restaurantes (0 ≤ _N_ ≤ 200.000). A continuación aparecen _N_ líneas, cada una con dos enteros: la posición _x<sub>i</sub>_ de un restaurante (0 ≤ _x<sub>i</sub>_ ≤ _L_) y su radio de influjo _r<sub>i</sub>_ (0 < _r<sub>i</sub>_ ≤ _L_).

# Salida

Para cada caso de prueba se escribirá una línea con el máximo número de restaurantes que se pueden cerrar de tal forma que todo punto de la calle siga bajo la influencia de algún restaurante no cerrado. En caso de que haya puntos de la calle no cubiertos por ningún restaurante, se escribirá -1 para indicar la situación (en vez del número de restaurantes a cerrar).

# Entrada de ejemplo

```
10 4
5 3
3 3
9 2
8 2
5 2
1 1
4 1
```

# Salida de ejemplo

```
2
-1
```
# Solución propuesta

``` python


```

[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2018-01-01-hamburguesquin.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=421)

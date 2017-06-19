---
layout: post
title: Más listos que el hambre
---
En el laboratorio estamos realizando una serie de experimentos para estudiar la inteligencia de una especie de ratones, los ratones coloraos. En los experimentos colocamos a unos ratones en una caja rectangular dividida en celdas como la de la figura. Los ratones se colocan en la esquina inferior izquierda y deben encontrar la salida situada en la esquina superior derecha. Para ello pueden moverse libremente por todas las celdas, pero de cada celda solamente pueden pasar a las colindantes en horizontal o vertical.

![Laberinto](https://www.aceptaelreto.com/pub/problems/v003/98/st/statements/Spanish/laberinto.svg)

Para estos ratones eso está chupado, por lo que hemos ido complicando el experimento. Primero pusimos una serie de botones (círculos rojos en la figura) en algunas celdas de tal forma que los ratones tuvieran que pulsar todos esos botones para que se abriera la puerta de la salida. Pronto aprendieron a hacerlo, y además de la forma más rápida posible.

Para potenciar el trabajo en equipo, ahora hemos numerado los botones del 1 al *N*, y además han sido electrificados[^1]. Para que el botón i sirva para abrir la puerta, y además no suelte una descarga eléctrica, deben haberse pulsado antes los botones con un número menor. En el experimento se colocan dos ratones en la celda inicial y ambos deben colaborar pulsando los botones en orden para lograr salir del laberinto en el menor tiempo posible. No hay más restricciones sobre qué botones pulsa cada ratón, salvo que si un ratón pulsa el botón *i*, antes él o su compañero deben haber pulsado el botón *i* − 1. Si lo logran encontrarán un suculento queso en la salida. Si no, solamente tendrán pan duro.

Nosotros somos mucho menos listos que los ratones y no sabemos si lo están haciendo en el mejor tiempo. ¿Nos puedes ayudar a calcularlo suponiendo que un ratón siempre tarda 1 segundo en pasar de una celda a otra colindante? El tiempo que tarda un ratón en pulsar un botón es despreciable, por lo que en el mismo segundo un ratón podría pulsar el botón *i* y el otro el botón *i* + 1. Ten en cuenta que la presencia de un botón en una celda no impide que un ratón pueda pasar por ella sin pulsarlo.

# Entrada

La entrada está compuesta por una serie de casos. Para cada caso, la primera línea contiene el número F de filas y el número C de columnas del entramado de celdas que contiene la caja (ambos números pueden estar entre 1 y 50). La siguiente línea contiene el número N de botones (entre 0 y 100) que deben pulsarse. En las siguientes *N* líneas se dan las posiciones de estos botones (una fila entre 1 y *F* y una columna entre 1 y *C*) en el orden en que tienen que ser pulsados.

# Salida

Para cada caso se escribirá el tiempo mínimo que necesitan los dos ratones situados inicialmente en la celda (1,1) para salir de la caja habiendo pulsado todos los botones sin haber recibido ninguna descarga. Una vez alcanzada la celda (*F*,*C*), si la puerta de salida está abierta, los ratones pueden salir con 1 segundo más.

# Entrada de ejemplo

```
4 6
3
2 4
2 6
4 2
3 3
4
2 1
1 2
3 1
1 3
```

# Salida de ejemplo

```
11
5
```
# Solución propuesta

``` python

```

[^1]: En la elaboración de este problema ningún animal ha sufrido daños. Se ha tenido un escrupuloso cuidado en respetar los derechos de los animales y las leyes contra el maltrato animal.

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=398&potw=1)

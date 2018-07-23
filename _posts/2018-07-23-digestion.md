---
layout: post
title: La digestión de las serpientes
---

Por todos es sabido que las serpientes son animales de "sangre fría", que significa que no son capaces de regular su temperatura corporal y que por tanto dependen de la temperatura ambiental para sobrevivir[^1].

Para incrementar su temperatura interna suelen tomar el sol en rocas u otros tipos de suelos que transmitan bien el calor. De esta forma consiguen subir su temperatura en un corto espacio de tiempo y pueden volver a lugares seguros donde son menos visibles.

Aunque son capaces de sobrevivir con temperaturas bajas, en ciertos momentos les resulta imprescindible mantener una temperatura corporal elevada. Uno de esos momentos es durante la caza: la temperatura elevada les proporciona la energía necesaria para la actividad. Otro momento importante es inmediatamente después, durante la digestión. En caso de que sus cuerpos sufrieran un enfriamiento, la presa engullida podría pudrirse y terminar matándolas "desde dentro".

Debido a esto, las serpientes deben planificar muy bien cuándo salir de caza. Necesitan buscar el momento del día en el que la temperatura ambiente se mantiene por encima de un umbral por más tiempo; eso les garantiza que tendrán tiempo suficiente para calentarse, buscar la presa, cazarla y digerirla.

Como miembros del equipo de apoyo de los biólogos australianos que estudian la fauna local, debemos comprobar si las serpientes escogen el momento de caza de forma óptima o no. Nuestra primera tarea es analizar la secuencia de temperatura ambiente de un día y encontrar la duración del periodo más largo en la que esa temperatura se mantiene lo suficientemente elevada. Eso sí, las serpientes tienen cierta tolerancia y admiten pequeños intervalos de tiempo con temperaturas por debajo del umbral deseado.

[^1]: En realidad en un contexto científico, el término "sangre fría" y "sangre caliente" ya no se utiliza directamente, pues se ha visto que los tipos de temperatura corporal no son tan simples como para utilizar únicamente esas dos categorías.

# Entrada

La entrada estará compuesta por distintos casos de prueba, cada uno ocupando dos líneas.

La primera línea de cada caso de prueba tendrá dos enteros, el primero indicando el número de mediciones realizadas (1 ≤ n ≤ 100.000), y el segundo el número k de mediciones consecutivas por debajo del umbral que una serpiente es capaz de soportar entre dos mediciones con temperaturas altas.

La segunda línea contiene n números que serán siempre ceros o unos. Un cero indica una temperatura demasiado baja para la serpiente para calentarse, mientras que un uno indica una temperatura aceptable.

La entrada termina con una línea con dos ceros, que no deberá procesarse.

# Salida

Por cada caso de prueba se escribirá la longitud del periodo más largo (medido en número de muestras) que tiene la serpiente para comer.

Un periodo es válido si comienza y termina por unos y entre dos lecturas con temperaturas por encima del umbral no hay más de k medidas consecutivas con temperaturas por debajo.

# Entrada de ejemplo

```
6 0
0 1 0 1 0 0
6 0
0 1 0 1 1 0
8 1
1 0 0 1 0 1 0 1
0 0
```

# Salida de ejemplo

```
1
2
5
```

# Solución propuesta

``` python

```

[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2018-07-23-digestion.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=444)

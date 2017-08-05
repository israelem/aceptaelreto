---
layout: post
title: Tres dedos en cada mano
---

Si nos fijamos en los personajes de ficción de dibujos es curioso ver el número de dedos que tienen. Muchos de ellos tienen cinco, pues el dibujante se ha tomado la molestia de hacer la mano en detalle. Ejemplos de personajes con cinco dedos en cada mano son Mortadelo, Lucky Luke, Asterix o Tintín.

También abundan personajes con cuatro dedos en cada mano, como el ratón Mickey, Mafalda, Roger Rabbit, el oso Yogui o los simpáticos Tom y Jerry. Manos de cuatro dedos también aparecen en otros personajes no dibujados como E.T. y Alf.

Pero si nos salimos de los cuatro o cinco dedos, el número de personajes distintos empieza a escasear. Con un único dedo podríamos hablar, quizá, del capitán Garfio. Con dos dedos nos encontramos a los graciosos playmobil y con tres dedos a Bender, el robot de Futurama.

No nos atrevemos a dar una explicación de por qué esta preferencia de cuatro o cinco dedos frente a cantidades más imaginativas. Lo que sí tenemos claro es que esos personajes con cuatro o cinco dedos lo tienen mucho más fácil para escribir los números. Los de cinco dedos a buen seguro utilizarán la base 10 que utilizamos nosotros y los de cuatro dedos utilizarán la base 8 que es muy cercana a la base 2 utilizada por los dispositivos digitales.

Para ayudar a los personajes de tres dedos por mano, nos hemos propuesto hacer un conversor de los números en nuestra base 10 a los de base 6.

# Entrada

La entrada empieza con un número indicando el número de casos de prueba que vendrán a continuación. Cada caso de prueba consta de una única línea con el número natural n (0 ≤ n ≤ 1.000.000) que hay que convertir expresado en base 10.

# Salida

Para cada caso de prueba se escribirá una línea con el número n expresado en base 6.

# Entrada de ejemplo

```
3
5
6
12
```

# Salida de ejemplo

```
5
10
20
```
# Solución propuesta

``` python
if __name__ == '__main__':
    BASE = 6
    casos = int(input())
    respuestas = []
    for i in range(casos):
        numero = int(input())
        numero_base = ''
        while numero != 0:
            numero_base = str(numero % BASE) + numero_base
            numero = numero // BASE
        respuestas.append(numero_base)
    for numero in respuestas:
        print(numero)
```

Después de unos ejercicios en los que hemos tenido que hacer uso de estructuras
de datos relativamente complejas, esta vez nos encontramos con un algoritmo que
lo único que nos pide es realizar una conversión de bases, concretamente, de base
10 a base 6.

Lo único que debemos que debemos hacer es dado un número en base 10, comenzar a
dividir el número entre 6 donde el nuevo número serán los restos de dividir entre
6 hasta que no podamos dividir más.

Al contrario que en otros ejercicios, repito que éste es relativamente sencillo.

[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2017-07-31-mano.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=272&potw=1)

---
layout: post
title: Pirámide de fichas de dominó
---

Blanca aún es demasiado pequeña para saber jugar al dominó, de modo que no entiende por qué sus abuelos se pasan las tardes dando golpes con las fichas sobre la mesa a la vez que gritan cosas como "me doblo", "a doses" o "¡cerrado!".

Pero cuando terminan y se marchan a la cocina a preparar la cena, se siente hipnotizada por las fichas blancas y negras, y se dedica a hacer construcciones con ellas. Una de sus preferidas es una pirámide. Cuando tiene las 28 fichas, hace una fila de 7 fichas, sobre esa coloca otra fila de 6, y así sucesivamente hasta construir una pirámide de 7 pisos, donde en la cúspide hay una única ficha.

![Piramide_28](https://www.aceptaelreto.com/pub/problems/v002/64/st/statements/images/TorreCompleta.png)

El fin de semana pasado empezó a montar su pirámide pero le faltaban dos fichas, que se habían caído al suelo. Al terminar, vio con pesar que su último piso tenía una única ficha, pero el anterior tenía tres, en lugar de dos.

No le gustan las pirámides que no son perfectamente escalonadas (al subir, quiere que cada piso pierda exactamente una ficha), de modo que prefiere construir una pirámide truncada, en la que el último piso tiene más de una ficha. Tras probar un buen rato, consiguió recolocar las 26 fichas en una pirámide de 4 pisos, en el que el piso inferior tenía 8 fichas y el superior 5.

![Piramide_26](https://www.aceptaelreto.com/pub/problems/v002/64/st/statements/images/TorreTruncada.png)

# Entrada

La entrada está compuesta por múltiples casos de prueba. Cada uno aparece en una línea independiente que contiene un número positivo hasta 10.000.000 indicando el número de fichas de dominó disponibles para construir la pirámide.

# Salida

Para cada caso de prueba, el programa escribirá, en una línea independiente, la altura de la pirámide (quizá truncada) más alta que se puede construir usando todas las fichas disponibles.

# Entrada de ejemplo

```
28
26
35
8
```

# Salida de ejemplo

```
7
4
7
1
```
# Solución propuesta

``` python
def gauss(n):
    return (n*(n+1))/2


def piramide_truncada(inicio, fin):
    return gauss(fin) - gauss(inicio)


def piramide(fichas):
    nivel = 1
    total = gauss(nivel)
    while fichas > total:
        nivel += 1
        total = gauss(nivel)
    if fichas < total:
        inicio = 2
        fin = nivel
        total = piramide_truncada(inicio, fin)
        while fichas != total:
            if fichas < total:
                inicio += 1
            else:
                fin += 1
            total = piramide_truncada(inicio, fin)
        respuesta = [fin - inicio, 'TRUNCADA']
    else:
        respuesta = [nivel, 'COMPLETA']

    return respuesta


if __name__ == '__main__':
    fichas = int(input())
    solución = piramide(fichas)
    print(solución[0], solución[1])
```

[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2017-12-18-fichas_domino.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=264)

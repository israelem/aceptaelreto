---
layout: post
title: Natalidad
---

Para luchar contra la superpoblación, en ciertos países se prohíbe a las familias tener más de un hijo. Bien pensado eso significa que a la larga la población disminuirá, pues los dos progenitores de una generación son responsables de un único nacimiento en la siguiente (a lo que habría que añadir la pérdida de población por aquellas personas que no tienen hijos...).

Si nuestro objetivo fuera mantener la población aproximadamente constante, la norma debería ser exigir a las familias que tengan dos hijos, y no uno (por el mismo motivo que antes, la población en realidad iría disminuyendo, pues se admite que haya familias que no tengan hijos).

Al limitar el número de hijos a dos, el árbol genealógico de varias generaciones de una misma familia puede verse como un árbol binario, en donde cada nodo representa un matrimonio que tendrá entre 0 y 2 hijos.

Dado ese árbol binario/genealógico, ¿podrías decir si la familia al completo cumple alguna de las dos normativas anteriores?

# Entrada

La entrada estará compuesta por distintos casos de prueba, cada uno en una línea. Cada caso de prueba contendrá la descripción de una familia completa en forma de árbol genealógico que, como se ha dicho, será siempre binario. Un árbol genealógico vacío marca el último caso, que no deberá procesarse. Cada línea no excederá los 100.000 caracteres.

En la descripción de cada familia, aparece un simple carácter por cada matrimonio con la inicial de uno de los dos progenitores. A continuación aparece la descripción del árbol genealógico de uno de los hijos, seguida de la del otro. El caracter punto (.) indica la _ausencia de hijo_ o lo que es lo mismo, el árbol vacío.


# Salida

Para cada caso de prueba se mostrará una línea indicando qué normativa cumple la familia en cuestión. En concreto, si ningún matrimonio tiene más de un hijo se mostrará un 1; si todos los matrimonios con hijos tienen exactamente dos, se mostrará 2. En cualquier otro caso se mostrará N.

# Entrada de ejemplo

```
A..
AB...
AB..C..
ABC..D...
.
```

# Salida de ejemplo

```
12
1
2
N
```

# Solución propuesta

``` python

```

[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2018-10-01-natalidad.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=201)

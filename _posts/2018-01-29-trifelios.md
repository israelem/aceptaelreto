---
layout: post
title: Trifelios
---

Aunque poca gente sabe lo que es un _trifelio_, casi todo el mundo conoce al menos uno: "_monja_". Como todos los niños saben, si se repite rápidamente esa palabra muchas veces, aparece otra distinta, "_jamón_".

Hay muchas otras parejas de palabras que tienen esta misma propiedad, como "_copa_" y "_Paco_", "_mora_" y "_amor_" o "_diosa_" y "_adiós_".

Otras requieren cambios ortográficos (más allá de las tildes) como "_carro_" y "_roca_", "_llave_" y "_bella_" o "_labio_" y "_viola_".

Por último, también existen algunas parejas que son trifelios al escribirlos, pero no al decirlos, ya sea por cambio de fonética o de entonación (o ambas), como "_cogeré_" y "_recoge_" o "_encuadernaré_" y "_reencuaderna_". Los llamamos trifelios ortográficos.

# Entrada

La entrada comienza con el número de casos de prueba que se deberán procesar. Cada caso ocupará una línea independiente y contendrá dos palabras de no más de 20 letras. Aunque suponga fallos ortográficos, por simplicidad ninguna vocal llevará tilde.

# Salida

Para cada caso de prueba se escribirá "SI" si la pareja de palabras es un trifelio, y "NO" en otro caso.

Dado que fonéticamente la 'b' y la 'v' son similares, deben considerarse iguales. De nuevo por simplicidad, el resto de idiosincrasias del español deberán ignorarse y considerar por tanto únicamente los trifelios _ortográficos_. Ten en cuenta que una palabra no forma un trifelio consigo misma ni, en este problema, con sus posibles variaciones de 'b' y 'v'.


# Entrada de ejemplo

```
5
monja jamon
Paco copa
carro roca
lavese Besela
vota bota
```

# Salida de ejemplo

```
SI
SI
NO
SI
NO
```
# Solución propuesta

``` python
from itertools import permutations


def calcular_permutaciones(palabra: str):
    permutaciones = [''.join(permutacion) for permutacion in permutations(palabra)]
    permutaciones.remove(palabra)
    if 'b' in palabra:
        palabra_v = palabra.replace('b', 'v')
        permutaciones += [''.join(permutacion) for permutacion in permutations(palabra_v)]
        permutaciones.remove(palabra_v)
    elif 'v' in palabra:
        palabra_b = palabra.replace('v', 'b')
        permutaciones += [''.join(permutacion) for permutacion in permutations(palabra_b)]
        permutaciones.remove(palabra_b)
    return permutaciones


if __name__ == '__main__':
    soluciones = []
    numero_parejas = int(input())
    for _ in range(numero_parejas):
        palabra_1, palabra_2 = [x.lower() for x in input().split()]
        if palabra_2 in calcular_permutaciones(palabra_1):
            soluciones.append('SI')
        else:
            soluciones.append('NO')
    for solución in soluciones:
        print(solución)
```

[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2018-01-20-trifelios.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=401)

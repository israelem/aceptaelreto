---
layout: post
title: Triángulos con piedras
---

En su última clase, Dianthe aprendió lo que son los números triangulares. "Si tenéis un número triangular de piedrecitas  — les decía 
Pitágoras — podréis formar un triángulo con el mismo número de piedras en cada lado". Cogiendo pequeñas piedras del suelo, les hizo una 
demostración:

![Triangulos_con_piedras](https://www.aceptaelreto.com/pub/problems/v001/70/st/statements/Spanish/images/TriangulosConPiedras.svg)

Con una sola piedra, se puede formar un triángulo de lado 1. Con 3, se puede formar un triángulo de lado 2. Serán necesarias 10 piedras 
para formar un triángulo de lado 4. En cada paso, se suma una piedra más a las que se añadieron en el paso anterior. Es decir, primero se 
pone una piedra, luego dos más, luego tres más, y así sucesivamente.

Dianthe se pregunta de qué tamaño será el triángulo más grande que puede formar así, si tiene 1000 piedras (aunque es posible que le 
sobren algunas). ¿Puedes ayudarla?

# Entrada

La entrada estará compuesta por múltiples casos de prueba. Cada uno contendrá un único número en una línea, indicando el número de piedras 
que tiene Dianthe (hasta 250.000.000).

La entrada terminará cuando el valor sea 0, que no deberá procesarse.

# Salida

Para cada caso de prueba se debe indicar el tamaño de los lados del triángulo más grande que se puede formar con las piedras disponibles, 
así como el número de piedras que sobrarán.

# Entrada de ejemplo
```
1
6
13
0
```

# Salida de ejemplo

```
1 0
3 0
4 3
```

Autores:	Pedro Pablo Gómez Martín; Patricia Díaz García; Marco Antonio Gómez Martín

Revisores:	Ferran Borrell Micola; Cristina Gómez Alonso; Catalina Molano Alvarado; Roger Meix Mañá

# Solución propuesta

``` python
def suma_n_numeros(n):
    return (pow(n,2)+n)/2

if __name__ == '__main__':
    numero_piedras = int(input())
    while(numero_piedras > 0):
        i = 1;
        while(suma_n_numeros(i)<numero_piedras):
            i += 1
        i -= 1
        sobran = numero_piedras - suma_n_numeros(i)
        print(str(i) + " " + str(int(sobran)))
        numero_piedras = int(input())
```

Si nos fijamos en cuántas piedras hay en cada triángulo, el número de total de piedras es la suma de 1 + 2 + ... + n, siendo n el número de piedras de cada lado. De forma que para resolverlo, podemos utilizar la fórmula de Gauss: (n^2 + n) / 2, que es el resultado que devuelve la función suma_n_numeros.

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/pub/problems/v001/70/st/statements/Spanish/index.html)
[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2017-05-15-triangulos_piedras.py)

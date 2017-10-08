---
layout: post
title: Los saltos de Mario
---

Mario se encuentra ante el castillo final. Puede verlo desde lo alto del muro en el que se encuentra. En breve podrá entrar en la Cámara de Koopa, enfrentarse (y vencer) al monstruo final y salvar a la princesa.

Sin embargo, tiene ante sí una serie de muros que tendrá que sobrepasar. Para eso, saltará desde el primero de ellos, donde se encuentra, al siguiente, y desde él al siguiente, y así sucesivamente hasta llegar al último.

La pregunta que nos hacemos es, ¿cuántos de estos saltos serán hacia arriba y cuántos hacia abajo? Mario realiza un salto hacia arriba cuando tiene que alcanzar un muro que está por encima de él, y hacia abajo cuando tiene que alcanzar un muro que está por debajo.

# Entrada

El primer valor de la entrada es un número que indica la cantidad de casos de prueba a evaluar. Cada caso de prueba comienza con un entero mayor que cero y no mayor que 109 que indica el número de muros del escenario (recuerda que Mario se encuentra situado en la parte de arriba del primero). A continuación se proporciona la serie de enteros que indican la altura de cada uno de ellos.

# Salida

Para cada caso de prueba se mostrará una línea en la que aparecerán dos enteros, uno con los saltos hacia arriba y otro con los saltos hacia abajo, separados por un espacio.

# Entrada de ejemplo

```
3
8
1 4 2 2 3 5 3 4
2
9 9
5
1 2 3 4 5
```

# Salida de ejemplo

```
4 2
0 0
4 0
```
# Solución propuesta

``` python
if __name__ == '__main__':
    soluciones = []
    numero_casos = int(input())
    for caso in range(numero_casos):
        muros = int(input())
        alturas = [int(x) for x in input().split(' ')]
        arriba = 0
        abajo = 0
        for i in range(1, len(alturas)):
            if alturas[i - 1] < alturas[i]:
                arriba += 1
            elif alturas[i - 1] > alturas[i]:
                abajo += 1
        soluciones.append("%d %d" % (arriba, abajo))
    for solucion in soluciones:
        print(solucion)
```

Este ejercicio para los que vivimos en los años 90 tiene un aire melancólico que
no debe distraernos del objetivo principal que es realizar el algoritmo para
resolver el problema que nos proponen. En este caso, y después de todos los que
llevamos, es relativamente sencillo, ya que lo primero que hay que hacer es leer
las distintas alturas de los muros. Después hay que recorrer el array y comparar
valor con el siguiente o en nuestro caso, cada valor con el anterior.

Si el anterior es menor que el siguiente el salto es hacia arriba y si es menor,
es hacia abajo. Una vez contabilizados los saltos en uno u otro sentido solo hay
que almacenarlos en el array (o lista) de soluciones.

[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2017-10-02-saltos_mario.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=161&potw=1)

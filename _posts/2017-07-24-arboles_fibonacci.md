---
layout: post
title: Árboles de Fibonacci
---
Cualquier informático que se precie conoce los números de Fibonacci y ha implementado al menos una vez la función recursiva que los calcula. La definición de la función es:

'''
fib(0) = 0
fib(1) = 1
fib(n) = fib(n - 2) + fib(n - 1)
'''

Hoy no implementaremos una vez más esa función, aunque sí trabajaremos con un concepto similar a los números de Fibonacci: los *árboles* de Fibonacci.

Entendemos por árbol de Fibonacci de tamaño *n* a aquel cuya raíz contiene el número de Fibonacci *fib(n)*, cuyo hijo izquierdo representa el árbol de Fibonacci de tamaño *n* − 2 y el derecho el de *n* − 1. Evidentemente, los árboles de Fibonacci de tamaños 0 y 1 tienen únicamente un nodo raíz con el valor 0 y 1 respectivamente.

¿Podrías dibujar este tipo de árboles?

# Entrada

La entrada estará compuesta por múltiples casos de prueba, cada uno en una línea. Cada caso de prueba consistirá en un número mayor o igual que cero que indicará el tamaño del árbol de Fibonacci que hay que dibujar. Un número negativo marcará el final de la entrada y no generará salida.

# Salida

Para cada caso de prueba se dibujará el árbol de Fibonacci del tamaño solicitado. Después de cada árbol se escribirá una línea con cuatro símbolos de igual (====) para separar un caso de prueba de otro.

El dibujo del árbol se realizará de la siguiente forma:

+   Si el árbol es vacío, escribirá \[vacio\] y después un retorno de carro.
+   Si el árbol es un árbol hoja, escribirá el contenido de la raíz y un retorno de carro.
+   Si el árbol tiene algún hijo, escribirá el contenido del nodo raíz, y recursivamente en las siguientes líneas el hijo izquierdo y después el hijo derecho. Los hijos izquierdo y derecho aparecerán tabulados, dejando tres espacios.

# Entrada de ejemplo

```
0
1
2
3
-1
```

# Salida de ejemplo

```
0
====
1
====
1
   0
   1
====
2
   1
   1
      0
      1
====
```
# Solución propuesta

``` python
class ArbolBinario:

    def __init__(self, valor, izquierda=None, derecha=None):
        self.__valor = valor
        self.__izquierda = izquierda
        self.__derecha = derecha

    def insertar_izquierda(self, valor):
        self.__izquierda = ArbolBinario(valor)
        return self.__izquierda

    def insertar_derecha(self, valor):
        self.__derecha = ArbolBinario(valor)
        return self.__derecha

    def devolver_valor(self):
        return self.__valor

    def imprimir(self, nivel=0):
        espacios = nivel * '   '
        print('%s%d' % (espacios, self.__valor))
        if self.__izquierda:
            self.__izquierda.imprimir(nivel + 1)
        if self.__derecha:
            self.__derecha.imprimir(nivel + 1)
        return None


def arbol_fibonacci(termino):
    if termino == 0:
        return ArbolBinario(termino)
    elif termino == 1:
        return ArbolBinario(termino)
    else:
        izquierda = arbol_fibonacci(termino - 2)
        derecha = arbol_fibonacci(termino - 1)
        valor = izquierda.devolver_valor() + derecha.devolver_valor()
        arbol = ArbolBinario(valor, izquierda, derecha)
        return arbol


def fibonacci(termino):
  if termino == 0:
    return termino
  elif termino == 1:
    return termino
  else:
    return fibonacci(termino - 2) + fibonacci(termino - 1)


if __name__ == '__main__':
    n = int(input())
    while n >= 0:
        arbol = arbol_fibonacci(n)
        arbol.imprimir()
        print('====')
        n = int(input())

```

El punto de partida del ejercicio es la archiconocida serie de Fibonacci de hecho
está definida en el código, antes del main. Dicha función hay varias formas de
implementarlas, yo he optado por una de las más conocidas, como es la recursiva,
incluso si no os habíais fijado, en la propia portada página de
[python.org](http://www.python.org) aparece.

Por otro lado, debemos tratar con una estructura de datos ya conocida como es el
árbol, donde hay que recordar que es una estructura recursiva donde cada nodo
está formado por el dato o valor a almacenar y colgando del nodo uno o más hijos
que a su vez son árboles, excepto en aquellos nodos que no tiene hijos y se
llaman nodos hoja. También hay un nodo que no tiene padre y es la raíz.

Esta explicación nos sirve para Cualquier tipo de árbol que nos encontremos, sin
embargo a los árboles se le pueden poner apellidos, en un ejercicio anterior nos
encontramos un árbol binario de búsqueda y en este ejercicio, nos quedamos solo
con el primero. Por tanto el árbol es un árbol binario, lo que significa es que
cada padre solo tiene dos hijos, izquierda y derecha. Esto significa que las
cosas se simplifican un poco las cosas ya que a la hora de recorrerlo sabremos
el número máximo de hijos.

Ahora volviendo al ejercicio he definido la función arbol_fibonacci, que no deja
de ser una función de fibonacci con esteroides ya que mientras calculamos el
término correspondiente, a su vez generamos el árbol binario que contiene la
sucesión. Por tanto hay que tener cuidado no confundir la llamada recursiva con
la llamada a la creación de la clase ArbolBinario.

Por último dentro de la clase ArbolBinario se define el método imprimir que
nos servirá para imprimir el árbol en el orden en el que nos piden.

Espero no estar siendo demasiado breve en las explicaciones, pero vamos camino
de 3 meses de ejercicios y se comienzan a crear un historial de explicaciones y
lo que no quiero es repetir más de lo necesario.

[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2017-07-24-arboles_fibonacci.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=200&potw=1)

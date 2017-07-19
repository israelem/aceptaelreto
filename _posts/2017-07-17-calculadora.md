---
layout: post
title: La máquina calculadora
---
A Javier le gusta la electrónica y cacharrear para construir máquinas que tengan cierto propósito. Ahora que su hijo Luis está aprendiendo a calcular le ha construido una máquina con un marcador, en el que aparecen cuatro dígitos y tres botones marcados con etiquetas +1, ∗2 y ÷3, que al ser pulsados actualizan el marcador realizando la operación correspondiente (sumar uno, multiplicar por dos o dividir entre tres). Como el marcador solamente tiene cuatro dígitos, las operaciones se realizan módulo 10.000 y la división es entera.

Luis ha entendido perfectamente el funcionamiento de la máquina y la utiliza para comprobar que los cálculos que hace mentalmente antes de pulsar un botón son correctos. Ahora Javier le ha retado con un juego: él configura el marcador para que aparezca un número concreto y le pide a Luis que consiga llegar a otro número pulsando los botones el menor número de veces.

¿Puedes ayudarles calculando cuál es el menor número de pulsaciones que hay que realizar para conseguir que aparezca el número final a partir del original?

![Calculadora](https://www.aceptaelreto.com/pub/problems/v003/19/st/statements/images/maquina.jpg)

# Entrada

El programa dará respuesta a una serie de casos de prueba. Cada caso consiste en una única línea con dos números (entre 0 y 9.999), el que aparece originalmente en el marcador y el que Luis debe conseguir pulsando los botones de la máquina calculadora.

# Salida

Para cada caso de prueba, se escribirá en una línea el menor número de pulsaciones necesarias para conseguir el número final a partir del original.

# Entrada de ejemplo

```
0 1024
5000 0
9999 6666
```

# Salida de ejemplo

```
11
1
2
```
# Solución propuesta

``` python
def resolver(inicio, fin, iteraciones, maximo):
    if iteraciones == maximo:
        respuesta = MAX
    elif inicio == fin:
        respuesta = iteraciones
    else:
        inicio_suma = (inicio + 1) % MAX
        inicio_prod = (inicio * 2) % MAX
        inicio_div = (inicio // 3) % MAX
        respuesta = min(resolver(inicio_suma, fin, iteraciones + 1, maximo),
                        resolver(inicio_prod, fin, iteraciones + 1, maximo),
                        resolver(inicio_div, fin, iteraciones + 1, maximo))
    return respuesta

if __name__ == '__main__':
    MAX = 10000
    inicio, fin = [int(x) for x in input().split(' ')]
    if 0 <= inicio < MAX and 0 <= fin < MAX:
        iteraciones = 0
        maximo = 1
        pulsaciones = MAX
        while pulsaciones == MAX and maximo <= MAX:
            pulsaciones = resolver(inicio,fin, iteraciones, maximo)
            maximo += 1
        if pulsaciones < MAX:
            print(pulsaciones)
        else:
            print("NÚMERO FINAL NO ALCANZADO")
    else:
        print("NÚMEROS FUERA DE RANGO")
```

Este ejercicio, aunque el enunciado es sencillo su resolución no lo es tanto.
Éste es un buen ejemplo de cómo el pensamiento natural puede ser más o menos complicado
plasmarlo en un algoritmo, porque cualquiera de nosotros es capaz de realizar
el ejercicio en el mundo real, pero la hora de describir el proceso mental o los
pasos que les lleva a la solución es a posteriori, más que a priori.

Entonces, para empezar a plantear el problema, imaginamos que dados el número
de inicio vamos a pulsar todas las posibles combinaciones hasta dar con el número
final de modo que así seguro que encontramos la solución o nos cansemos y luego
explicaré eso. Sin olvidar que hay que hacerlo en el mínimo número de pulsaciones
posibles.

Ahora bien, vamos a comenzar con los conceptos necesarios para la resolución del
problema.

Lo primero que vemos es que dado un número de inicio si realizamos una operación
hemos dado un paso, es decir, si es la operación correcta estamos un paso más cerca
de la solución, si no, pues es un paso perdido, aunque no lo sepamos. Todo esto nos
lleva a que en cada paso hemos de realizar las mismas operaciones, de modo que
lo que muchos dirían es una función que de forma iterativa resuelva el problema.
Sin embargo, como vemos en el enunciado, en cada paso tenemos tres posibles opciones,
de modo que si usáramos una solución iterativa (while inicio != fin), solo podríamos
seguir un único camino a cada paso. Esto ha de quedar claro, ya que si no, no se verá
ningún sentido en la solución recursiva propuesta.

Antes de seguir, hay que explicar qué es la recursividad. Se puede definir una función
recursiva como aquella que se llama a sí misma, ya está, así de sencillo. Sin embargo
falta una segunda pata para este banco y es que además de llamarse a sí misma, es necesario
que existan uno o varios casos bases, es decir, un caso que se resuelva sin recurrir
a la llamada de la función.

Vamos a empezar por lo fácil y son los casos bases, el más obvio es que el incio
y el final son iguales, es decir, hemos llegado a una solución. El otro caso base
es el que antes comenté como la alternativa de cuando nos cansemos. Pues bien,
cuando el número de iteraciones llega al máximo que hemos indicado nos hemos cansado
de probar y no hemos encontrado la solución.

Por otro lado la llamada general como he comentado anteriormente hay que realizarla
tres veces, una por cada operación y además, hay que buscar la mejor solución de las
tres, en este caso la que devuelva menos pulsaciones.

Con lo explicado hasta ahora sería suficiente como para dar la solución, sin embargo
hay un parámetro que en principio sobra, el de máximo. ¿Por qué este parámetros?
Originalmente este parámetro no estaba y se usaba como máximo la constante MAX.
Sin embargo, me encontraba con un problema y es que el número de llamadas recursivas
se iba de madre, es decir, empezaba a consumir memoria y tiempo de ejecución como
si no hubiera un mañana. Para evitar esto, decidí ir limitando el número de llamadas
recursivas con este parámetro. De modo que, primero busco todas las soluciones que
impliquen hacer una pulsación, si no lo encuentro, busco las de dos, si no las de
tres así hasta encontrarla o llegar a la profundidad MAX.

Esto tiene lo bueno de que voy limitando las llamadas y así me aseguro de que la
primera solución encontrada será la mejor, pero tiene el inconveniente de que
recalcularé muchas veces los niveles, pero para mantener la solución sencilla es
el precio a pagar.

Por último, quería comentar que la forma en la que he realizado el algoritmo no
ha sido porque se me haya ocurrido así sin más. Una vez más he desempolvado los
conocimientos de la carrera y he intentado utilizar la técnica de *backtracking*
o vuelta atrás algo modificada. Si quieres aprender esta técnica y unas cuantas
más precisamente el libro con el que estudié y que además mantiene su actualidad
porque los fundamentos de algoritmia son los que son es [Técnicas de diseños de Algoritmos](http://www.lcc.uma.es/~av/Libro/)
que se encuentra libre en el enlace, subido por uno de sus autores, el profesor
[Antonio Vallecillo](http://www.lcc.uma.es/~av/).

Como siempre espero que os haya servido y toda mejora o sugerencia sobre el algoritmo
será bienvenida.

[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2017-07-17-calculadora.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=319&potw=1)

---
layout: post
title: Solitario
---

Maneras de jugar al solitario hay tantas como tipos de barajas y países donde se juega con ellas. Siendo muy pequeña, mi abuelo materno me enseñó a jugar a una variedad del solitario muy sencilla utilizando la baraja española. Como en la mayoría de los solitarios, el objetivo es crear cuatro pilas de cartas, una para cada palo, en orden ascendente, es decir del as al rey.

En la modalidad de mi abuelo, se baraja el mazo de cartas y se coloca boca abajo sobre la mano. En cada jugada, se cogen simultáneamente dos cartas de ese mazo y se dan la vuelta sobre la mesa, formando una pila de cartas visibles. De esa pila, sólo podrá retirarse en cada momento la carta situada más arriba.

Durante la partida, se construyen también cuatro pilas de cartas, una para cada palo. Para eso, es necesario primero tener la suerte de que el as de cada palo quede en la parte de arriba de las cartas según van siendo llevadas desde el mazo de la mano a la mesa. Cuando eso ocurre, el as se retira y se coloca iniciando su propia pila, sobre la que podrá luego colocarse el dos de ese palo, luego el tres, etcétera, siempre que queden visibles en el mazo de cartas descubiertas.

Cuando se retira la carta de la parte superior del mazo de cartas descubiertas, la que queda inmediatamente debajo pasa a quedar visible; si es posible colocarla en alguna de las pilas de los palos que se están construyendo, deberá ser colocada también; el proceso continuará hasta que no queden cartas visibles, o la superior no pueda ser colocada.
Inicio del solitario

Por ejemplo, imagina que, tras varias cartas descubiertas, hemos conseguido iniciar las pilas de los palos espadas, copas y oros colocando varias de sus cartas, llegando a la situación de la figura. En la penúltima jugada, extragimos del mazo de cartas boca abajo que tenemos en la mano la sota de oros y el cinco de espadas, que no pudieron ser colocadas. En el último hemos tenido más suerte al sacar el cuatro de espadas y el as de bastos. Éste queda en la parte superior y podemos colocarlo sobre la mesa, iniciando su propia pila. Además, al retirar el as, queda al descubierto el cuatro de espadas, que también colocamos inmediatamente (sobre el tres), y éste a su vez deja visible al cinco, que también extraemos. La sota de oros, que pasa a ser la superior, no se puede colocar, por lo que llega el momento de probar suerte descubriendo dos cartas nuevas del mazo de la mano.

Es importante darse cuenta de que si en lugar del as de bastos hubiera quedado en la parte superior, por ejemplo, el dos de bastos, al no poderlo retirar no podríamos tampoco colocar el cuatro de espadas de debajo.

Lo habitual es que tras llevar todas las cartas por parejas del mazo boca abajo a la mesa, no hayamos sido capaces de construir completas las cuatro pilas de cartas de cada palo. En ese caso, recogemos, sin barajar, las cartas visibles que no hemos colocado y les damos la vuelta, de modo que la última carta que extragimos se convierte en la inferior del mazo boca abajo. Después, repetimos el proceso sacando las cartas de dos en dos otra vez. Es posible que al terminar de descubrir todas las cartas nos quede una única carta en la mano, y no dos. En ese caso, se colocará esta última sobre la pila de cartas visibles y se comprobará si se puede colocar siguiendo el procedimiento habitual.

El jugador gana la partida si consigue colocar todas las cartas en las pilas de los palos, y pierde en caso contrario, lo que ocurre cuando da toda una vuelta a las cartas pendientes sin haber sido capaz de colocar ninguna. 

# Entrada

La entrada consta de una serie de casos de prueba terminados con un 0. Cada caso de prueba consiste en una configuración de baraja formada por uno, dos, tres o cuatro palos; es decir, 10, 20, 30 o 40 cartas. Cada palo consta de 10 cartas con valores desde el 1 (As) hasta el 7, 10 (sota), 11 (caballo) y 12 (rey).

El caso de prueba comenzará por un número que indica el número de palos con el que jugamos el solitario. En la línea siguiente aparecerá la configuración del mazo de cartas inicial, ya barajado, como una secuencia de cartas. El mazo se considera colocado boca abajo, de manera que la primera carta que aparece será la primera que tengamos levantar.

Cada carta se representa con un número y un carácter, que indican el valor de la carta y el palo al que pertenece respectivamente. Se utilizará O para los oros, C para las copas, E para las espadas y B para los bastos. Entre el número y el palo aparecerá un espacio, al igual que entre una carta y la siguiente.

# Salida

Para cada caso de prueba se mostrará una línea en la que se escribirá `GANA` si un jugador del solitario que comience con la configuración del caso de prueba acabará ganando la partida. En caso contrario se escribirá `PIERDE`.

# Entrada de ejemplo

```
1 
1 B 2 B 3 B 4 B 5 B 6 B 7 B 10 B 11 B 12 B
1 
12 E 2 E 3 E 7 E 11 E 10 E 6 E 5 E 4 E 1 E
2
2 O 1 O 2 C 1 C 4 O 3 O 4 C 3 C 12 O 11 O 12 C 11 C 10 O 7 O 10 C 7 C 6 O 5 O 6 C 5 C
0 
```

# Salida de ejemplo

```
PIERDE
GANA
GANA
```
# Solución propuesta

``` python

```

[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2018-05-21-solitario.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=187)

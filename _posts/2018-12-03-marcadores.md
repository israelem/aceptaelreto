---
layout: post
title: Marcadores de 7 segmentos
---

Los paneles informativos están en todos los sitios. Cuando la tecnología se abarató, los carteles de papel se transformaron en letreros luminosos que muestran palabras que van apareciendo por un lado y saliendo por el otro, como el de la figura:

![Rótulo del metro en Asia](https://www.aceptaelreto.com/pub/problems/v001/29/st/statements/Spanish/images/RotuloMetro.jpg)

Cuando uno de estos rótulos se pone en marcha, suele empezar vacío y el texto sale desde el lateral derecho hacia el izquierdo, desplazándose hasta desaparecer.

Su funcionamiento consiste en ir encendiendo y apagando las pequeñas bombillas (LEDs) para dar la sensación de movimiento.

Si en vez de texto necesitamos únicamente mostrar números, el cartel puede ser mucho menos sofisticado utilizando los llamados marcadores de siete segmentos como el siguiente:

![Cartel de 7 segmentos](https://www.aceptaelreto.com/pub/problems/v001/29/st/statements/Spanish/images/Cartel7Segmentos.jpg)

En este caso cada número se representa gracias a la combinación encendido/apagado de únicamente 7 segmentos luminosos que permiten representar todos los números:

![Todos los números en 7 segmentos](https://www.aceptaelreto.com/pub/problems/v001/29/st/statements/Spanish/images/TodosLosLeds.png)

La pregunta que nos hacemos es ¿cuántos cambios de luces (cuántos encendidos y apagados) deberán hacerse para hacer pasar por uno de estos carteles un número determinado?

Por ejemplo, para mostrar el 123 en un cartel de 3 dígitos que comienza con todos los leds apagados tendremos:

![Ejemplo de cambios al mostar '123' en un panel de 3 dígitos](https://www.aceptaelreto.com/pub/problems/v001/29/st/statements/Spanish/images/MarcadorLeds.png)

1. Inicialmente todos los segmentos están apagados.
2. Cuanto entra por la izquierda el 1, se encienden dos segmentos.
3. Al desplazarse el 1 y entrar el 2 se encienden seis segmentos y se apaga otro, lo que hacen un total de 7 cambios.
4. En el siguiente desplazamiento, al entrar el 3, se encienden siete segmentos y se apagan dos.
5. Al desaparecer el 1, el dígito de más a la derecha queda por completo apagado; hay cinco leds que se encienden y siete que se apagan.
6. La desaparición del 2 provoca otro dígito más apagado por completo y un led que se enciende y 6 que se apagan.
7. En el último paso se apagan cinco leds quedándose el marcador completo apagado.

Eso hace un total de 42 cambios de luces. 

# Entrada

La entrada contendrá una línea por cada caso de prueba. En cada línea aparecerá una secuencia de enteros (0 ≤ _n_ ≤ 9) separados por espacios que tendrán el mensaje que se quiere mostrar en el marcador; el fin del mensaje se marca con un -1. El ancho del marcador varía con cada caso de prueba y coincide con el número de dígitos total del mensaje, de forma que todos los mensajes serán completamente visibles durante un instante.

La entrada termina cuando nos encontramos ante un marcador en el que no entrará ningún dígito; este marcador no debe generar ninguna salida.

# Salida

Para cada caso de prueba se mostrará en una línea independiente el número de cambios de estado de las luces del marcador. 

# Entrada de ejemplo

```
1 2 3 -1
3 0 5 -1
1 -1
-1
```

# Salida de ejemplo

```
42
48
4
```

# Solución propuesta

``` python

```

[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2018-12-03-marcadores.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=129)

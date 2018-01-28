---
layout: post
title: Detectando copiones
---
La memoria del viejo profesor de matemáticas ya no es lo que era. Hace años, cuando empezó en eso de ilustrar mentes en blanco, no sólo se sabía los nombres y apellidos de todos sus alumnos sino que además era un lince detectando copias de exámenes. Estaba tan seguro de su habilidad que mientras los alumnos intentaban resolver aquellas derivadas e integrales infernales, él se sentaba en la última fila de la clase a dormir sin preocuparse de que la información fluyera entre los estudiantes.

Su habilidad se basaba en su memoria fotográfica: cuando corregía un examen, era capaz de recordar a la perfección si había visto otro examen con exactamente las mismas respuestas o no. Y si lo encontraba, acusaba al segundo de copiar.

Ahora, con tantos años encima, su memoria fotográfica se limita a sólo unos pocos de los últimos exámenes que ha corregido, por lo que el número de copias que detecta se ha reducido drásticamente.

![Examen](https://www.aceptaelreto.com/pub/problems/v003/38/st/statements/images/examen.jpg)

# Entrada

La entrada contiene distintos casos de prueba, cada uno de ellos formado por dos líneas.

En la primera línea aparecen dos números, _N_ y _K_, que indican, respectivamente, el número de exámenes que tiene que corregir el viejo profesor y el número de exámenes que es capaz de recordar (1 ≤ _N_ ≤ 1.000.000, 1 ≤ _K_ ≤ 100.000). Tras eso, viene una línea con _N_ números (entre 1 y 100.000) separados por espacios que representan las respuestas de cada uno de los exámenes. Dos exámenes se consideran copiados si están representados por el mismo número.

# Salida

Para cada caso de prueba se escribirá una línea con dos números separados por un espacio. El primero indicará el número de exámenes copiados mientras que el segundo dará la cantidad de copias detectadas por el profesor, sabiendo que, en el momento de corregir un examen, éste es capaz de recordar únicamente los _K_ exámenes inmediatamente anteriores.

# Entrada de ejemplo

```
5 1
1 2 1 2 1
5 2
1 2 1 2 1
6 2
1 2 3 1 2 1
```

# Salida de ejemplo

```
3 0
3 3
3 1
```
# Solución propuesta

``` python
def f_repetidos_sublistas(sublistas, repetidos):
    # Se inicializa la variable de respuesta
    respuesta = 0
    for lista in sublistas:
        for x in repetidos:
            # Si hay más de dos apariciones se detecta la copia
            if lista.count(x) >= 2:
                respuesta += lista.count(x) - 1
    return respuesta


def f_sublistas(longitud, lista):
    # Se iniciliaza la variable de respuesta
    listas = []
    for i in range(len(lista)-longitud):
        listas.append(lista[i:i+longitud+1])
    return listas

if __name__ == '__main__':
    # variables
    repetidos = []
    copias_totales = 0
    copias_profesor = 0
    # Lectura de datos
    n, k = [int(x) for x in list(input().split(' '))]
    examenes = [int(x) for x in list(input().split(' '))]
    if 1 <= n <= 1000000 \
            and 1 <= k <= 100000 \
            and n == len(examenes):
        for x in examenes:
            if x in repetidos:
                copias_totales += 1
            else:
                repetidos.append(x)
        sublistas = f_sublistas(k, examenes)
        copias_profesor = f_repetidos_sublistas(sublistas, repetidos)
        print('%d %d' % (copias_totales, copias_profesor))
    else:
        print("Los datos de entrada no cumplen las condiciones")
```

Este problema, aunque relativamente sencillo, hay varios puntosa a acalarar.

+   A la hora de leer los datos se utiliza como en otras soluciones listas por comprensión,
esto permite que en una sola línea devuelva los valores convertidos en variables numéricas.

+   A continuación se recorre la lista de exámenes, en este bucle relleno la variable
repetidos, que es una lista con los distintos exámenes. Realmente, no estoy seguro de
que el nombre sea del todo explicativo. En este bucle aprovecho para contar las
copias que hay realmente de cada examen.

+   La función f_sublistas es necesaria ya que si leemos atentamente el enunciado, el profesor
cuenta los exámenes haciendo precisamente sublistas de la lista total de exámenes, siendo estas
sublistas de tamaño k tal y como nos indican en la entrada. Por ello, se recorre y haciendo
uso del *slice* se van recuperando cada sublista.

+   Por último, la función f_repetidos_sublistas, solo hay que comprobar cuántos repetidos
hay en cada sublista, de cada tipo de examen, por supuesto. En este caso llamamos a la función
*count*, que nos permite contar las apariciones de un elemento en una lista. Aquí hay que tener
en cuenta que para que los alumnos se copien, han de existir al menos dos exámenes iguales
dentro del rango de lo que es capaz de recordar el profesor.

Espero que os guste este problema que no es más que un ejercicio de manejo de listas.

[Enlace del código](https://github.com/israelem/aceptaelreto/blob/master/codes/2017-06-19-detectando_copiones.py)

[Enlace en aceptaelreto.com](https://www.aceptaelreto.com/problem/statement.php?id=338&potw=1)

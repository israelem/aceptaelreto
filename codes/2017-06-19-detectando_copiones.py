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

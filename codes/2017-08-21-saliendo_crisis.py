if __name__ == '__main__':
    respuestas = []
    numero_muestras = int(input())
    while numero_muestras != 0:
        salida = True
        indicadores = [int(x) for x in input().split(' ')]
        anterior = indicadores[0]
        posicion = 1
        while posicion < len(indicadores) and anterior < indicadores[posicion]:
            anterior = indicadores[posicion]
            posicion += 1
        if posicion == len(indicadores):
            respuestas.append('SI')
        else:
            respuestas.append('NO')
        numero_muestras = int(input())
    for respuesta in respuestas:
        print(respuesta)

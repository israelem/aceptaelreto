from statistics import mode


def moda(muestras):
    frecuencias = {}
    for muestra in muestras:
        if muestra not in frecuencias.keys():
            frecuencias[muestra] = 1
        else:
            frecuencias[muestra] += 1
    valores = []
    frecuencia_maxima = max(frecuencias.values())
    for clave in frecuencias.keys():
        if frecuencia_maxima == frecuencias[clave]:
            valores.append(clave)
    return valores


if __name__ == '__main__':
    soluciones = []
    tamano_muestra = int(input())
    while tamano_muestra:
        muestras = [int(x) for x in input().split(' ')]
        #  soluciones.append(moda(muestras))
        soluciones.append(mode(muestras))
        tamano_muestra = int(input())
    for solucion in soluciones:
        print(solucion)

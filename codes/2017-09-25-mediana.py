from statistics import median

if __name__ == '__main__':
    soluciones = []
    tamaño_muestra = int(input())
    while tamaño_muestra:
        muestras = [int(x) for x in input().split(' ')]
        soluciones.append(median(muestras) * 2)
        tamaño_muestra = int(input())
    for solucion in soluciones:
        print(solucion)

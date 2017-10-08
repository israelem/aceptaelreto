if __name__ == '__main__':
    soluciones = []
    numero_casos = int(input())
    for caso in range(numero_casos):
        casos = [int(x) for x in input().split(' ')]
        temperaturas = [int(x) for x in input().split(' ')]
        picos = 0
        valles = 0
        for i in range(1, len(temperaturas)-1):
            if temperaturas[i - 1] < temperaturas[i] > temperaturas[i + 1]:
                picos += 1
            elif temperaturas[i - 1] > temperaturas[i] < temperaturas[i + 1]:
                valles += 1
        soluciones.append("%d %d" % (picos, valles))
    for solucion in soluciones:
        print(solucion)

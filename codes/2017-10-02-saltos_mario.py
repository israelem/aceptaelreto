if __name__ == '__main__':
    soluciones = []
    numero_casos = int(input())
    for caso in range(numero_casos):
        muros = int(input())
        alturas = [int(x) for x in input().split(' ')]
        arriba = 0
        abajo = 0
        for i in range(1, len(alturas)):
            if alturas[i - 1] < alturas[i]:
                arriba += 1
            elif alturas[i - 1] > alturas[i]:
                abajo += 1
        soluciones.append("%d %d" % (arriba, abajo))
    for solucion in soluciones:
        print(solucion)

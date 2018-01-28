def gauss(n):
    return (n*(n+1))/2


def piramide_truncada(inicio, fin):
    return gauss(fin) - gauss(inicio)


def piramide(fichas):
    nivel = 1
    total = gauss(nivel)
    while fichas > total:
        nivel += 1
        total = gauss(nivel)
    if fichas < total:
        inicio = 2
        fin = nivel
        total = piramide_truncada(inicio, fin)
        while fichas != total:
            if fichas < total:
                inicio += 1
            else:
                fin += 1
            total = piramide_truncada(inicio, fin)
        respuesta = [fin - inicio, 'TRUNCADA']
    else:
        respuesta = [nivel, 'COMPLETA']

    return respuesta


if __name__ == '__main__':
    fichas = int(input())
    solución = piramide(fichas)
    print(solución[0], solución[1])

def gauss(n):
    return (n + 1) * n / 2


def pares(n):
    lista = []
    for x in range(0, n + 1):
        lista.append([x, n - x])
    return lista


if __name__ == '__main__':
    casos = int(input())
    respuestas = []
    for caso in range(casos):
        par = [int(x) for x in input().split(' ')]
        total = sum(par)
        previos = int(gauss(total))
        lista = pares(total)
        respuestas. append(previos + lista.index(par) + 1 )
    for respuesta in respuestas:
        print(respuesta)

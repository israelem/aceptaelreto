from functools import reduce


def cadena_a_numero(cadena, revés=False):
    lista = sorted([c for c in cadena], reverse=revés)
    número = int(reduce(lambda x, y: x + y, lista))
    return número


def rellenar_ceros(cadena):
    if len(cadena) < 4:
        cadena += '0' * (4 - len(cadena))
    return cadena


if __name__ == '__main__':
    soluciones = []
    número_casos = int(input())
    for _ in range(número_casos):
        número = input()
        solución = -1
        if número == '6174':
            solución = 0
        elif reduce(lambda x, y: x and y, list(map(lambda x: número[0] == x, número))):
            solución = 8
        else:
            solución = 0
            while número != '6174':
                mayor = cadena_a_numero(número, True)
                menor = cadena_a_numero(número)
                número = rellenar_ceros(str(mayor - menor))
                solución += 1
        soluciones.append(solución)
    for solución in soluciones:
        print(solución)

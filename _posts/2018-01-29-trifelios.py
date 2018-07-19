from itertools import permutations


def calcular_permutaciones(palabra: str):
    permutaciones = [''.join(permutacion) for permutacion in permutations(palabra)]
    if 'rr' in palabra:
        palabra_r = palabra.replace('rr', 'r')
        permutaciones += [''.join(permutacion) for permutacion in permutations(palabra_r)]
    if 'b' in palabra:
        palabra_v = palabra.replace('b', 'v')
        permutaciones += [''.join(permutacion) for permutacion in permutations(palabra_v)].remove(palabra_v)
    if 'v' in palabra:
        palabra_b = palabra.replace('v', 'b')
        permutaciones += [''.join(permutacion) for permutacion in permutations(palabra_b)].remove(palabra_b)
    return permutaciones


if __name__ == '__main__':
    soluciones = []
    numero_parejas = int(input())
    for _ in range(numero_parejas):
        palabra_1, palabra_2 = [x.lower() for x in input().split()]
        if palabra_2 in calcular_permutaciones(palabra_1):
            soluciones += 'SI'
        else:
            soluciones += 'NO'
    for solución in soluciones:
        print(solución)
